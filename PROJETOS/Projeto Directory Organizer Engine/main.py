import sys
import logging
from engine.application.main_app import MainApplication
from engine.config.settings import LOG_FILE_NAME

def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE_NAME,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'
    )

def main():
    try:
        print("--- Iniciando aplicação ---")
        setup_logging()
        
        print("Configurando Application...")
        app = MainApplication()
        
        print("Iniciando mainloop (Janela deve aparecer agora)...")
        app.run()
    except Exception as e:
        logging.critical(f"Falha ao iniciar a aplicação: {str(e)}")
        print(f"Erro Fatal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
