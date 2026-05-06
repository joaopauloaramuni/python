import cv2
import face_recognition
import os
import numpy as np


def inicializar_sistema():
    """
    Inicializa o sistema de reconhecimento facial.
    Apenas imprime a mensagem inicial.
    """
    print("Iniciando o sistema de Reconhecimento Facial...")


def obter_diretorio_base():
    """
    Retorna o diretório onde o arquivo principal (main.py) está localizado.
    """
    return os.path.dirname(os.path.abspath(__file__))


def preparar_pasta_conhecidos(diretorio_atual):
    """
    Garante que a pasta de rostos conhecidos exista.
    Se não existir, cria a pasta e orienta o usuário.
    """
    pasta_conhecidos = os.path.join(diretorio_atual, "rostos_conhecidos")

    if not os.path.exists(pasta_conhecidos):
        os.makedirs(pasta_conhecidos)
        print(f"Pasta '{pasta_conhecidos}' criada! Coloque fotos com o seu rosto lá dentro (ex: Davi.jpg)")

    return pasta_conhecidos


def carregar_rostos_conhecidos(pasta_conhecidos):
    """
    Carrega as imagens da pasta e gera os encodings faciais.
    Retorna listas de encodings e nomes.
    """
    rostos_conhecidos = []
    nomes_conhecidos = []

    for arquivo in os.listdir(pasta_conhecidos):
        if arquivo.endswith(('.jpg', '.jpeg', '.png')):
            caminho_imagem = os.path.join(pasta_conhecidos, arquivo)
            nome = os.path.splitext(arquivo)[0]

            try:
                foto = face_recognition.load_image_file(caminho_imagem)
                encoding = face_recognition.face_encodings(foto)[0]
                rostos_conhecidos.append(encoding)
                nomes_conhecidos.append(nome)
                print(f"Rosto de '{nome}' carregado com sucesso!")
            except Exception as e:
                print(f"Não foi possível carregar ou encontrar um rosto em '{arquivo}'.")

    return rostos_conhecidos, nomes_conhecidos


def iniciar_webcam():
    """
    Inicializa a webcam padrão (índice 0).
    """
    print("\nAbrindo a webcam... (Pressione 'q' para sair)")
    return cv2.VideoCapture(0)


def processar_frame(frame):
    """
    Reduz o frame, converte para RGB e garante formato correto para o face_recognition.
    Retorna o frame convertido.
    """
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

    print(f"Frame Type: {type(rgb_small_frame)}, Dtype: {rgb_small_frame.dtype}, Shape: {rgb_small_frame.shape}, Contiguous: {rgb_small_frame.flags['C_CONTIGUOUS']}")

    if rgb_small_frame.dtype != np.uint8:
        rgb_small_frame = rgb_small_frame.astype(np.uint8)

    if len(rgb_small_frame.shape) != 3 or rgb_small_frame.shape[2] != 3:
        print("Erro crítico: A câmera não está retornando uma imagem colorida padrão (3 canais).")
        return None

    return rgb_small_frame


def reconhecer_e_desenhar(frame, rgb_small_frame, rostos_conhecidos, nomes_conhecidos):
    """
    Detecta rostos no frame, compara com os conhecidos e desenha retângulos e nomes.
    """
    localizacao_rostos = face_recognition.face_locations(rgb_small_frame)
    encodings_rostos_na_tela = face_recognition.face_encodings(rgb_small_frame, localizacao_rostos)

    for face_encoding, face_location in zip(encodings_rostos_na_tela, localizacao_rostos):
        matches = face_recognition.compare_faces(rostos_conhecidos, face_encoding)
        nome = "Desconhecido"

        if True in matches:
            primeiro_match_index = matches.index(True)
            nome = nomes_conhecidos[primeiro_match_index]

        top, right, bottom, left = face_location
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, nome, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


def loop_principal(video_capture, rostos_conhecidos, nomes_conhecidos):
    """
    Loop principal que captura frames da webcam,
    processa e exibe o reconhecimento facial em tempo real.
    """
    while True:
        ret, frame = video_capture.read()

        if not ret:
            print("Erro: Não foi possível acessar a câmera ou o frame está vazio.")
            break

        rgb_small_frame = processar_frame(frame)

        if rgb_small_frame is None:
            break

        reconhecer_e_desenhar(frame, rgb_small_frame, rostos_conhecidos, nomes_conhecidos)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def finalizar(video_capture):
    """
    Libera a webcam e fecha todas as janelas do OpenCV.
    """
    video_capture.release()
    cv2.destroyAllWindows()


def main():
    """
    Função principal que orquestra toda a execução do sistema.
    """
    inicializar_sistema()
    diretorio_atual = obter_diretorio_base()
    pasta_conhecidos = preparar_pasta_conhecidos(diretorio_atual)
    rostos_conhecidos, nomes_conhecidos = carregar_rostos_conhecidos(pasta_conhecidos)

    video_capture = iniciar_webcam()
    loop_principal(video_capture, rostos_conhecidos, nomes_conhecidos)
    finalizar(video_capture)


if __name__ == "__main__":
    main()