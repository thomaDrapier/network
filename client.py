import socket
import threading

HOST = 'localhost'
PORT = 5000
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_message():
    while True:
        texte = input ("")
        socket.send(texte.encode())

def received_message():
    while True :
        data = socket.recv(1096)
        print(data.decode())

try:
    socket.connect((HOST, PORT))
    print("Vous êtes connectés au serveur")
    thread1 = threading.Thread(target=send_message, args=())
    thread2 = threading.Thread(target=received_message, args=())
    thread1.start()
    thread2.start()
except:
    pass
    

