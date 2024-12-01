class Estado:
    def __init__(self, nome, is_final=False):
        self.nome = nome
        self.is_final = is_final
        self.transicoes = {}

    def adicionar_transicao(self, simbolo, destino):
        self.transicoes.setdefault(simbolo, []).append(destino)
