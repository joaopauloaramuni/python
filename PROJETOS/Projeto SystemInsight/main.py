import os
import platform
import psutil
import socket
import time
import datetime
import hid
import GPUtil
from cpuinfo import get_cpu_info

# Função para obter informações do sistema
def get_system_info():
    system_info = {
        "Sistema Operacional": platform.system(),
        "Versão do SO": platform.version(),
        "Nome do Host": socket.gethostname(),
        "IP Local": socket.gethostbyname(socket.gethostname()),
        "Arquitetura": platform.architecture()[0],
        "Processador": platform.processor(),
        "CPU Detalhada": get_cpu_info()['brand_raw'],
        "Cores Físicos": psutil.cpu_count(logical=False),
        "Cores Lógicos": psutil.cpu_count(logical=True),
        "Memória Total (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Disco Total (GB)": round(psutil.disk_usage('/').total / (1024 ** 3), 2),
        "GPU": "Detectando..."
    }

    # Exibir informações formatadas
    for key, value in system_info.items():
        print(f"{key}: {value}")

# Função para obter informações da GPU
def get_gpu_info():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return ["Nenhuma GPU NVIDIA detectada ou suportada."]
        gpu_info = [
            f"{gpu.name} | Memória: {gpu.memoryTotal}MB | Uso: {gpu.load * 100:.1f}%"
            for gpu in gpus
        ]
        return gpu_info
    except Exception as e:
        return [f"Erro ao detectar GPU: {str(e)}"]

# Função para obter a temperatura da GPU
def get_gpu_temperature():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return ["Nenhuma GPU NVIDIA detectada ou suportada."]
        temperature_info = [
            f"{gpu.name} | Temperatura: {gpu.temperature}°C"
            for gpu in gpus
        ]
        return temperature_info
    except Exception as e:
        return [f"Erro ao detectar temperatura da GPU: {str(e)}"]

# Função para monitorar o uso de CPU, memória e disco
def monitoramento_realtime():
    cpu_usage = psutil.cpu_percent(interval=1)  # uso da CPU em porcentagem
    print(f"Uso de CPU: {cpu_usage}%")

    memory = psutil.virtual_memory()
    print(f"Uso de Memória: {round(memory.percent, 2)}% | Total: {round(memory.total / (1024 ** 3), 2)}GB | Livre: {round(memory.available / (1024 ** 3), 2)}GB")

    for partition in psutil.disk_partitions():
        disk_usage = psutil.disk_usage(partition.mountpoint)
        print(f"Disco: {partition.device} | Tipo: {partition.fstype} | Tamanho Total: {round(disk_usage.total / (1024 ** 3), 2)}GB | Livre: {round(disk_usage.free / (1024 ** 3), 2)}GB")

# Função para obter informações de memória
def get_memory_info():
    memory = psutil.virtual_memory()
    memory_info = {
        "Uso de Memória": f"{round(memory.percent, 2)}%",
        "Memória Total (GB)": round(memory.total / (1024 ** 3), 2),
        "Memória Livre (GB)": round(memory.available / (1024 ** 3), 2)
    }
    return memory_info

# Função para obter informações de disco
def get_disk_info():
    disk_info = []
    for partition in psutil.disk_partitions():
        disk_usage = psutil.disk_usage(partition.mountpoint)
        disk_info.append({
            "Dispositivo": partition.device,
            "Tipo": partition.fstype,
            "Tamanho Total (GB)": round(disk_usage.total / (1024 ** 3), 2),
            "Espaço Livre (GB)": round(disk_usage.free / (1024 ** 3), 2)
        })
    return disk_info

# Função para obter informações sobre os periféricos conectados
def get_connected_peripherals():
    periféricos = hid.enumerate()
    if periféricos:
        peripherals_info = [
            f"Dispositivo: {device['product_string']} | ID: {device['vendor_id']}:{device['product_id']}"
            for device in periféricos
        ]
    else:
        peripherals_info = ["Nenhum dispositivo HID detectado."]
    return peripherals_info

