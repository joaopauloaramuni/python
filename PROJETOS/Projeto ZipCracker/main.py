# import necessary modules
from pathlib import Path
from zipfile import ZipFile
from tqdm import tqdm

# import the word-list
word_list = Path("rockyou.txt")
zip_file_path = Path("secret.zip")


def crack_password():
    # initialize the zip-file object
    zip_file = ZipFile(zip_file_path)

    # count the number of words in the word-list
    n_words = len(list(open(word_list, 'rb')))

    # check how many passwords there are to test
    print('[2] Total de senhas a testar:', f'{n_words:,}')

    with open(word_list, 'rb') as wordlist:
        for word in tqdm(wordlist, total=n_words, unit='word'):
            try:
                zip_file.extractall(pwd=word.strip())

            except:
                continue

            else:
                print('\n[+] Senha encontrada:', word.decode().strip())
                # tqdm.write(f'\n[+] Senha encontrada: {word.decode(errors="ignore").strip()}')
                exit(0)

    print("\n[!] Senha não encontrada. Tente com outra wordlist.")


if word_list.exists() and zip_file_path.exists():
    crack_password()

else:
    print('[x] Caminho incorreto ou arquivo inexistente.')
    exit(1)

# pip install tqdm
