# 📊 Projeto SciPy Samples

Este projeto tem como objetivo didático demonstrar como utilizar algumas funcionalidades essenciais da biblioteca **SciPy** e suas integrações com **NumPy**, **Matplotlib**, **Seaborn** e **Pandas**. Ele inclui exemplos práticos de:

* Integração numérica
* Otimização de funções
* Álgebra linear (resolução de sistemas)
* Estatística descritiva e inferencial (incluindo **Correlação de Pearson**, **Correlação de Spearman** e **Teste Mann–Whitney U**)
* Interpolação de dados
* Transformada de Fourier (FFT)

O intuito é fornecer um guia de estudo prático para estudantes e profissionais que desejam aprender a aplicar ferramentas científicas e matemáticas em Python de forma direta e visual.

---

## 📝 Sobre o projeto

Este projeto foi criado com fins educacionais, para que estudantes e profissionais possam entender e aplicar conceitos matemáticos e científicos em Python de forma prática. Ele oferece exemplos claros e visuais, permitindo que o usuário veja resultados imediatos de integração, otimização, estatística, interpolação e análise de sinais.

---

## 🖼️ Gráficos gerados

| ![histogramas](https://joaopauloaramuni.github.io/python-imgs/SciPySamples/imgs/histogramas.png) | ![dispersao](https://joaopauloaramuni.github.io/python-imgs/SciPySamples/imgs/dispersao.png) | ![spearman\_heatmap](https://joaopauloaramuni.github.io/python-imgs/SciPySamples/imgs/spearman_heatmap.png) | ![interpolacao](https://joaopauloaramuni.github.io/python-imgs/SciPySamples/imgs/interpolacao.png) | ![fft\_sinal](https://joaopauloaramuni.github.io/python-imgs/SciPySamples/imgs/fft_sinal.png) | ![fft\_espectro](https://joaopauloaramuni.github.io/python-imgs/SciPySamples/imgs/fft_espectro.png) |
| :----------------------------------: | :------------------------------: | :---------------------------------------------: | :------------------------------------: | :-------------------------------: | :-------------------------------------: |
|            histogramas.png           |           dispersao.png          |               spearman_heatmap.png              |            interpolacao.png            |           fft_sinal.png           |             fft_espectro.png            |

---

## 📊 Estatística: Conceitos breves

Neste projeto, algumas técnicas estatísticas são demonstradas de forma prática:

* **Correlação de Pearson**: mede a relação linear entre duas variáveis contínuas. Varia de -1 (correlação negativa perfeita) a 1 (correlação positiva perfeita). É sensível à normalização dos dados.

* **Correlação de Spearman**: mede a relação monotônica entre duas variáveis, usando posições (rank) em vez de valores absolutos. Útil quando a relação não é linear e menos sensível a outliers.

* **Teste Mann–Whitney U**: teste não paramétrico que compara duas amostras independentes para verificar se uma tende a ter valores maiores que a outra, sem assumir distribuição normal dos dados.

* **Normalização dos dados**: muitas análises estatísticas, como Pearson, assumem que os dados estejam em escalas comparáveis ou distribuídos normalmente. Normalizar os dados (por exemplo, padronizando média = 0 e desvio = 1) ajuda a tornar os resultados mais confiáveis.

Estes conceitos ajudam a analisar a relação entre dados, testar diferenças estatisticamente significativas e preparar os dados de maneira adequada para análise.

---

## 📦 Instalação das dependências

Para rodar este projeto, instale as bibliotecas necessárias usando o comando:

```bash
pip install numpy scipy matplotlib seaborn pandas
```

---

## ⚙️ Ambiente virtual

Para usar este projeto, recomendamos criar e ativar um ambiente virtual Python:

```bash
# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual

# Windows:
.venv\Scripts\activate

# Linux/macOS:
source .venv/bin/activate
```

---

## 📚 Bibliotecas usadas

* **SciPy 🧪**
  Biblioteca que fornece algoritmos e funções matemáticas avançadas para integração, otimização, álgebra linear, estatística, interpolação e muito mais.

* **NumPy ⚡**
  Biblioteca para computação científica em Python. Suporta arrays multidimensionais e operações matemáticas avançadas de forma eficiente.

* **Pandas 🐼**
  Biblioteca essencial para manipulação e análise de dados em Python. Facilita o trabalho com tabelas e séries temporais, tornando o processo de limpeza e organização dos dados muito mais simples.

* **Seaborn 🎨**
  Biblioteca baseada no Matplotlib que oferece uma interface de alto nível para criar gráficos estatísticos bonitos e informativos de forma simples e elegante.

* **Matplotlib 📈**
  Biblioteca fundamental para criação de gráficos em Python. Permite criar praticamente qualquer tipo de visualização, desde gráficos simples até complexas figuras personalizadas.

---

## 📚 Documentação e links úteis

### SciPy
* Site oficial: [https://scipy.org/](https://scipy.org/)
* Documentação: [https://docs.scipy.org/doc/scipy/](https://docs.scipy.org/doc/scipy/)

### NumPy
* Site oficial: [https://numpy.org/](https://numpy.org/)
* Documentação: [https://numpy.org/doc/](https://numpy.org/doc/)

### Pandas
* Site oficial: [https://pandas.pydata.org/](https://pandas.pydata.org/)
* Documentação: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

### Seaborn
* Site oficial: [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
* Documentação: [https://seaborn.pydata.org/api.html](https://seaborn.pydata.org/api.html)

### Matplotlib
* Site oficial: [https://matplotlib.org/](https://matplotlib.org/)
* Documentação: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)

### Python
* Site oficial: [https://www.python.org/](https://www.python.org/)
* Documentação: [https://docs.python.org/3/](https://docs.python.org/3/)

---

## 🧾 Licença

Este projeto é disponibilizado sob a licença **MIT**.
