from transformers import pipeline
from typing import List, Dict, Tuple
from statistics import mean
import emoji
 
# Modelos disponíveis
MODELOS_DISPONIVEIS = {
    "1": "nlptown/bert-base-multilingual-uncased-sentiment",
    "2": "pysentimiento/robertuito-sentiment-analysis",
    "3": "finiteautomata/bertweet-base-sentiment-analysis"
}
 
# Mapeamentos de sentimentos
MAPA = {
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
    "LABEL_2": "positivo",
    "POSITIVE": "positivo",
    "NEGATIVE": "negativo",
    "NEUTRAL": "neutro"
}
 
# Emojis
EMOJIS = {
    "muito negativo": emoji.emojize("😡"),
    "negativo": emoji.emojize("☹️"),
    "neutro": emoji.emojize("😐"),
    "positivo": emoji.emojize("🙂"),
    "muito positivo": emoji.emojize("😍"),
    "desconhecido": emoji.emojize("❓")
}
 
def escolher_modelo() -> str:
    print("Modelos disponíveis:")
    for chave, nome in MODELOS_DISPONIVEIS.items():
        print(f"{chave} - {nome}")
    print("*" * 150)
    escolha = input("Escolha o modelo (número): ").strip()
    return MODELOS_DISPONIVEIS.get(escolha)
 
def criar_pipeline(modelo: str):
    return pipeline("sentiment-analysis", model=modelo)
 
def interpretar_resultado(label: str) -> Tuple[str, str]:
    chave = label.strip().split()[0].upper()
    interpretacao = MAPA.get(chave, "desconhecido")
    emoji_sentimento = EMOJIS.get(interpretacao, EMOJIS["desconhecido"])
    return interpretacao, emoji_sentimento
 
def analisar_conversa(mensagens: List[str], analisador) -> List[Dict]:
    resultados = []
    for msg in mensagens:
        output = analisador(msg)[0]
        label = output['label'].strip().upper()
        score = output['score'] if label in ['POSITIVE', 'LABEL_2', '5', '4'] else -output['score']
        resultados.append({
            'text': msg,
            'label': label,
            'sentiment': label,
            'reliability': score
        })
    return resultados
 
def calcular_sentimento_geral(resultados: List[Dict]) -> Tuple[str, float]:
    media = mean([r['reliability'] for r in resultados])
    if media > 0.2:
        return 'POSITIVO', media
    elif media < -0.2:
        return 'NEGATIVO', media
    else:
        return 'NEUTRO', media
 
def exibir_resultados(resultados: List[Dict]):
    print("\n" + "*" * 150)
    print("Resultados por linha:")
    for res in resultados:
        interpretacao, emoji_sent = interpretar_resultado(res['label'])
        print(f'> "{res["text"]}" → {interpretacao} - Confiança: ({abs(res["reliability"]):.2f}) {emoji_sent}')
 
def main():
    modelo_escolhido = escolher_modelo()
    if not modelo_escolhido:
        print("Modelo inválido. Encerrando.")
        return
 
    analisador = criar_pipeline(modelo_escolhido)
 
    print("Digite as mensagens (uma por linha). Digite 'FIM' para finalizar:")
    mensagens = []
    while True:
        linha = input()
        if linha.strip().upper() == "FIM":
            break
        mensagens.append(linha)
 
    resultados = analisar_conversa(mensagens, analisador)
    sentimento_geral, media_score = calcular_sentimento_geral(resultados)
 
    exibir_resultados(resultados)
 
    print("\n" + "*" * 150)
    print(f"Sentimento geral da conversa: {sentimento_geral} (Confiança média: {abs(media_score):.2f})")
    print("*" * 150)
 
if __name__ == "__main__":
    main()
 
 