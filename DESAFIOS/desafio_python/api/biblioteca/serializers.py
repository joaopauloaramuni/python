from rest_framework import serializers
from .models import *


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome', 'url']


class LivroSerializer(serializers.ModelSerializer):
    # autor = serializers.PrimaryKeyRelatedField(many=False, read_only=False)

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'edicao', 'url']


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'cpf', 'url']


class EmprestimoSerializer(serializers.ModelSerializer):

    def validate_livro(self, value):
        emprestimos = Emprestimo.objects.filter(livro=value, data_devolucao=None)
        if len(emprestimos) > 0:
            raise serializers.ValidationError(
                f"O livro: {value.titulo} já esta emprestado atualmente para: {emprestimos[0].aluno.nome}.")
        return value

    class Meta:
        model = Emprestimo
        fields = ['id', 'aluno', 'livro', 'data_emprestimo', 'data_devolucao', 'esta_emprestado','url']