# Função para obter informações de rede
def get_network_info():
    network_info = psutil.net_if_addrs()
    if not network_info:
        return ["Nenhuma interface de rede detectada."]
    network_details = []
    for interface, addresses in network_info.items():
        for address in addresses:
            network_details.append(f"Interface: {interface} | Endereço: {address.address} | Família: {address.family}")
    return network_details

# Função para obter processos em execução
def get_running_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        processes.append(f"PID: {proc.info['pid']} | Nome: {proc.info['name']} | Status: {proc.info['status']}")
    return processes

# Função para obter os usuários logados no sistema
def get_logged_in_users():
    users = psutil.users()
    if not users:
        return "Nenhum usuário logado."
    
    user_info = []
    for user in users:
        # Verifique se o atributo 'term' existe
        term = getattr(user, 'term', 'Desconhecido')  # 'Desconhecido' é o valor padrão se 'term' não existir
        user_info.append(f"Usuário: {user.name}, Terminal: {term}, IP: {user.host}")
    
    return user_info

# Função para obter o tempo de atividade do sistema
def get_system_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
    return f"Tempo de Atividade: {uptime}"

def get_battery_info():
    battery = psutil.sensors_battery()
    if battery:
        # Informações básicas da bateria com psutil
        battery_info = {
            "Percentual da Bateria": f"{battery.percent}%",
            "Status": "Carregando" if battery.power_plugged else "Descarregando",
            "Tempo Restante": str(datetime.timedelta(seconds=battery.secsleft)) if battery.secsleft != psutil.POWER_TIME_UNLIMITED else "Desconhecido"
        }

        return battery_info
    else:
        return "Nenhuma bateria detectada."

def main():
    print("=" * 100)
    print("INFORMAÇÕES DO SISTEMA")
    print("=" * 100)
    get_system_info()
    print("=" * 100)

    print("GPU(s):")
    for gpu in get_gpu_info():
        print(f"  - {gpu}")
    print("=" * 100)

    print("Temperatura da GPU:")
    for temp in get_gpu_temperature():
        print(f"  - {temp}")
    print("=" * 100)

    print("Detalhes do Disco:")
    disk_info = get_disk_info()
    for disk in disk_info:
        print(f"Dispositivo: {disk['Dispositivo']}, Tipo: {disk['Tipo']}, Tamanho Total (GB): {disk['Tamanho Total (GB)']}, Espaço Livre (GB): {disk['Espaço Livre (GB)']}")
    print("=" * 100)

    print("Memória do Sistema:")
    memory_info = get_memory_info()
    for key, value in memory_info.items():
        print(f"{key}: {value}")
    print("=" * 100)

    print("Detectando periféricos conectados (mouse, teclado, etc):")
    peripherals_info = get_connected_peripherals()
    for peripheral in peripherals_info:
        print(f"  - {peripheral}")
    print("=" * 100)

    print("Informações de Rede:")
    network_info = get_network_info()
    for network in network_info:
        print(f"  - {network}")
    print("=" * 100)

    print("Processos em Execução:")
    running_processes = get_running_processes()
    for process in running_processes:
        print(f"  - {process}")
    print("=" * 100)

    print("Usuários Logados:")
    logged_in_users = get_logged_in_users()
    for user in logged_in_users:
        print(f"  - {user}")
    print("=" * 100)

    print("Tempo de Atividade do Sistema:")
    print(get_system_uptime())
    print("=" * 100)

    print("Monitoramento - CPU, Memória, Disco e Periféricos:")
    monitoramento_realtime()
    print("=" * 100)
    
    print("Informações da Bateria:")
    battery_info = get_battery_info()
    if isinstance(battery_info, dict):
        for key, value in battery_info.items():
            print(f"{key}: {value}")
    else:
        print(battery_info)
    print("=" * 100)

if __name__ == "__main__":
    main()

# pip install psutil py-cpuinfo gputil setuptools hid
# brew install hidapi
