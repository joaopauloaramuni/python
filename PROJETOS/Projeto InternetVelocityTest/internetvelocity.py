import streamlit as st
import speedtest


def run_speedtest():
    s = speedtest.Speedtest()
    s.get_best_server()
    download_speed = s.download() / 1_000_000  # Convertendo para Mbps
    upload_speed = s.upload() / 1_000_000  # Convertendo para Mbps
    ping = s.results.ping
    return download_speed, upload_speed, ping


def display_results(download_speed, upload_speed, ping):
    st.write(f"Velocidade de Download: {download_speed:.2f} Mbps")
    st.progress(
        min(download_speed / 100, 1.0)
    )  # Assumindo 100 Mbps como máxima para a barra
    st.write(f"Velocidade de Upload: {upload_speed:.2f} Mbps")
    st.progress(
        min(upload_speed / 100, 1.0)
    )  # Assumindo 100 Mbps como máxima para a barra
    st.write(f"Ping: {ping} ms")


def main():
    st.header("Teste de Velocidade da Internet")
    st.write("Clique no botão abaixo para iniciar o teste.")

    if st.button("Iniciar"):
        with st.spinner("Testando a velocidade da sua internet..."):
            download_speed, upload_speed, ping = run_speedtest()
            display_results(download_speed, upload_speed, ping)


if __name__ == "__main__":
    main()
