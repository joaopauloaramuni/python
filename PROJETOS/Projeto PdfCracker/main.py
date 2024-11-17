from pathlib import Path
from tqdm import tqdm
import pikepdf

# Caminhos dos arquivos
word_list = Path("rockyou.txt")
pdf_file_path = Path("protected.pdf")

def crack_pdf_password():
    # Contar o número de palavras na wordlist
    n_words = len(list(open(word_list, 'rb')))
    print('[2] Total de senhas a testar:', f'{n_words:,}')

    # Testar cada senha
    with open(word_list, 'rb') as wordlist:
        for word in tqdm(wordlist, total=n_words, unit='word'):
            password = word.strip().decode(errors="ignore")
            try:
                # Usando pikepdf para tentar abrir o PDF com a senha
                with pikepdf.open(pdf_file_path, password=password):
                    print('\n[+] Senha encontrada:', password)
                    exit(0)
            except pikepdf.PasswordError:
                continue

    print("\n[!] Senha não encontrada. Tente com outra wordlist.")

# Verificar se os arquivos existem
if word_list.exists() and pdf_file_path.exists():
    crack_pdf_password()
else:
    print('[x] Caminho incorreto ou arquivo inexistente.')
    exit(1)

# pip install tqdm pikepdf