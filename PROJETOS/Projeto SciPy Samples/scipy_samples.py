import os
import numpy as np
from scipy import integrate, optimize, linalg, stats, interpolate, fft
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
    
# Criar pasta imgs/ se não existir
if not os.path.exists("imgs"):
    os.makedirs("imgs")


def exemplo_integracao():
    """
    Demonstra a integração numérica usando scipy.integrate.quad.
    Calcula ∫ sin(x) dx de 0 a π.
    """
    f = lambda x: np.sin(x)
    # integrate.quad é usado para integração numérica de uma função em um intervalo
    resultado, erro = integrate.quad(f, 0, np.pi)
    print("\n🧮 Integração Numérica:")
    print(f"∫ sin(x) dx de 0 a π = {resultado:.4f}, erro estimado = {erro:.2e}")


def exemplo_otimizacao():
    """
    Demonstra a otimização (minimização) de função usando scipy.optimize.minimize.
    Função usada: f(x) = x^4 - 3*x^3 + 2
    """
    f = lambda x: x**4 - 3*x**3 + 2
    # optimize.minimize tenta encontrar o valor de x que resulta no menor valor para a função f(x)
    # x0 é o chute inicial para a minimização
    resultado = optimize.minimize(f, x0=0)
    print("\n🎯 Otimização:")
    print(f"Valor mínimo encontrado: x = {resultado.x[0]:.4f}, f(x) = {f(resultado.x[0]):.4f}")


def exemplo_algebra_linear():
    """
    Demonstra a resolução de um sistema linear usando scipy.linalg.solve.
    Sistema: 3x + 2y = 5, x + 2y = 5
    """
    # Matriz de coeficientes A
    A = np.array([[3, 2], [1, 2]])
    # Vetor de resultados b
    b = np.array([5, 5])
    # linalg.solve resolve o sistema de equações lineares Ax = b
    x = linalg.solve(A, b)
    print("\n📐 Álgebra Linear:")
    print(f"Solução do sistema Ax = b → x = {x}")


def exemplo_estatistica():
    """
    Demonstra estatística usando scipy.stats e pandas:
    - Média e desvio padrão
    - Correlação de Pearson e Spearman
    - Teste Mann–Whitney U
    - Visualização: histogramas, dispersão e heatmap de correlação
    """
    print("\n📊 Estatística:")

    np.random.seed(42)
    # Geração de duas amostras de dados com pequenas diferenças de média e desvio
    dados1 = np.random.normal(loc=10, scale=2, size=100)
    dados2 = np.random.normal(loc=11, scale=2.5, size=100)

    # Estatística Descritiva: Média (tendência central) e Desvio Padrão (dispersão)
    print(f"Média (dados1) = {np.mean(dados1):.2f}, Desvio = {np.std(dados1):.2f}")
    print(f"Média (dados2) = {np.mean(dados2):.2f}, Desvio = {np.std(dados2):.2f}")

    # Correlação de Pearson
    r_pearson, p_pearson = stats.pearsonr(dados1, dados2)
    print(f"\n📈 Correlação de Pearson: r = {r_pearson:.3f}, p-valor = {p_pearson:.3e}")

    # Correlação de Spearman
    r_spearman, p_spearman = stats.spearmanr(dados1, dados2)
    print(f"🔗 Correlação de Spearman: ρ = {r_spearman:.3f}, p-valor = {p_spearman:.3e}")

    # Teste Mann–Whitney U
    u_stat, p_mannwhitney = stats.mannwhitneyu(dados1, dados2, alternative='two-sided')
    print(f"⚖️  Teste Mann–Whitney U: U = {u_stat:.2f}, p-valor = {p_mannwhitney:.3e}")
    if p_mannwhitney < 0.05:
        print("➡️  Diferença estatisticamente significativa entre as amostras.")
    else:
        print("➡️  Nenhuma diferença significativa detectada.")

    # ---- Gráficos: histogramas e dispersão ----
    
    # histogramas
    plt.figure()
    plt.hist(dados1, bins=15, alpha=0.7, label='dados1')
    plt.hist(dados2, bins=15, alpha=0.7, label='dados2')
    plt.title('Histogramas das Amostras')
    plt.xlabel('Valor')
    plt.ylabel('Frequência')
    plt.legend()
    plt.savefig("imgs/histogramas.png")
    plt.close()

    # dispersão
    plt.figure()
    plt.scatter(dados1, dados2, color='purple')
    plt.title('Dispersão dos Dados')
    plt.xlabel('dados1')
    plt.ylabel('dados2')
    plt.grid(True)
    plt.savefig("imgs/dispersao.png")
    plt.close()


    # ---- Heatmap de Correlação usando pandas (escala para várias variáveis) ----

    # Criar DataFrame com as amostras
    df = pd.DataFrame({'dados1': dados1, 'dados2': dados2})
    # Matriz de correlação Spearman
    corr_matrix = df.corr(method='spearman')

    plt.figure(figsize=(6, 5))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Heatmap de Correlação Spearman')
    plt.savefig("imgs/spearman_heatmap.png")
    plt.close()

    print("➡️  Gráficos salvos em imgs/ (histogramas.png, dispersao.png e spearman_heatmap.png)")


