"""
Projeto ASCII Webcam Mirror
===========================

Captura a imagem da webcam e a converte, em tempo real, em arte ASCII
exibida diretamente no terminal.

Modos disponíveis:
    mono    -> caracteres brancos (clássico)
    matrix  -> tons de verde estilo "Matrix"
    cor     -> cada caractere recebe a cor real do pixel (truecolor)

Dependências:
    pip install opencv-python numpy

Exemplos de uso:
    python ascii_webcam.py
    python ascii_webcam.py --modo matrix
    python ascii_webcam.py --modo cor --fps 20
    python ascii_webcam.py --inverter --camera 1
    python ascii_webcam.py --estilo katakana     (Matrix de verdade!)
    python ascii_webcam.py --estilo blocos --modo cor
    python ascii_webcam.py --caracteres " .oO@"  (sua própria sequência)

Estilos de caracteres:
    classico  -> " .:-=+*#%@"
    blocos    -> " ░▒▓█"
    katakana  -> katakanas de meia largura, como no filme Matrix
    detalhado -> sequência longa, com mais níveis de brilho

Teclas durante a execução:
    S -> salva um "retrato" ASCII do frame atual em .txt (pasta retratos/)
    Q -> sai do programa (Ctrl+C também funciona)
"""

import argparse
import os
import shutil
import sys
import time
from datetime import datetime

import cv2
import numpy as np

# Leitura de teclado sem travar o programa:
# no Windows usamos msvcrt; no Linux/Mac usamos termios + select.
if os.name == "nt":
    import msvcrt
else:
    import select
    import termios
    import tty


# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

# Conjuntos de caracteres ordenados do "mais escuro" (menos tinta) para o
# "mais claro" (mais tinta). Em um terminal de fundo preto, pixels claros
# viram caracteres densos e pixels escuros viram espaços.
ESTILOS = {
    "classico": " .:-=+*#%@",
    "blocos": " ░▒▓█",
    # Katakanas de MEIA largura (ocupam 1 coluna, como uma letra comum).
    # Os de largura cheia (ア, イ...) ocupariam 2 colunas e distorceriam a imagem.
    "katakana": " ･ｰｱｲｳｴｵｶｷｸｹｺ",
    "detalhado": " .'`^\",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",
}

# Um caractere no terminal é aproximadamente 2x mais alto do que largo.
# Sem essa correção, a imagem sairia "esticada" verticalmente.
PROPORCAO_FONTE = 0.5

# Códigos ANSI de controle do terminal
ANSI_CURSOR_INICIO = "\033[H"     # move o cursor para o canto superior esquerdo
ANSI_LIMPAR_TELA = "\033[2J"      # limpa a tela inteira
ANSI_ESCONDER_CURSOR = "\033[?25l"
ANSI_MOSTRAR_CURSOR = "\033[?25h"
ANSI_RESET = "\033[0m"            # volta às cores padrão
ANSI_LIMPAR_LINHA = "\033[K"      # apaga do cursor até o fim da linha

# Pasta onde os retratos ASCII serão salvos
PASTA_RETRATOS = "retratos"

# Por quantos segundos a mensagem "Retrato salvo" fica visível
DURACAO_MENSAGEM = 2.5


# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

