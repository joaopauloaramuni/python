from transformers import pipeline
import numpy as np
import lime
from lime.lime_text import LimeTextExplainer

# Usaremos o pipeline da HuggingFace para sentimento
classifier = pipeline("sentiment-analysis")

class_names = ['NEGATIVE', 'POSITIVE']

def predict_proba(texts):
    # Função para gerar probabilidades para LIME
    results = classifier(texts)
    # Retorna matriz de probabilidades no formato esperado por LIME
    probs = []
    for res in results:
        prob_neg = res['score'] if res['label'] == 'NEGATIVE' else 1 - res['score']
        prob_pos = res['score'] if res['label'] == 'POSITIVE' else 1 - res['score']
        probs.append([prob_neg, prob_pos])
    return np.array(probs)

def explain_sentiment(text):
    explainer = LimeTextExplainer(class_names=class_names)
    exp = explainer.explain_instance(text, predict_proba, num_features=6)
    
    print(f"Texto: {text}\n")
    print(f"Sentimento previsto: {classifier(text)[0]['label']} (confiança {classifier(text)[0]['score']:.2f})\n")
    print("Explicação das palavras que mais impactaram a decisão:\n")
    for word, weight in exp.as_list():
        print(f"{word}: {weight:.4f}")

    # Gera HTML com a explicação:
    exp.save_to_file('explanation.html')

if __name__ == "__main__":
    print("*" * 150)
    frase = input("Digite uma frase para analisar: ")
    explain_sentiment(frase)
    print("*" * 150)
