"""
Sistema AraMovies - Análise e predição de dados cinematográficos.

Este módulo implementa funcionalidades para:
- Leitura de dados de filmes
- Organização em estruturas de dados
- Visualização gráfica
- Predição de receita usando regressão linear
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from filme import Filme


def criar_filmes_exemplo():
    """
    Cria uma lista de filmes de exemplo para análise.
    
    Returns:
        list: Lista de objetos Filme
    """
    filmes = [
        Filme("Matrix", 63000000, 465000000, "Ficção"),
        Filme("Titanic", 200000000, 2200000000, "Drama"),
        Filme("Avatar", 237000000, 2847000000, "Ficção"),
        Filme("Joker", 55000000, 1074000000, "Drama"),
        Filme("Interestelar", 165000000, 677000000, "Ficção")
    ]
    return filmes


def agrupar_por_genero(filmes):
    """
    Agrupa filmes por gênero em um dicionário.
    
    Args:
        filmes (list): Lista de objetos Filme
        
    Returns:
        dict: Dicionário com gêneros como chaves e listas de filmes como valores
    """
    filmes_por_genero = {}
    
    for filme in filmes:
        if filme.genero not in filmes_por_genero:
            filmes_por_genero[filme.genero] = []
        filmes_por_genero[filme.genero].append(filme)
    
    return filmes_por_genero


def calcular_lucro_medio(filmes):
    """
    Calcula o lucro médio de uma lista de filmes.
    
    Args:
        filmes (list): Lista de objetos Filme
        
    Returns:
        float: Lucro médio
    """
    if not filmes:
        return 0
    
    lucros = [filme.lucro() for filme in filmes]
    return sum(lucros) / len(lucros)


def obter_generos_unicos(filmes):
    """
    Obtém conjunto de gêneros únicos.
    
    Args:
        filmes (list): Lista de objetos Filme
        
    Returns:
        set: Conjunto de gêneros
    """
    return set(filme.genero for filme in filmes if filme.genero)


def preparar_dados_regressao(filmes):
    """
    Prepara os dados para regressão linear.
    
    Args:
        filmes (list): Lista de objetos Filme
        
    Returns:
        tuple: (orcamentos, receitas) como arrays NumPy
    """
    orcamentos = np.array([f.orcamento for f in filmes]).reshape(-1, 1)
    receitas = np.array([f.receita for f in filmes])
    
    return orcamentos, receitas


def treinar_modelo_regressao(orcamentos, receitas, test_size=0.4, random_state=42):
    """
    Treina um modelo de regressão linear.
    
    Args:
        orcamentos (np.array): Array de orçamentos
        receitas (np.array): Array de receitas
        test_size (float): Proporção dos dados para teste
        random_state (int): Seed para reprodutibilidade
        
    Returns:
        tuple: (modelo, X_train, X_test, y_train, y_test)
    """
    # Divide dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        orcamentos, receitas, test_size=test_size, random_state=random_state
    )
    
    # Cria e treina o modelo
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    return modelo, X_train, X_test, y_train, y_test


def exibir_metricas_modelo(modelo, X_test, y_test):
    """
    Exibe métricas do modelo treinado.
    
    Args:
        modelo: Modelo LinearRegression treinado
        X_test: Dados de teste (features)
        y_test: Dados de teste (target)
    """
    print("\n=== Métricas do Modelo ===")
    print(f"Coeficiente (a): {modelo.coef_[0]:.2f}")
    print(f"Intercepto (b): {modelo.intercept_:.2f}")
    
    # Calcula R²
    r2 = modelo.score(X_test, y_test)
    print(f"R² (coeficiente de determinação): {r2:.4f}")
    print()


def comparar_predicoes(modelo, X_test, y_test):
    """
    Compara valores reais e previstos.
    
    Args:
        modelo: Modelo treinado
        X_test: Dados de teste
        y_test: Valores reais
    """
    y_pred = modelo.predict(X_test)
    
    print("=== Comparação: Real vs Previsto ===")
    for real, previsto in zip(y_test, y_pred):
        print(f"Real: R$ {real:,.0f} | Previsto: R$ {previsto:,.0f}")
    print()
    
    return y_pred


def prever_receita(modelo, orcamento):
    """
    Prevê receita para um dado orçamento.
    
    Args:
        modelo: Modelo treinado
        orcamento (float): Orçamento do filme
        
    Returns:
        float: Receita prevista
    """
    return modelo.predict(np.array([[orcamento]]))[0]


def plotar_regressao_linear(filmes, orcamentos, receitas, modelo):
    """
    Plota gráfico de dispersão com linha de regressão.
    
    Args:
        filmes (list): Lista de objetos Filme
        orcamentos (np.array): Array de orçamentos
        receitas (np.array): Array de receitas
        modelo: Modelo treinado
    """
    plt.figure(figsize=(10, 6))
    
    # Gráfico de dispersão
    plt.scatter(orcamentos, receitas, alpha=0.6, s=100)
    
    # Linha de regressão
    plt.plot(orcamentos, modelo.predict(orcamentos), color="red", linewidth=2, 
             label="Linha de Regressão")
    
    # Adiciona nomes dos filmes
    for filme, x, y in zip(filmes, orcamentos, receitas):
        plt.text(x.item(), y.item(), filme.titulo, fontsize=9, ha='right', va='bottom')
    
    plt.xlabel("Orçamento (R$)", fontsize=12)
    plt.ylabel("Receita (R$)", fontsize=12)
    plt.title("Regressão Linear: Receita x Orçamento", fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plotar_residuos(X_test, y_test, y_pred):
    """
    Plota gráfico de resíduos.
    
    Args:
        X_test: Dados de teste (features)
        y_test: Valores reais
        y_pred: Valores previstos
    """
    residuos = y_test - y_pred
    
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, residuos, alpha=0.6, s=100)
    plt.axhline(0, color="red", linestyle="--", linewidth=2, label="Resíduo Zero")
    
    plt.xlabel("Orçamento (R$)", fontsize=12)
    plt.ylabel("Resíduo (R$)", fontsize=12)
    plt.title("Análise de Resíduos da Regressão", fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plotar_orcamento_receita_por_genero(filmes, orcamentos, receitas):
    """
    Plota gráfico de dispersão colorido por gênero.
    
    Args:
        filmes (list): Lista de objetos Filme
        orcamentos (np.array): Array de orçamentos
        receitas (np.array): Array de receitas
    """
    generos = [f.genero for f in filmes]
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=orcamentos.flatten(), y=receitas, hue=generos, s=150, alpha=0.7)
    
    plt.xlabel("Orçamento (R$)", fontsize=12)
    plt.ylabel("Receita (R$)", fontsize=12)
    plt.title("Orçamento x Receita por Gênero", fontsize=14, fontweight='bold')
    plt.legend(title="Gênero")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plotar_frequencia_generos(filmes):
    """
    Plota gráfico de barras com frequência de filmes por gênero.
    
    Args:
        filmes (list): Lista de objetos Filme
    """
    filmes_por_genero = agrupar_por_genero(filmes)
    generos = list(filmes_por_genero.keys())
    frequencias = [len(filmes_por_genero[g]) for g in generos]
    
    plt.figure(figsize=(10, 6))
    plt.bar(generos, frequencias, color=['#3498db', '#e74c3c'], alpha=0.7)
    
    plt.xlabel("Gênero", fontsize=12)
    plt.ylabel("Quantidade de Filmes", fontsize=12)
    plt.title("Distribuição de Filmes por Gênero", fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()


def criar_tabela_comparacao(X_test, y_test, y_pred):
    """
    Cria DataFrame com comparação entre valores reais e previstos.
    
    Args:
        X_test: Dados de teste
        y_test: Valores reais
        y_pred: Valores previstos
        
    Returns:
        DataFrame: Tabela de comparação
    """
    comparacao = pd.DataFrame({
        "Orçamento": X_test.flatten(),
        "Receita Real": y_test,
        "Receita Prevista": y_pred,
        "Erro": y_test - y_pred
    })
    
    return comparacao


def exibir_estatisticas_basicas(filmes):
    """
    Exibe estatísticas básicas sobre os filmes.
    
    Args:
        filmes (list): Lista de objetos Filme
    """
    print("\n=== Estatísticas Básicas ===")
    print(f"Total de filmes: {len(filmes)}")
    print(f"Gêneros únicos: {obter_generos_unicos(filmes)}")
    print(f"Lucro médio: R$ {calcular_lucro_medio(filmes):,.2f}")
    
    # Lucro por gênero
    filmes_por_genero = agrupar_por_genero(filmes)
    print("\nLucro médio por gênero:")
    for genero, lista_filmes in filmes_por_genero.items():
        lucro_medio = calcular_lucro_medio(lista_filmes)
        print(f"  {genero}: R$ {lucro_medio:,.2f}")
    print()


def main():
    """
    Função principal que executa o pipeline completo de análise.
    """
    print("="*60)
    print(" "*15 + "ARAMOVIES - ANÁLISE DE FILMES")
    print("="*60)
    
    # 1. Criar dados de exemplo
    filmes = criar_filmes_exemplo()
    print(f"\n✓ {len(filmes)} filmes carregados com sucesso!")
    
    # 2. Exibir estatísticas básicas
    exibir_estatisticas_basicas(filmes)
    
    # 3. Preparar dados para regressão
    orcamentos, receitas = preparar_dados_regressao(filmes)
    
    # 4. Treinar modelo
    modelo, X_train, X_test, y_train, y_test = treinar_modelo_regressao(
        orcamentos, receitas
    )
    print("✓ Modelo de regressão linear treinado!")
    
    # 5. Exibir métricas
    exibir_metricas_modelo(modelo, X_test, y_test)
    
    # 6. Comparar predições
    y_pred = comparar_predicoes(modelo, X_test, y_test)
    
    # 7. Fazer predição para novo filme
    orcamento_novo = 100_000_000
    receita_prevista = prever_receita(modelo, orcamento_novo)
    print("=== Predição para Novo Filme ===")
    print(f"Orçamento: R$ {orcamento_novo:,}")
    print(f"Receita prevista: R$ {receita_prevista:,.0f}")
    print()
    
    # 8. Criar tabela de comparação
    tabela = criar_tabela_comparacao(X_test, y_test, y_pred)
    print("=== Tabela Detalhada de Comparação ===")
    print(tabela.to_string(index=False))
    print()
    
    # 9. Gerar visualizações
    print("Gerando visualizações...")
    print("  • Gráfico de regressão linear")
    plotar_regressao_linear(filmes, orcamentos, receitas, modelo)
    
    print("  • Gráfico de resíduos")
    plotar_residuos(X_test, y_test, y_pred)
    
    print("  • Gráfico por gênero")
    plotar_orcamento_receita_por_genero(filmes, orcamentos, receitas)
    
    print("  • Distribuição de gêneros")
    plotar_frequencia_generos(filmes)
    
    print("\n" + "="*60)
    print(" "*15 + "ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()