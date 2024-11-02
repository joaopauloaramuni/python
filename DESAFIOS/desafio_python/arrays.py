'''
Tendo os arrays ['ES', 'MG', 'RJ', 'SP'] e ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo'], percorra os vetores dados e crie um outro com a seguinte estrutura: ['ES'=>'Espírito Santo', 'MG'=>'Minas Gerais', 'RJ'=>'Rio de Janeiro', 'SP'=>'São Paulo']. Depois de criado terceiro vetor, leia-o e imprima em cada linha a chave de cada posição e seu respectivo valor separados por "-".
'''
uf_sigla = ['ES', 'MG', 'RJ', 'SP']
uf_cidade = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo']
uf = {}

for indice, sigla in enumerate(uf_sigla):
    uf[sigla] = uf_cidade[(len(uf_cidade) - 1) - indice]

for sigla, nome in uf.items():
    print(f"{sigla}-{nome}")
