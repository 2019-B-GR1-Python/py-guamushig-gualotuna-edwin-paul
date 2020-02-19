import socket
from threading import *

server_port = 3030
IP = '172.17.0.1'
clientes = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class manejarCliente(Thread):
    def __init__(self, cliente, direccion):
        Thread.__init__(self)
        self._cliente = cliente
        self.direccion = direccion

    def run(self):
        self._cliente.send('Servidor: Bienvenido al chat RENEGADOS'.encode())
        while True:
            mensaje = self._cliente.recv(2048)
            if not mensaje:
                self._cliente.send('Cliente desconectado'.encode())
                print(f'Cliente eliminado {str(self.direccion)} Clientes activos: ')
                clientes.remove((self._cliente, self.direccion))
                for i in clientes:
                    print(i[1])
                break
            for i in clientes:
                if not str(self.direccion) == str(i[1]):
                    replica = mensaje.decode('utf-8')
                    i[0].send(replica.encode())
        self._cliente.close()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP, server_port))
    sock.listen()
    print('El servidor esta listo para escuchar')
    while True:
        cliente = sock.accept()
        clientes.append(cliente)
        manejarCliente(cliente[0], cliente[1]).start()


if __name__ == '__main__':
    main()
