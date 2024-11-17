from pathlib import Path
from tqdm import tqdm
import rarfile

# Caminho da word-list e do arquivo RAR
word_list = Path("rockyou.txt")
rar_file_path = Path("secret.rar")

# Configurar o rarfile para usar o unrar (é necessário instalar o unrar no sistema)
rarfile.UNRAR_TOOL = "unrar"

def crack_password():
    # Inicializar o objeto do arquivo RAR
    try:
        rar_file = rarfile.RarFile(rar_file_path)

        # Contar o número de palavras na word-list
        n_words = len(list(open(word_list, 'rb')))

        # Exibir o número total de senhas a testar
        print('[2] Total de senhas a testar:', f'{n_words:,}')

        # Abrir a word-list em modo leitura binária
        with open(word_list, 'rb') as wordlist:
            for word in tqdm(wordlist, total=n_words, unit='word'):
                word = word.strip()  # Remover espaços ou caracteres extras
                
                try:
                    # Tentar extrair o conteúdo com a senha
                    rar_file.extractall(pwd=word)

                    print(f'[+] Senha encontrada: {word.decode()}')

                    # Se conseguiu extrair sem erro, a senha é correta
                    print(f'[+] Arquivo extraído com sucesso!')
                    exit(0)

                except rarfile.RarWrongPassword:
                    # Senha incorreta, tenta a próxima
                    continue
                except rarfile.RarLockedArchiveError:
                    # Arquivo está protegido, mas podemos continuar
                    print(f"[x] Arquivo protegido por senha: {rar_file_path}")
                    continue
                except (rarfile.RarCRCError, rarfile.RarFatalError, rarfile.RarOpenError):
                    # Erros de CRC, Fatal ou ao abrir o arquivo
                    print(f"[x] Erro ao acessar o arquivo: {rar_file_path}")
                    continue
                except Exception as e:
                    # print(f"[x] Erro inesperado: {e}")
                    continue

    except rarfile.BadRarFile:
        print("\n[x] Arquivo RAR inválido ou corrompido.")
        exit(1)
    except Exception as e:
        print(f"[x] Erro inesperado ao abrir o arquivo RAR: {e}")
        exit(1)

    print("\n[!] Senha não encontrada. Tente com outra wordlist.")

# Verificar se os caminhos do arquivo RAR e da word-list existem
if word_list.exists() and rar_file_path.exists():
    crack_password()
else:
    print('[x] Caminho incorreto ou arquivo inexistente.')
    exit(1)

# pip install tqdm rarfile
# brew install carlocab/personal/unrar