def parse_argumentos():
    """Lê os argumentos de linha de comando e retorna as opções escolhidas."""
    parser = argparse.ArgumentParser(
        description="Espelho ASCII ao vivo usando a webcam."
    )
    parser.add_argument(
        "--modo",
        choices=["mono", "matrix", "cor"],
        default="matrix",
        help="Estilo de cor da saída (padrão: matrix).",
    )
    parser.add_argument(
        "--estilo",
        choices=list(ESTILOS.keys()),
        default="classico",
        help="Conjunto de caracteres usado no desenho (padrão: classico).",
    )
    parser.add_argument(
        "--caracteres",
        type=str,
        default=None,
        help="Sequência personalizada (do mais escuro ao mais claro). "
             "Se informada, substitui o --estilo.",
    )
    parser.add_argument(
        "--camera",
        type=int,
        default=0,
        help="Índice da webcam (padrão: 0).",
    )
    parser.add_argument(
        "--fps",
        type=int,
        default=24,
        help="Limite de quadros por segundo (padrão: 24).",
    )
    parser.add_argument(
        "--inverter",
        action="store_true",
        help="Inverte o brilho (útil em terminais de fundo branco).",
    )
    parser.add_argument(
        "--sem-espelho",
        action="store_true",
        help="Desativa o efeito espelho (imagem não invertida horizontalmente).",
    )
    return parser.parse_args()


def habilitar_ansi_windows():
    """
    No Windows, os códigos ANSI podem vir desativados no console.
    Chamar os.system("") é um truque simples que os habilita.
    """
    if os.name == "nt":
        os.system("")

    # Garante saída em UTF-8, senão caracteres como ░ ou ｱ podem gerar erro
    # (UnicodeEncodeError) em consoles configurados com outra codificação.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass  # versões muito antigas do Python não têm reconfigure


def abrir_camera(indice):
    """Abre a webcam indicada e encerra o programa caso não seja possível."""
    camera = cv2.VideoCapture(indice)
    if not camera.isOpened():
        print(f"Erro: não foi possível abrir a câmera de índice {indice}.")
        sys.exit(1)
    return camera


# ---------------------------------------------------------------------------
# Teclado
# ---------------------------------------------------------------------------

def preparar_teclado():
    """
    No Linux/Mac, coloca o terminal em modo 'cbreak': as teclas são lidas
    na hora, sem precisar apertar Enter. Retorna a configuração original
    para que ela possa ser restaurada no final.
    """
    if os.name == "nt":
        return None  # no Windows o msvcrt já lê teclas diretamente
    fd = sys.stdin.fileno()
    configuracao_original = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    return configuracao_original


def restaurar_teclado(configuracao_original):
    """Devolve o terminal ao modo normal (importante para não 'quebrar' o shell)."""
    if configuracao_original is not None:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, configuracao_original)


def ler_tecla():
    """
    Verifica se alguma tecla foi pressionada, SEM esperar.
    Retorna a tecla em minúsculo, ou None se nada foi pressionado.
    """
    if os.name == "nt":
        if msvcrt.kbhit():
            return msvcrt.getwch().lower()
        return None

    # select com timeout 0 apenas "espia" se há algo para ler
    pronto, _, _ = select.select([sys.stdin], [], [], 0)
    if pronto:
        return sys.stdin.read(1).lower()
    return None


# ---------------------------------------------------------------------------
# Processamento de imagem
# ---------------------------------------------------------------------------

def calcular_dimensoes(largura_frame, altura_frame):
    """
    Calcula quantas colunas e linhas de caracteres cabem no terminal,
    mantendo a proporção da imagem original.
    """
    colunas, linhas = shutil.get_terminal_size()
    linhas_disponiveis = linhas - 1  # reserva a última linha para o status

    # Tenta usar toda a largura do terminal
    largura = colunas
    altura = int(largura * (altura_frame / largura_frame) * PROPORCAO_FONTE)

    # Se a altura estourar o terminal, recalcula a partir da altura
    if altura > linhas_disponiveis:
        altura = linhas_disponiveis
        largura = int(altura * (largura_frame / altura_frame) / PROPORCAO_FONTE)

    return max(largura, 1), max(altura, 1)


def preprocessar_frame(frame, largura, altura, espelhar):
    """
    Redimensiona o frame para o tamanho em caracteres e, se desejado,
    aplica o efeito espelho. Retorna a versão colorida e a versão em cinza.
    """
    if espelhar:
        frame = cv2.flip(frame, 1)  # 1 = inversão horizontal

    # INTER_AREA é o melhor método para reduzir imagens
    pequeno = cv2.resize(frame, (largura, altura), interpolation=cv2.INTER_AREA)
    cinza = cv2.cvtColor(pequeno, cv2.COLOR_BGR2GRAY)
    return pequeno, cinza


def converter_para_indices(cinza, inverter, caracteres):
    """
    Converte cada pixel (0 a 255) em um índice da sequência de caracteres.
    Usa NumPy para processar a imagem inteira de uma vez (muito mais rápido
    do que percorrer pixel por pixel).
    """
    if inverter:
        cinza = 255 - cinza

    niveis = len(caracteres) - 1
    indices = (cinza.astype(np.uint16) * niveis) // 255
    return indices


# ---------------------------------------------------------------------------
# Geração do texto ASCII
# ---------------------------------------------------------------------------

def construir_tabela(modo, caracteres):
    """
    Pré-calcula a string final de cada caractere (já com a cor ANSI).
    Assim, no loop principal, basta consultar a tabela pelo índice,
    sem montar códigos de cor a cada frame.
    """
    tabela = []
    total = len(caracteres)

    for i, caractere in enumerate(caracteres):
        if modo == "matrix":
            # Quanto mais claro o pixel, mais intenso o verde
            verde = 60 + int(195 * i / (total - 1))
            tabela.append(f"\033[38;2;0;{verde};0m{caractere}")
        else:  # mono
            tabela.append(caractere)

    return tabela


def frame_para_ascii(indices, tabela):
    """Monta o texto do frame usando a tabela pré-calculada (modos mono/matrix)."""
    linhas = ["".join(tabela[i] for i in linha) for linha in indices.tolist()]
    return "\n".join(linhas) + ANSI_RESET


def frame_para_ascii_colorido(indices, pequeno_bgr, caracteres):
    """
    Monta o texto do frame no modo 'cor': cada caractere recebe a cor RGB
    real do pixel correspondente. É o modo mais bonito e também o mais pesado.
    """
    linhas = []
    for linha_idx, linha_cor in zip(indices.tolist(), pequeno_bgr.tolist()):
        partes = []
        for indice, (b, g, r) in zip(linha_idx, linha_cor):  # OpenCV usa BGR
            partes.append(f"\033[38;2;{r};{g};{b}m{caracteres[indice]}")
        linhas.append("".join(partes))
    return "\n".join(linhas) + ANSI_RESET


def salvar_retrato(indices, caracteres):
    """
    Salva o frame atual como texto puro (sem códigos de cor) em um arquivo
    .txt com data e hora no nome. Retorna o caminho do arquivo criado.
    """
    os.makedirs(PASTA_RETRATOS, exist_ok=True)

    # Inclui milissegundos para não sobrescrever retratos tirados no mesmo segundo
    carimbo = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
    caminho = os.path.join(PASTA_RETRATOS, f"retrato_{carimbo}.txt")

    linhas = ["".join(caracteres[i] for i in linha) for linha in indices.tolist()]
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(linhas) + "\n")

    return caminho


# ---------------------------------------------------------------------------
# Exibição
# ---------------------------------------------------------------------------

def desenhar(texto, status):
    """
    Desenha o frame no terminal. Em vez de limpar a tela (o que causa
    'piscadas'), apenas volta o cursor ao início e sobrescreve tudo.
    """
    sys.stdout.write(ANSI_CURSOR_INICIO + texto + "\n" + status)
    sys.stdout.flush()


def montar_status(fps_real, modo, estilo, mensagem=None):
    """
    Cria a linha de status exibida abaixo da imagem. Se houver uma mensagem
    (ex.: "Retrato salvo"), ela aparece no lugar das instruções.
    """
    if mensagem:
        texto = f"\033[1;33m{mensagem}"  # amarelo e negrito para chamar atenção
    else:
        texto = f"FPS: {fps_real:5.1f} | modo: {modo} | estilo: {estilo} | S: salvar retrato | Q: sair"
    return f"{ANSI_RESET}{texto}{ANSI_RESET}{ANSI_LIMPAR_LINHA}"


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------

