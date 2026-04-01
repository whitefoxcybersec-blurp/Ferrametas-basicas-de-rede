import socket
import threading
from urllib import request

IP = input("Insira IP alvo: ")
PORT = input("Insira Porta alvo: ")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f'[*] Ouvindo em {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Conexão aceita de {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=client_handler, args=(client,))
        client_handler.start()
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Recebido: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__=='__main__':
    main()