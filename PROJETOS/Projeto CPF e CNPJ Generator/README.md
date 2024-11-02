# Gerador e validador de CPF e CNPJ

Este projeto é um gerador e validador de CPF e CNPJ. O código em Python utiliza funções para verificar a validade de CPFs e CNPJs, bem como gerar novos números válidos aleatoriamente.

## Funcionalidades

- **Validação de CPF**: Verifica se um CPF fornecido é válido com base nas regras de cálculo dos dígitos verificadores.
- **Validação de CNPJ**: Verifica se um CNPJ fornecido é válido de acordo com os critérios estabelecidos.
- **Geração de CPF**: Cria um CPF válido aleatoriamente.
- **Geração de CNPJ**: Cria um CNPJ válido aleatoriamente.

## Como executar

Para rodar o projeto, utilize o seguinte comando no terminal: 

```bash
python3 cpf_cnpj_generator.py
```

## Dependências

Este projeto utiliza a biblioteca padrão do Python, por isso não há necessidade de instalar pacotes adicionais.

## Importação da biblioteca random

O código importa a biblioteca `random`, que é parte da biblioteca padrão do Python. A função `random.randint(a, b)` é utilizada para gerar números inteiros aleatórios entre `a` e `b`, que são usados para criar os números de CPF e CNPJ válidos.

## Exemplo de saída

Ao executar o programa, você verá uma saída semelhante a esta:

CPF Gerado: 12345678909 CPF é válido? True

CNPJ Gerado: 11222333000181 CNPJ é válido? True

Validação de CPF (123.456.789-09): True

Validação de CNPJ (11.222.333/0001-81): True

## Licença

Este projeto está licenciado sob a MIT License.