def main():
    args = parse_argumentos()
    habilitar_ansi_windows()

    # Define a sequência de caracteres: a personalizada tem prioridade
    if args.caracteres:
        if len(args.caracteres) < 2:
            print("Erro: --caracteres precisa de pelo menos 2 caracteres.")
            sys.exit(1)
        caracteres = args.caracteres
        nome_estilo = "personalizado"
    else:
        caracteres = ESTILOS[args.estilo]
        nome_estilo = args.estilo

    camera = abrir_camera(args.camera)
    tabela = construir_tabela(args.modo, caracteres)
    intervalo_minimo = 1.0 / args.fps
    tamanho_terminal_anterior = None

    # Controle da mensagem temporária exibida após salvar um retrato
    mensagem = None
    mensagem_ate = 0.0

    # Prepara o terminal e o teclado
    sys.stdout.write(ANSI_ESCONDER_CURSOR + ANSI_LIMPAR_TELA)
    configuracao_teclado = preparar_teclado()

    try:
        while True:
            inicio = time.perf_counter()

            ok, frame = camera.read()
            if not ok:
                print("Erro: falha ao ler o frame da câmera.")
                break

            # Se o usuário redimensionou o terminal, limpa a tela
            # para não sobrar "lixo" de frames maiores
            tamanho_terminal = shutil.get_terminal_size()
            if tamanho_terminal != tamanho_terminal_anterior:
                sys.stdout.write(ANSI_LIMPAR_TELA)
                tamanho_terminal_anterior = tamanho_terminal

            # 1) Calcula o tamanho da imagem em caracteres
            altura_frame, largura_frame = frame.shape[:2]
            largura, altura = calcular_dimensoes(largura_frame, altura_frame)

            # 2) Reduz a imagem e converte para tons de cinza
            pequeno, cinza = preprocessar_frame(
                frame, largura, altura, espelhar=not args.sem_espelho
            )

            # 3) Mapeia cada pixel para um caractere
            indices = converter_para_indices(cinza, args.inverter, caracteres)

            # 4) Gera o texto ASCII de acordo com o modo escolhido
            if args.modo == "cor":
                texto = frame_para_ascii_colorido(indices, pequeno, caracteres)
            else:
                texto = frame_para_ascii(indices, tabela)

            # 5) Controla o FPS: espera se o frame foi gerado rápido demais
            decorrido = time.perf_counter() - inicio
            if decorrido < intervalo_minimo:
                time.sleep(intervalo_minimo - decorrido)

            fps_real = 1.0 / (time.perf_counter() - inicio)

            # 6) Verifica se o usuário apertou alguma tecla
            tecla = ler_tecla()
            if tecla == "q":
                break
            if tecla == "s":
                caminho = salvar_retrato(indices, caracteres)
                mensagem = f"Retrato salvo em {caminho}!"
                mensagem_ate = time.perf_counter() + DURACAO_MENSAGEM

            # Apaga a mensagem depois de alguns segundos
            if mensagem and time.perf_counter() > mensagem_ate:
                mensagem = None

            # 7) Exibe no terminal
            desenhar(texto, montar_status(fps_real, args.modo, nome_estilo, mensagem))

    except KeyboardInterrupt:
        pass  # Ctrl+C: saída normal

    finally:
        # Sempre libera a câmera e restaura o terminal, mesmo em caso de erro
        camera.release()
        restaurar_teclado(configuracao_teclado)
        sys.stdout.write(ANSI_RESET + ANSI_MOSTRAR_CURSOR + ANSI_LIMPAR_TELA + ANSI_CURSOR_INICIO)
        sys.stdout.flush()
        print("Espelho ASCII encerrado. Até a próxima!")


if __name__ == "__main__":
    main()