from transformers import pipeline
import emoji

# Modelos disponíveis
modelos_disponiveis = {
    "1": "nlptown/bert-base-multilingual-uncased-sentiment",
    "2": "pysentimiento/robertuito-sentiment-analysis",
    "3": "finiteautomata/bertweet-base-sentiment-analysis"
}

print("Modelos disponíveis:")
for chave, nome in modelos_disponiveis.items():
    print(f"{chave} - {nome}")

# Escolher modelo
print("*" * 150)
escolha = input("Escolha o modelo (número): ").strip()
modelo = modelos_disponiveis.get(escolha)

if not modelo:
    print("Modelo inválido. Encerrando.")
    exit()

# Criar pipeline com o modelo escolhido
analisador = pipeline("sentiment-analysis", model=modelo)

# Entrada do usuário
texto = input("Digite o texto a ser analisado: ").strip()

# Analisar
resultado = analisador(texto)[0]
label = resultado['label']

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

# Extrair a chave do mapa de forma segura
chave_mapa = label.strip().split()[0].upper()  # Funciona para "4 stars" → "4", e "POS", "LABEL_0", etc.

# Obter a interpretação
interpretacao = mapa.get(chave_mapa, "desconhecido")
emoji_sentimento = emojis.get(interpretacao, emojis["desconhecido"])

# Mostrar resultado
print("*" * 150)
print(f"Texto: {texto}")
print(f"Modelo usado: {modelo}")
print(f"Classificação bruta: {label}")
print(f"Score de confiança: {resultado['score']:.2f}")
print(f"Sentimento interpretado: {interpretacao} {emoji_sentimento}")
print("*" * 150)

# pip install transformers emoji
