import socket
import threading

HOST = ''
PORT = 5000
address = (HOST,PORT)
members = []


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(address)


def listen_data_socket(conn, address):
    a = True
    while a :
        try:
            data = conn.recv(1024)
            print(data)
            pass
        except ConnectionResetError:
            print(f"connexion perdue avec address{address}")
            a = False
            
def listen_connexion():
    while True:
        socket.listen()
        conn, address = socket.accept()
        print(f"{address} vient de se connecter")
        members.append(address[1])
        thread = threading.Thread(target=listen_data_socket, args=(conn,address,))
        thread.start()


listen_connexion()
