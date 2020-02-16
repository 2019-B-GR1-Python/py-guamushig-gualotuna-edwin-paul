import socket
from threading import Thread
from pip._vendor.distlib.compat import raw_input

server_port = 2030
host = '192.168.1.26'


class enviarMensaje(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.sock = sock

    def run(self):
        try:
            usuario = raw_input('Nombre Usuario:')
            while True:
                mensaje = raw_input('')
                if not mensaje:
                    break
                mensaje_a_enivar = usuario + ': '+mensaje
                self.sock.send(mensaje_a_enivar.encode())
            self.sock.close()
        except:
            print('Conexion perdida')


class recibirMensaje(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.sock = sock

    def run(self):
        try:
            while True:
                reply = self.sock.recv(2048)
                if not len(reply):
                    print('Servidor desconectado')
                    break
                print(reply.decode('utf-8'))
            self.sock.close()
        except:
            print('Conexion perdida')
            pass


def main():
    server = (host, server_port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    sock.connect(server)
    recibirMensaje(sock).start()
    enviarMensaje(sock).start()


if __name__ == '__main__':
    main()
