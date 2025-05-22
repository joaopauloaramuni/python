from transformers import pipeline
import emoji

# Modelos disponíveis
modelos_disponiveis = {
    "1": "nlptown/bert-base-multilingual-uncased-sentiment",
    "2": "pysentimiento/robertuito-sentiment-analysis",
    "3": "finiteautomata/bertweet-base-sentiment-analysis"
}

# Mapeamento geral
mapa = {
    "1": "muito negativo",
    "2": "negativo",
    "3": "neutro",
    "4": "positivo",
    "5": "muito positivo",
    "POS": "positivo",
    "NEG": "negativo",
    "NEU": "neutro",
    "LABEL_0": "negativo",
    "LABEL_1": "neutro",
    "LABEL_2": "positivo"
}

# Emojis para cada sentimento
emojis = {
    "muito negativo": emoji.emojize("😡"),
    "negativo": emoji.emojize("☹️"),
    "neutro": emoji.emojize("😐"),
    "positivo": emoji.emojize("🙂"),
    "muito positivo": emoji.emojize("😍"),
    "desconhecido": emoji.emojize("❓")
}

def escolher_modelo():
    print("Modelos disponíveis:")
    for chave, nome in modelos_disponiveis.items():
        print(f"{chave} - {nome}")
    print("*" * 150)
    escolha = input("Escolha o modelo (número): ").strip()
    return modelos_disponiveis.get(escolha)

def analisar_sentimento(modelo, texto):
    analisador = pipeline("sentiment-analysis", model=modelo)
    resultado = analisador(texto)[0]
    return resultado

def interpretar_resultado(label):
    chave_mapa = label.strip().split()[0].upper()
    interpretacao = mapa.get(chave_mapa, "desconhecido")
    emoji_sentimento = emojis.get(interpretacao, emojis["desconhecido"])
    return interpretacao, emoji_sentimento

def main():
    modelo = escolher_modelo()
    if not modelo:
        print("Modelo inválido. Encerrando.")
        return

    texto = input("Digite o texto a ser analisado: ").strip()
    resultado = analisar_sentimento(modelo, texto)
    interpretacao, emoji_sentimento = interpretar_resultado(resultado['label'])

    print("*" * 150)
    print(f"Texto: {texto}")
    print(f"Modelo usado: {modelo}")
    print(f"Classificação bruta: {resultado['label']}")
    print(f"Score de confiança: {resultado['score']:.2f}")
    print(f"Sentimento interpretado: {interpretacao} {emoji_sentimento}")
    print("*" * 150)

if __name__ == "__main__":
    main()
