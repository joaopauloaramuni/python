from graphviz import Digraph

def desenhar_automato(automato, nome_arquivo):
    dot = Digraph()

    # Adiciona a seta para o estado inicial
    dot.node("start", shape="none", label="")  # Nodo fictício para a seta inicial
    dot.edge("start", automato.estado_inicial.nome)  # Conecta ao estado inicial

    for estado in automato.estados.values():
        shape = 'doublecircle' if estado.is_final else 'circle'
        dot.node(estado.nome, shape=shape)
        for simbolo, destinos in estado.transicoes.items():
            for destino in destinos:
                dot.edge(estado.nome, destino, label=simbolo)
    dot.render(f"AFs/{nome_arquivo}", format='png', cleanup=True)
