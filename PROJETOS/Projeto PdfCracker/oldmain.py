from pathlib import Path
from tqdm import tqdm
from PyPDF2 import PdfReader
from PyPDF2._encryption import PasswordType

# Caminhos dos arquivos
word_list = Path("rockyou.txt")
pdf_file_path = Path("protected.pdf")

def crack_pdf_password():
    # Abrir o arquivo PDF
    pdf_reader = PdfReader(pdf_file_path)

    # Contar o número de palavras na wordlist
    n_words = len(list(open(word_list, 'rb')))
    print('[2] Total de senhas a testar:', f'{n_words:,}')

    # Testar cada senha
    with open(word_list, 'rb') as wordlist:
        for word in tqdm(wordlist, total=n_words, unit='word'):
            password = word.strip().decode(errors="ignore")
            # Verificar se a senha foi correta
            result = pdf_reader.decrypt(password)
            if result == PasswordType.USER_PASSWORD or result == PasswordType.OWNER_PASSWORD:
                print('\n[+] Senha encontrada:', password)
                exit(0)

    print("\n[!] Senha não encontrada. Tente com outra wordlist.")

if word_list.exists() and pdf_file_path.exists():
    crack_pdf_password()
else:
    print('[x] Caminho incorreto ou arquivo inexistente.')
    exit(1)

# pip install tqdm PyPDF2
