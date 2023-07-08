import socket
import threading
import database

HOST = ''
PORT = 5000
address = (HOST,PORT)


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(address)

def server_process(data):
    pass


def listen_data_socket(conn, address):
    a = True
    while a :
        try:
            data = conn.recv(1024)
            server_process(data)
        # En cas de perte de la connexion avec le remote client, on arrête d'écouter la socket
        # et on ferme la connexion.
        except ConnectionResetError:
            print(f"connexion perdue avec address{address}")
            database.delete_user(address[0])
            a = False
            conn.close()

def select_username(conn, address):
# Lors d'une connexion par le client, cette fonction demande au client de renseigner un nom d'utilsiateur
    text = "Choisissez un nom d'tilisateur pour être connecté au chat"
    conn.send(text.encode())
    name = conn.recv(1024).decode()

# Et en fonction de la disponibilté du nom, ajoute ou non le cient dans la base de données.
    if database.check_username(name): # Disponible
        database.insert_user(name, address[0], address[1])
        conn.send("Vous êtes connecté à la base de données".encode())

        thread = threading.Thread(target=listen_data_socket, args=(conn,address,))
        thread.start() # On lance l'écoute permanente pour cette connexion cliente sur un autre thread

    else: # Indisponible 
        conn.send("Ce nom n'est pas disponible".encode())
        select_username(conn, address)

            
def listen_connexion():
    while True:
        socket.listen()
        conn, address = socket.accept() # Connexion d'un client au serveur mais pas encore connecté à la base de données
        print(f"{address} vient de se connecter")
        
        # Nouveau thread pour ajouter ou on le client à la base de données
        thread = threading.Thread(target=select_username, args=(conn,address)) 
        thread.start()
        


listen_connexion()
