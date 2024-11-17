# Projeto DDoS Attack

Este é um projeto didático para simular um ataque DDoS controlado e seguro usando Python. O script envia múltiplas requisições simultâneas para um serviço de teste, httpbin.org.

## Aviso Legal

Este projeto é apenas para fins educacionais. Jamais utilize este script para atacar sistemas sem permissão explícita, pois isso é ilegal e antiético.

## Como usar

1. Clone o repositório:  
   `git clone https://github.com/seuusuario/ddos_attack.git`  
   `cd ddos_attack`

2. Instale as dependências:  
   `pip install requests`

3. Execute o script:  
   `python main.py`

4. Monitore a saída do terminal para visualizar as respostas do servidor.

## Configuração

- **TARGET_URL**: URL do alvo. Certifique-se de usar apenas alvos seguros para testes.
- **REQUEST_COUNT**: Número de requisições a serem enviadas.

## Uso de Threads

Neste projeto, o uso de **threads** é fundamental para simular o comportamento de um ataque DDoS de forma controlada. Ao invés de enviar as requisições de forma sequencial, utilizamos várias threads para enviar múltiplas requisições simultaneamente. Isso simula a sobrecarga de tráfego que um servidor poderia enfrentar em um ataque real. Cada thread é responsável por enviar uma requisição individual para o servidor-alvo, e o uso de múltiplas threads permite que o script envie até 50 requisições de forma paralela, o que aumenta a eficácia do teste. A biblioteca `threading` do Python é utilizada para criar e gerenciar as threads, garantindo que o código execute as requisições de maneira eficiente e sem bloquear o processo principal.

## Expansão

Você pode modificar este projeto para incluir:
- Testes em servidores locais.
- Logs mais detalhados.
- Métricas de desempenho, como tempo médio de resposta.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
