import tkinter as tk
from time import strftime, localtime

# Lista correta dos dias da semana de acordo com tm_wday (0 = segunda, 6 = domingo)
dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira',
               'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

# Função para atualizar a hora e a data
def atualizar_relogio(rotulo_hora, rotulo_data):
    hora_atual = strftime('%H:%M:%S')
    hoje = localtime()
    dia_semana = dias_semana[hoje.tm_wday]
    data_formatada = f'{dia_semana}, {strftime("%d/%m/%Y")}'

    rotulo_hora.config(text=hora_atual)
    rotulo_data.config(text=data_formatada)

    # Atualiza a cada 1 segundo
    rotulo_hora.after(1000, atualizar_relogio, rotulo_hora, rotulo_data)

# Função principal
def main():
    # Janela principal
    janela = tk.Tk()
    janela.title('Relógio Digital')
    janela.geometry('350x100')
    janela.resizable(False, False)
    janela.configure(bg='black')

    # Rótulo da data
    rotulo_data = tk.Label(janela, font=('Arial', 14), fg='lime', bg='black')
    rotulo_data.pack(pady=(10, 0))

    # Rótulo da hora
    rotulo_hora = tk.Label(janela, font=('Arial', 36, 'bold'), fg='lime', bg='black')
    rotulo_hora.pack()

    # Inicia a atualização
    atualizar_relogio(rotulo_hora, rotulo_data)

    # Loop da interface
    janela.mainloop()

# Executa o programa
if __name__ == '__main__':
    main()
