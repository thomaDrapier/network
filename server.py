import socket
import threading
import os

HOST = ''
PORT = 5000
address = (HOST,PORT)
members = []
threads = []

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(address)


def listen_data_socket(conn, address):
    while True :
        try:
            data = conn.recv(1024)
            print(data)
            pass
        except ConnectionResetError:
            print("connexion perdue")
            client = members.index(address[1])
            threads[client].stop()


def listen_connexion():
    while True:
        socket.listen()
        conn, address = socket.accept()
        print(f"{address} vient de se connecter")
        members.append(address[1])
        thread = threading.Thread(target=listen_data_socket, args=(conn,address,))
        thread.start()
        threads.append(thread)

thread = threading.Thread(target=listen_connexion, args=())

listen_connexion()

