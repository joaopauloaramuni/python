from estado import Estado

class AutomatoFinito:
    def __init__(self, alfabeto):
        self.estados = {}
        self.alfabeto = alfabeto
        self.estado_inicial = None

    def adicionar_estado(self, nome, is_final=False):
        self.estados[nome] = Estado(nome, is_final)

    def definir_transicao(self, estado_origem, simbolo, estado_destino):
        if simbolo not in self.alfabeto and simbolo != "ε":
            raise ValueError("Símbolo inválido para o alfabeto.")
        self.estados[estado_origem].adicionar_transicao(simbolo, estado_destino)

    def definir_inicial(self, nome):
        if nome not in self.estados:
            raise ValueError("Estado inicial inválido.")
        self.estado_inicial = self.estados[nome]

    def simular_entrada(self, entrada):
        estado_atual = self.estado_inicial
        caminho = [estado_atual.nome]

        for simbolo in entrada:
            if simbolo not in estado_atual.transicoes:
                return False, caminho
            estado_atual = self.estados[estado_atual.transicoes[simbolo][0]]
            caminho.append(estado_atual.nome)

        # Verifica se o estado final foi alcançado após processar a palavra
        return estado_atual.is_final, caminho
