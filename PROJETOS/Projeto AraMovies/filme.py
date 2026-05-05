"""
Módulo que define a classe Filme para representar dados cinematográficos.
"""


class Filme:
    """
    Representa um filme com suas características principais.
    
    Atributos:
        titulo (str): Título do filme
        orcamento (int/float): Orçamento de produção
        receita (int/float): Receita total arrecadada
        genero (str): Gênero cinematográfico (opcional)
    """
    
    def __init__(self, titulo, orcamento, receita, genero=None):
        """
        Inicializa um objeto Filme.
        
        Args:
            titulo (str): Título do filme
            orcamento (int/float): Orçamento de produção
            receita (int/float): Receita arrecadada
            genero (str, optional): Gênero do filme. Padrão é None.
        """
        self.titulo = titulo
        self.orcamento = orcamento
        self.receita = receita
        self.genero = genero
    
    def valores_sao_numericos(self):
        """
        Verifica se orçamento e receita são valores numéricos.
        
        Returns:
            bool: True se ambos forem int ou float, False caso contrário
        """
        return isinstance(self.orcamento, (int, float)) and isinstance(self.receita, (int, float))
    
    def lucro(self):
        """
        Calcula o lucro do filme (receita - orçamento).
        
        Returns:
            int/float: Valor do lucro
        """
        return self.receita - self.orcamento
    
    def __str__(self):
        """
        Representação em string do filme.
        
        Returns:
            str: Formato "Título (Gênero)"
        """
        return f"{self.titulo} ({self.genero})"