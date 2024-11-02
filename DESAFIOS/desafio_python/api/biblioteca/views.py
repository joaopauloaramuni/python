from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import *
from .serializers import *


# Create your views here.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class EmprestimoFilter(filters.FilterSet):
    esta_emprestado = filters.BooleanFilter(field_name='data_devolucao', lookup_expr='isnull')

    class Meta:
        model = Emprestimo
        fields = ['livro', 'aluno', 'data_emprestimo', 'data_devolucao', 'esta_emprestado']


class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmprestimoFilter
