import requests
import re

# Função para remover tags HTML
def remove_html_tags(text):
    return re.sub(r'<.*?>', '', text)

# Função principal para processar o Kahoot
def process_kahoot(quiz_id):
    # Base da URL
    url_base = "https://play.kahoot.it/rest/kahoots"

    # Construção da URL completa
    url = f"{url_base}/{quiz_id}"

    # Fazendo a requisição
    response = requests.get(url)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()  # Convertendo o JSON para um dicionário Python
        print("*" * 100)
        # Iterando pelas perguntas
        for index, question in enumerate(data.get("questions", []), start=1):
            # Removendo tags HTML da pergunta
            clean_question = remove_html_tags(question["question"])
            print(f"Pergunta {index}:")
            print(clean_question)  # Mostra a pergunta limpa

            # Exibindo as alternativas
            print("Alternativas:")
            for choice in question["choices"]:
                print(f"- {choice['answer']}")
            
            # Encontrando a resposta correta
            correct_answers = [choice["answer"] for choice in question["choices"] if choice["correct"]]
            print(f"Resposta correta: {', '.join(correct_answers)}")
            
            # Imprimindo 100 asteriscos entre as perguntas
            print("*" * 100)
    else:
        print(f"Erro na requisição: {response.status_code}")

# Função main
def main():
    # Variável para o quizId
    quiz_id = "a5fba24d-e7e4-4cf2-8933-efc056232ba4"
    process_kahoot(quiz_id)

# Executa o programa
if __name__ == "__main__":
    main()
