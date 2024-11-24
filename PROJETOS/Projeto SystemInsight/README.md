# Projeto SystemInsight - Sistema de Monitoramento de Hardware

Este projeto fornece informações detalhadas sobre o seu sistema, incluindo CPU, memória, disco, GPU, periféricos conectados, rede e mais.

## Dependências

### Bibliotecas Python

1. **psutil** - Biblioteca para recuperar informações e status de processos e sistemas, como uso de CPU, memória e disco.
   - [Link para psutil](https://pypi.org/project/psutil/)
   
2. **py-cpuinfo** - Fornece informações sobre o processador do sistema, como o modelo e a arquitetura da CPU.
   - [Link para py-cpuinfo](https://pypi.org/project/py-cpuinfo/)
   
3. **GPUtil** - Permite obter informações sobre as GPUs disponíveis no sistema, incluindo uso de memória e temperatura.
   - [Link para GPUtil](https://pypi.org/project/GPUtil/)
   
4. **setuptools** - Ferramenta para facilitar o empacotamento de bibliotecas Python e seus scripts.
   - [Link para setuptools](https://pypi.org/project/setuptools/)
   
5. **hid** - Permite interagir com dispositivos USB HID (Human Interface Device), como teclados e mouses.
   - [Link para hid](https://pypi.org/project/hid/)

6. **hidapi** - Biblioteca que fornece uma interface para comunicação com dispositivos HID (Human Interface Devices) via USB, como teclados, mouses e outros periféricos.
   - [Link para hidapi](https://pypi.org/project/hidapi/)
   - **Instalação via Brew (macOS)**:
      ```bash
      brew install hidapi
      ```
   - **Instalação no Linux (Ubuntu/Debian)**:
      ```bash
      sudo apt-get install libhidapi-dev
      ```
   - **Instalação no Windows**:
   Você pode instalar a versão binária via `pip`:
      ```bash
      pip install hidapi
      ```
   Ou, se necessário, compile a partir do código-fonte, após instalar as dependências do sistema.

### Por que é necessário instalar o hidapi?

O `hidapi` é necessário para interagir com dispositivos HID diretamente através de USB, permitindo que seu código Python se comunique com teclados, mouses, controles de jogos e outros dispositivos. Em sistemas como o macOS e o Linux, é comum que a biblioteca `hidapi` não esteja instalada por padrão, o que torna necessário o processo de instalação. No Windows, a instalação via `pip` deve funcionar diretamente, mas em alguns casos, pode ser necessário compilar a biblioteca se o suporte nativo não estiver presente.

### Instalação

Recomenda-se instalar as dependências dentro de um ambiente virtual. Para isso, siga os passos abaixo:

#### Passo 1: Instalar as dependências

Se o arquivo `requirements.txt` estiver presente, você pode instalar as dependências com o comando:

```bash
pip install -r requirements.txt
```

Caso contrário, instale as dependências manualmente:

```bash
pip install psutil py-cpuinfo gputil setuptools hid
```

#### Passo 2: Criar e ativar o ambiente virtual

1. Crie o ambiente virtual com o seguinte comando:

```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual:
   - No macOS e Linux:

```bash
source .venv/bin/activate
```

   - No Windows:

```bash
.venv\Scripts\activate
```

#### Passo 3: Executar o script

Execute o script principal com o seguinte comando:

```bash
python main.py
```

## Funções

- **get_system_info()**: Obtém informações gerais do sistema, como SO, processador, memória, disco e mais.
  
- **get_gpu_info()**: Detecta as GPUs NVIDIA e exibe suas informações, como memória e uso.

- **get_gpu_temperature()**: Exibe a temperatura da(s) GPU(s) detectada(s).

- **monitoramento_realtime()**: Monitora em tempo real o uso da CPU, memória e disco.

- **get_memory_info()**: Exibe informações sobre o uso da memória do sistema.

- **get_disk_info()**: Exibe informações sobre o uso de disco, incluindo dispositivos e espaço livre.

- **get_connected_peripherals()**: Detecta periféricos conectados ao sistema via HID, como teclados e mouses.

- **get_network_info()**: Exibe informações sobre as interfaces de rede do sistema.

- **get_running_processes()**: Exibe uma lista de processos em execução no sistema.

- **get_logged_in_users()**: Exibe informações sobre os usuários logados no sistema.

- **get_system_uptime()**: Exibe o tempo de atividade do sistema.

- **get_battery_info()**: Exibe informações sobre a bateria, como status e tempo restante.

## Exemplo de resultado

### Informações do Sistema

#### Sistema Operacional
- **Sistema Operacional**: Darwin
- **Versão do SO**: Darwin Kernel Version 24.1.0: Thu Oct 10 21:05:14 PDT 2024; root:xnu-11215.41.3~2/RELEASE_ARM64_T8103
- **Nome do Host**: MacBook-Pro-de-Joao.local
- **IP Local**: 127.0.0.1
- **Arquitetura**: 64bit
- **Processador**: Apple M1
- **Cores Físicos**: 8
- **Cores Lógicos**: 8
- **Memória Total**: 8.0 GB
- **Disco Total**: 228.27 GB
- **GPU**: Detectando...

### GPU
- **Nenhuma GPU NVIDIA detectada ou suportada**

### Temperatura da GPU
- **Nenhuma GPU NVIDIA detectada ou suportada**

### Detalhes do Disco
| Dispositivo             | Tipo | Tamanho Total (GB) | Espaço Livre (GB) |
|-------------------------|------|--------------------|-------------------|
| /dev/disk3s3s1          | apfs | 228.27             | 55.42             |
| /dev/disk3s6            | apfs | 228.27             | 55.42             |
| /dev/disk3s4            | apfs | 228.27             | 55.42             |
| /dev/disk3s2            | apfs | 228.27             | 55.42             |
| /dev/disk1s2            | apfs | 0.49               | 0.47              |
| /dev/disk1s1            | apfs | 0.49               | 0.47              |
| /dev/disk1s3            | apfs | 0.49               | 0.47              |
| /dev/disk3s1            | apfs | 228.27             | 55.42             |

### Memória do Sistema
- **Uso de Memória**: 81.6%
- **Memória Total**: 8.0 GB
- **Memória Livre**: 1.47 GB

### Periféricos Conectados
- **Dispositivo**: Apple Internal Keyboard / Trackpad | ID: 1452:833
- **Dispositivo**: TouchBarUserDevice | ID: 1452:34304
- **Dispositivo**: Keyboard Backlight | ID: 1452:833
- **Dispositivo**: Headset | ID: 0:0

### Informações de Rede
| Interface | Endereço | Família |
|-----------|----------|---------|
| lo0       | 127.0.0.1 | 2       |
| lo0       | ::1       | 30      |
| en0       | 192.168.0.18 | 2    |
| en0       | 3a:74:a1:a8:63:0b | 18 |
| en0       | 2804:14c:5b74:8d56:1059:aa49:2806:68cf | 30 |
| anpi0     | 0a:5c:ec:d7:4b:31 | 18 |
| anpi1     | 0a:5c:ec:d7:4b:32 | 18 |
| en3       | 0a:5c:ec:d7:4b:11 | 18 |

### Processos em Execução
- **PID**: 0 | **Nome**: kernel_task | **Status**: running
- **PID**: 1 | **Nome**: launchd | **Status**: running
- **PID**: 254 | **Nome**: Python | **Status**: running

### Usuários Logados
- **Usuário**: joaopauloaramuni | **Terminal**: Desconhecido | **IP**: None

### Tempo de Atividade do Sistema
- **Tempo de Atividade**: 03:23:02

### Monitoramento - CPU, Memória, Disco e Periféricos
- **Uso de CPU**: 12.3%
- **Uso de Memória**: 81.6% | **Total**: 8.0GB | **Livre**: 1.47GB
- **Disco**: /dev/disk3s3s1 | **Tipo**: apfs | **Tamanho Total**: 228.27GB | **Livre**: 55.42GB

### Informações da Bateria
- **Percentual da Bateria**: 87%
- **Status**: Descarregando
- **Tempo Restante**: 20:00:00

## Links úteis

- [psutil](https://pypi.org/project/psutil/)
- [py-cpuinfo](https://pypi.org/project/py-cpuinfo/)
- [GPUtil](https://pypi.org/project/GPUtil/)
- [setuptools](https://pypi.org/project/setuptools/)
- [hid](https://pypi.org/project/hid/)

## Licença

Este projeto está licenciado sob a **Licença MIT**.