def exemplo_interpolacao():
    """
    Demonstra interpolação cúbica usando scipy.interpolate.interp1d.
    Salva gráfico em imgs/interpolacao.png
    """
    x = np.linspace(0, 10, 10)
    y = np.sin(x)
    # interp1d cria uma função que interpola os pontos originais. 'cubic' usa splines cúbicas.
    f_interp = interpolate.interp1d(x, y, kind='cubic')
    x_novo = np.linspace(0, 10, 50)
    # Usa a função de interpolação para estimar y em novos pontos x
    y_novo = f_interp(x_novo)
    print("\n🔢 Interpolação:")
    print(f"Interpolação cúbica gerada para {len(x_novo)} novos pontos.")

    plt.figure()
    plt.plot(x, y, 'o', label='Pontos Originais')
    plt.plot(x_novo, y_novo, '-', label='Interpolação Cúbica')
    plt.title('Interpolação Cúbica com scipy.interpolate')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.savefig("imgs/interpolacao.png")
    plt.close()


def exemplo_fft():
    """
    Demonstra a transformada de Fourier usando scipy.fft.
    Salva gráfico em imgs/fft.png mostrando o sinal no tempo e o espectro.
    """
    t = np.linspace(0, 1, 500)
    # Cria um sinal composto por duas ondas senoidais (50 Hz e 120 Hz)
    sinal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)
    # fft.fft calcula a Transformada Rápida de Fourier, convertendo o sinal do domínio do tempo para o domínio da frequência.
    espectro = fft.fft(sinal)
    # fft.fftfreq calcula as frequências correspondentes aos pontos do espectro
    freq = fft.fftfreq(t.size, d=t[1] - t[0])
    print("\n⚡ Transformada de Fourier:")
    # np.argmax(np.abs(espectro)) encontra o índice da frequência com maior amplitude (o pico)
    print(f"Frequência de pico: {abs(freq[np.argmax(np.abs(espectro))]):.1f} Hz")

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t, sinal)
    plt.title('Sinal no Tempo')
    plt.xlabel('Tempo [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    # Plota apenas a metade positiva do espectro (suficiente para sinais reais)
    plt.plot(freq[:250], np.abs(espectro)[:250])
    plt.title('Espectro de Frequência (FFT)')
    plt.xlabel('Frequência [Hz]')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("imgs/fft.png")
    plt.close()


def main():
    """
    Função principal que chama todos os exemplos do projeto SciPy Samples.
    """
    print("=== Projeto SciPy Samples ===")
    exemplo_integracao()
    exemplo_otimizacao()
    exemplo_algebra_linear()
    exemplo_estatistica()
    exemplo_interpolacao()
    exemplo_fft()
    print("\n✅ Execução concluída com sucesso!")


if __name__ == "__main__":
    main()

# pip install numpy scipy matplotlib seaborn