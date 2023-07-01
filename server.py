import socket
import threading
import os

HOST = ''
PORT = 5000
address = (HOST,PORT)
members = []
conns = []

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(address)

def server_process(data, address):
    if address[1] == members[0]:
        print(type(data))
        conns[1].send(data)
        print("les données ont été envoyées")
    else :
        print(data)
        conns[0].send(data)
        print("les données ont été envoyées")


def listen_data_socket(conn, address):
    while True :
        data = conn.recv(1024)
        print("Des données ont été reçues")
        print(data)
        server_process(data, address)
        

def listen_connexion():
    while True:
        socket.listen()
        conn, address = socket.accept()
        print(f"{address} vient de se connecter")
        members.append(address[1])
        conns.append(conn)
        thread = threading.Thread(target=listen_data_socket, args=(conn,address,))
        thread.start()

thread = threading.Thread(target=listen_connexion, args=())

listen_connexion()

        
        
