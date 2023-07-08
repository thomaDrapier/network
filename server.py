import socket
import threading
import database

class Server():
    HOST = ''
    PORT = 5000
    address = (HOST,PORT)

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.database = database.Database()
        
    def listen_connexion(self):
        self.socket.bind(self.address)
        while True:
            self.socket.listen()
            conn, address = self.socket.accept() # Connexion d'un client au serveur mais pas encore connecté à la base de données
            print(f"{address} vient de se connecter")
            
            # Nouveau thread pour ajouter ou on le client à la base de données
            thread = threading.Thread(target=self.select_username, args=(conn,address)) 
            thread.start()
        

    def listen_data_socket(self, conn, address):
        a = True
        while a :
            try:
                data = conn.recv(1024)
            # En cas de perte de la connexion avec le remote client, on arrête d'écouter la socket
            # et on ferme la connexion.
            except ConnectionResetError:
                print(f"connexion perdue avec address{address}")
                self.database.delete_user(address[1]) # Numéro de port car en local 
                a = False
                conn.close()

    def select_username(self, conn, address):
    # Lors d'une connexion par le client, cette fonction demande au client de renseigner un nom d'utilsiateur
        text = "Choisissez un nom d'tilisateur pour être connecté au chat"
        conn.send(text.encode())
        name = conn.recv(1024).decode()

    # Et en fonction de la disponibilté du nom, ajoute ou non le cient dans la base de données.
        if self.database.check_username(name): # Disponible
            self.database.insert_user(name, address[0], address[1])
            conn.send("Vous êtes connecté à la base de données".encode())

            thread = threading.Thread(target=self.listen_data_socket, args=(conn,address,))
            thread.start() # On lance l'écoute permanente pour cette connexion cliente sur un autre thread

        else: # Indisponible 
            conn.send("Ce nom n'est pas disponible".encode())
            self.select_username(conn, address)

                



serveur = Server()
serveur.listen_connexion()

