from pathlib import Path
from tqdm import tqdm
import pikepdf

# Caminhos dos arquivos
WORD_LIST_PATH = Path("rockyou.txt")
PDF_FILE_PATH = Path("protected.pdf")

def crack_pdf_password(word_list: Path, pdf_file: Path):
    """Tenta quebrar a senha de um PDF usando uma wordlist."""
    # Contar o número de palavras na wordlist
    with open(word_list, 'rb') as f:
        n_words = sum(1 for _ in f)
    print('[2] Total de senhas a testar:', f'{n_words:,}')

    # Testar cada senha
    with open(word_list, 'rb') as wordlist:
        for word in tqdm(wordlist, total=n_words, unit='word'):
            password = word.strip().decode(errors="ignore")
            try:
                with pikepdf.open(pdf_file, password=password):
                    print('\n[+] Senha encontrada:', password)
                    return password
            except pikepdf.PasswordError:
                continue

    print("\n[!] Senha não encontrada. Tente com outra wordlist.")
    return None

def main():
    """Função principal que organiza o fluxo do script."""
    if WORD_LIST_PATH.exists() and PDF_FILE_PATH.exists():
        crack_pdf_password(WORD_LIST_PATH, PDF_FILE_PATH)
    else:
        print('[x] Caminho incorreto ou arquivo inexistente.')
        exit(1)

if __name__ == "__main__":
    main()

# pip install tqdm pikepdf
