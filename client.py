import socket
import threading


class client ():
    HOST = 'localhost'
    PORT = 5000
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_message(self):
        while True:
            texte = input ("")
            self.socket.send(texte.encode())

    def received_message(self):
        while True :
            data = self.socket.recv(1096)
            print(data.decode())

    def connect_server(self):
        try:
            self.socket.connect((self.HOST, self.PORT))
            thread1 = threading.Thread(target=self.send_message, args=())
            thread2 = threading.Thread(target=self.received_message, args=())
            thread1.start()
            thread2.start()
        except:
            pass
            

