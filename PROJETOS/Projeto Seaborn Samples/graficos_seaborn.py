import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta
import os


def salvar_grafico(nome_arquivo):
    """Salva o gráfico atual em PNG na pasta 'graficos'."""
    pasta = 'graficos'
    os.makedirs(pasta, exist_ok=True)  # Cria a pasta se não existir
    caminho = os.path.join(pasta, f'{nome_arquivo}.png')
    plt.savefig(caminho, bbox_inches='tight')
    plt.close()  # Fecha a figura atual para liberar memória
    print(f'Gráfico salvo em: {caminho}')


def gerar_dados_csv(nome_arquivo='dados_vendas.csv', linhas=300):
    produtos = ['Notebook', 'Smartphone', 'Tablet', 'Fone de Ouvido', 'Monitor']
    regioes = ['Sul', 'Sudeste', 'Centro-Oeste', 'Norte', 'Nordeste']
    estados = {
        'Sul': ['RS', 'SC', 'PR'],
        'Sudeste': ['SP', 'RJ', 'MG', 'ES'],
        'Centro-Oeste': ['DF', 'GO', 'MT', 'MS'],
        'Norte': ['AM', 'PA', 'RO', 'RR', 'AC'],
        'Nordeste': ['BA', 'PE', 'CE', 'MA', 'PB']
    }

    dados = []
    data_inicial = datetime(2025, 1, 1)

    for _ in range(linhas):
        produto = random.choice(produtos)
        regiao = random.choice(regioes)
        estado = random.choice(estados[regiao])
        data = data_inicial + timedelta(days=random.randint(0, 200))
        vendas = round(random.uniform(100, 5000), 2)
        lucro = round(vendas * random.uniform(0.1, 0.4), 2)

        dados.append({
            'Data': data.strftime('%Y-%m-%d'),
            'Produto': produto,
            'Regiao': regiao,
            'Estado': estado,
            'Vendas': vendas,
            'Lucro': lucro
        })

    df = pd.DataFrame(dados)
    df.to_csv(nome_arquivo, index=False)
    print(f'Arquivo {nome_arquivo} gerado com sucesso!')


# GRÁFICOS BÁSICOS

def grafico_barras(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Produto', y='Vendas', data=df, estimator=sum, errorbar=None)
    plt.title('Vendas Totais por Produto')
    plt.xticks(rotation=45)
    plt.tight_layout()
    salvar_grafico("grafico_barras")
    # plt.show()


def grafico_pizza(df):
    vendas_por_regiao = df.groupby('Regiao')['Vendas'].sum()
    plt.figure(figsize=(6, 6))
    plt.pie(vendas_por_regiao, labels=vendas_por_regiao.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribuição das Vendas por Região')
    plt.axis('equal')
    salvar_grafico("grafico_pizza")
    # plt.show()


def grafico_linha(df):
    df['Data'] = pd.to_datetime(df['Data'])
    df_por_dia = df.groupby('Data')['Vendas'].sum().reset_index()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x='Data', y='Vendas', data=df_por_dia)
    plt.title('Evolução das Vendas ao Longo do Tempo')
    plt.tight_layout()
    salvar_grafico("grafico_linha")
    # plt.show()


def grafico_histograma(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Lucro'], bins=20, kde=True)
    plt.title('Distribuição dos Lucros')
    plt.tight_layout()
    salvar_grafico("grafico_histograma")
    # plt.show()


# GRÁFICOS AVANÇADOS

def grafico_dispersao(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='Vendas', y='Lucro', hue='Produto', data=df)
    plt.title('Vendas vs Lucro por Produto')
    plt.tight_layout()
    salvar_grafico("grafico_dispersao")
    # plt.show()


def grafico_boxplot(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Produto', y='Lucro', data=df)
    plt.title('Distribuição de Lucros por Produto')
    plt.xticks(rotation=45)
    plt.tight_layout()
    salvar_grafico("grafico_boxplot")
    # plt.show()


def grafico_heatmap(df):
    df['Data'] = pd.to_datetime(df['Data'])
    df['Mes'] = df['Data'].dt.month
    tabela = pd.pivot_table(df, values='Vendas', index='Produto', columns='Mes', aggfunc='sum')

    plt.figure(figsize=(10, 6))
    sns.heatmap(tabela, annot=True, fmt=".0f", cmap="YlGnBu")
    plt.title('Heatmap de Vendas por Produto e Mês')
    plt.tight_layout()
    salvar_grafico("grafico_heatmap")
    # plt.show()


def grafico_pairplot(df):
    sns.pairplot(df[['Vendas', 'Lucro']], kind='reg')
    plt.suptitle('Correlação entre Vendas e Lucro', y=1.02)
    salvar_grafico("grafico_pairplot")
    # plt.show()


def grafico_violin(df):
    plt.figure(figsize=(8, 5))
    sns.violinplot(x='Produto', y='Lucro', data=df, hue='Produto', palette='Set2', legend=False)
    plt.title('Distribuição dos Lucros por Produto (Violin Plot)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    salvar_grafico("grafico_violin")
    # plt.show()


def grafico_barras_empilhadas(df):
    vendas_por_produto_regiao = df.groupby(['Produto', 'Regiao'])['Vendas'].sum().unstack()
    vendas_por_produto_regiao.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='tab20')
    plt.title('Vendas por Produto e Região (Barras Empilhadas)')
    plt.ylabel('Vendas Totais')
    plt.xticks(rotation=45)
    plt.tight_layout()
    salvar_grafico("grafico_barras_empilhadas")
    # plt.show()


def main():
    # Geração do CSV
    gerar_dados_csv()

    # Leitura dos dados
    df = pd.read_csv('dados_vendas.csv')

    # Gráficos básicos
    grafico_barras(df)
    grafico_pizza(df)
    grafico_linha(df)
    grafico_histograma(df)

    # Gráficos avançados
    grafico_dispersao(df)
    grafico_boxplot(df)
    grafico_heatmap(df)
    grafico_pairplot(df)
    grafico_violin(df)
    grafico_barras_empilhadas(df)

if __name__ == '__main__':
    main()
