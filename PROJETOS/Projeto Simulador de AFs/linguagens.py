from automato import AutomatoFinito

def linguagem_apenas_a_b():
    automato = AutomatoFinito(['a', 'b'])
    automato.adicionar_estado('q0', is_final=True)  # Único estado, inicial e final
    automato.definir_inicial('q0')
    automato.definir_transicao('q0', 'a', 'q0')  # Permite 'a'
    automato.definir_transicao('q0', 'b', 'q0')  # Permite 'b'

    return automato

def linguagem_terminadas_em_ab():
    automato = AutomatoFinito(['a', 'b'])
    automato.adicionar_estado('q0')          # Estado inicial
    automato.adicionar_estado('q1')          # Estado após 'a'
    automato.adicionar_estado('q2', is_final=True)  # Estado final após 'ab'
    automato.definir_inicial('q0')

    # Transições
    automato.definir_transicao('q0', 'a', 'q1')  # Transição de q0 para q1 com 'a'
    automato.definir_transicao('q1', 'b', 'q2')  # Transição de q1 para q2 com 'b'
    automato.definir_transicao('q1', 'a', 'q1')  # Permite múltiplos 'a' antes do 'b'
    automato.definir_transicao('q0', 'b', 'q0')  # Ignora 'b' no estado inicial
    automato.definir_transicao('q2', 'a', 'q1')  # Volta para q1 após 'ab' com 'a'
    automato.definir_transicao('q2', 'b', 'q0')  # Volta para q0 após 'ab' com 'b'

    return automato

def linguagem_par_de_as():
    automato = AutomatoFinito(['a', 'b'])
    automato.adicionar_estado('q0', is_final=True)  # Par de 'a's
    automato.adicionar_estado('q1')                # Ímpar de 'a's
    automato.definir_inicial('q0')
    automato.definir_transicao('q0', 'a', 'q1')  # Alterna para 'q1' com 'a'
    automato.definir_transicao('q1', 'a', 'q0')  # Alterna para 'q0' com 'a'
    automato.definir_transicao('q0', 'b', 'q0')  # Permite 'b' sem alterar estado
    automato.definir_transicao('q1', 'b', 'q1')  # Permite 'b' sem alterar estado

    return automato

def linguagem_contem_aa():
    automato = AutomatoFinito(['a', 'b'])
    automato.adicionar_estado('q0')          # Estado inicial
    automato.adicionar_estado('q1')          # Estado após o primeiro 'a'
    automato.adicionar_estado('q2', is_final=True)  # Estado final após 'aa'
    automato.definir_inicial('q0')

    # Transições
    automato.definir_transicao('q0', 'a', 'q1')  # Vai para 'q1' com 'a'
    automato.definir_transicao('q1', 'a', 'q2')  # Vai para 'q2' com 'a'
    automato.definir_transicao('q1', 'b', 'q0')  # Volta para 'q0' com 'b'
    automato.definir_transicao('q0', 'b', 'q0')  # Permite 'b' no estado inicial
    automato.definir_transicao('q2', 'a', 'q2')  # Permanece em 'q2' após atingir o estado final
    automato.definir_transicao('q2', 'b', 'q2')  # Permanece em 'q2' após atingir o estado final

    return automato

def linguagem_somente_ab_repetido():
    automato = AutomatoFinito(['a', 'b'])
    automato.adicionar_estado('q0')          # Estado inicial
    automato.adicionar_estado('q1')          # Estado após 'a'
    automato.adicionar_estado('q2', is_final=True)  # Estado final após 'ab'
    automato.adicionar_estado('e')        # Estado de erro
    automato.definir_inicial('q0')

    # Transições válidas
    automato.definir_transicao('q0', 'a', 'q1')  # Aceita 'a' no início
    automato.definir_transicao('q1', 'b', 'q2')  # Aceita 'b' após 'a'
    automato.definir_transicao('q2', 'a', 'q1')  # Reinicia o padrão com 'a'

    # Transições para estado de erro
    automato.definir_transicao('q0', 'b', 'e')  # 'b' inesperado no início
    automato.definir_transicao('q1', 'a', 'e')  # Dois 'a' consecutivos
    automato.definir_transicao('q2', 'b', 'e')  # Dois 'b' consecutivos

    # Estado de erro é absorvente
    automato.definir_transicao('e', 'a', 'e')
    automato.definir_transicao('e', 'b', 'e')

    return automato
