import streamlit as st

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    # Título da página
    st.title("🧮 Calculadora de IMC")

    # Subtítulo
    st.markdown("Esta aplicação calcula o **Índice de Massa Corporal (IMC)** com base no peso e altura fornecidos.")

    # Entradas do usuário
    peso = st.number_input("Informe seu peso (kg):", min_value=1.0, max_value=300.0, step=0.1)
    altura = st.number_input("Informe sua altura (m):", min_value=0.5, max_value=2.5, step=0.01)

    # Botão de cálculo
    if st.button("Calcular IMC"):
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        # Exibindo o resultado
        st.success(f"Seu IMC é **{imc}** - {classificacao}")
        
        # Visual feedback
        st.progress(min(int(imc / 40 * 100), 100))

# Executa o app
if __name__ == "__main__":
    main()

# pip install streamlit
# streamlit run imc_streamlit.py
# http://localhost:8501/
