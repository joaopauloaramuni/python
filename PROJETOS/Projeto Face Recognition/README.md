# 🎯 Projeto Face Recognition

Sistema de **reconhecimento facial em tempo real** utilizando webcam, desenvolvido em Python com as bibliotecas OpenCV e Face Recognition.

O sistema identifica rostos previamente cadastrados e exibe o nome da pessoa na tela em tempo real.

---

## 📸 Demonstração

- Detecta rostos via webcam  
- Compara com rostos conhecidos  
- Exibe nome ou "Desconhecido"  
- Interface simples usando OpenCV  

---

## 🧠 Sobre o Projeto

Este projeto utiliza técnicas de **visão computacional** e **machine learning** para reconhecimento facial.

Fluxo:

1. Carrega imagens de rostos conhecidos  
2. Gera encodings faciais  
3. Captura frames da webcam  
4. Detecta rostos no frame  
5. Compara com os rostos conhecidos  
6. Exibe o resultado  

---

## 📦 O que é a biblioteca face_recognition?

Biblioteca baseada em dlib que usa deep learning para identificar rostos.

Criada por Adam Geitgey, simplifica o uso de reconhecimento facial em Python.

---

## 📁 Estrutura

📦 face-recognition-project  
 ┣ 📂 rostos_conhecidos  
 ┣ 📜 main.py  
 ┣ 📜 requirements.txt  
 ┗ 📜 README.md  

---

## ⚙️ Requisitos

- Python 3.8+
- Webcam

---

## 📚 Dependências

```
numpy<2.0.0  
opencv-python<4.10.0.0  
setuptools==69.5.1  
face_recognition==1.3.0  
```

---

## 🐍 Ambiente Virtual

### Windows

```
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
```

### Linux / macOS

```
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
```

---

## ▶️ Execução

```bash
python main.py  
```

---

## 📂 Cadastro de Rostos

Adicione imagens na pasta:

- rostos_conhecidos

Exemplo:

```
Davi.jpg  
Joao.png  
```

---

## 📊 Melhorias Futuras

- Banco de dados  
- API REST  
- Melhor precisão  
- Múltiplas imagens por pessoa  

---

## 📚 Documentação e Links Úteis

- 📌 **Face Recognition (GitHub)**  
  https://github.com/ageitgey/face_recognition  

- 🎥 **OpenCV (Visão Computacional)**  
  https://opencv.org/  

- 🔢 **NumPy (Computação Numérica)**  
  https://numpy.org/  

---

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos:

1. Faça um Fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`).
3. Faça commits descritivos (`git commit -m 'Adiciona NovaFeature'`).
4. Push para a branch (`git push origin feature/NovaFeature`).
5. Abra um Pull Request.

---

## 🙏 Agradecimentos

Agradecimentos especiais ao Professor João Paulo Aramuni pela orientação e ajuda na criação deste projeto. Sua contribuição foi fundamental para o desenvolvimento e aprendizado.

---

## 📜 Licença

Este projeto está licenciado sob a MIT License.

---

## 🧑‍💻 Autor

Desenvolvido por <a href="https://github.com/Davii13">Davii13</a>, aluno do 4° período do curso de Engenharia de Software da PUC Minas durante as oficinas de desenvolvimento "DevLabs" ministradas pelo professor João Paulo Aramuni | <a href="https://github.com/Davii13/Directory-Organizer-Engine/issues">Reportar Issues</a>