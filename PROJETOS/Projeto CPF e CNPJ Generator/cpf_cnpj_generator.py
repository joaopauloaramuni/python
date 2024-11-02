import random

# Função para validar CPF
def valida_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove qualquer caractere que não seja número
    if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito_1 = (soma * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito_2 = (soma * 10 % 11) % 10

    return digito_1 == int(cpf[9]) and digito_2 == int(cpf[10])

# Função para validar CNPJ
def valida_cnpj(cnpj: str) -> bool:
    cnpj = ''.join(filter(str.isdigit, cnpj))  # Remove qualquer caractere que não seja número
    if len(cnpj) != 14 or cnpj == cnpj[0] * len(cnpj):
        return False

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    digito_1 = (soma % 11)
    digito_1 = 0 if digito_1 < 2 else 11 - digito_1

    # Cálculo do segundo dígito verificador
    soma = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    digito_2 = (soma % 11)
    digito_2 = 0 if digito_2 < 2 else 11 - digito_2

    return digito_1 == int(cnpj[12]) and digito_2 == int(cnpj[13])

# Função para gerar CPF válido
def gera_cpf() -> str:
    while True:
        cpf = [random.randint(0, 9) for _ in range(9)]
        cpf_completo = ''.join(map(str, cpf)) + '00'  # Preencher com '00' para completar 11 dígitos
        if valida_cpf(cpf_completo):
            return cpf_completo

# Função para gerar CNPJ válido
def gera_cnpj() -> str:
    while True:
        cnpj = [random.randint(0, 9) for _ in range(12)]
        cnpj_completo = ''.join(map(str, cnpj)) + '00'  # Preencher com '00' para completar 14 dígitos
        if valida_cnpj(cnpj_completo):
            return cnpj_completo

# Função principal
def main():
    # Gerar e validar CPF
    cpf = gera_cpf()
    cpf_valido = valida_cpf(cpf)
    print(f"CPF Gerado: {cpf}")
    print(f"CPF é válido? {cpf_valido}\n")
    
    # Gerar e validar CNPJ
    cnpj = gera_cnpj()
    cnpj_valido = valida_cnpj(cnpj)
    print(f"CNPJ Gerado: {cnpj}")
    print(f"CNPJ é válido? {cnpj_valido}\n")
    
    # Exemplos de validação com valores fixos
    cpf_teste = "12345678909"  # Insira um CPF para teste
    cpf_teste_valido = valida_cpf(cpf_teste)
    print(f"Validação de CPF (123.456.789-09): {cpf_teste_valido}\n")
    
    cnpj_teste = "11222333000181"  # Insira um CNPJ para teste
    cnpj_teste_valido = valida_cnpj(cnpj_teste)
    print(f"Validação de CNPJ (11.222.333/0001-81): {cnpj_teste_valido}")

# Chamar a função principal
if __name__ == "__main__":
    main()
