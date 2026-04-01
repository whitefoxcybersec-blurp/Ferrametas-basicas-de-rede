import socket

target_host = "IP Alvo"
target_port = "Porta Alvo"

#Objeto Socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Enviar dados
client.sendto(b"AAABBBCCC",(target_host,target_port))

#Receber dados
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
