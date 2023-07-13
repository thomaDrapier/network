import socket
import threading
import database
import pickle

class Server():
    HOST = ''
    PORT = 5000
    address = (HOST,PORT)
    user_connections = dict()

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.database = database.Database()
        
    def listen_connexion(self):
        self.socket.bind(self.address)
        while True:
            self.socket.listen()
            conn, address = self.socket.accept() 
            print(f"{address} vient de se connecter")
            thread = threading.Thread(target=self.verify_username, args=(conn, address, self.socket)) 
            thread.start()
    
    def verify_username(self, conn, address, socket):
        data_received = pickle.loads(conn.recv(1096))
        user_name = data_received['text']
        if self.database.check_username(user_name): # Disponible
            self.database.insert_user(user_name, address[0], address[1])
            self.user_connections[f"{user_name}"] = conn # Ajout dans le dico de l'utilisateur associé à sa socket
            conn.send("connected".encode())
            thread = threading.Thread(target=self.listen_data_socket, args=(conn, address, socket))
            thread.start()
        else :
            conn.send("error")
            

    
    def listen_data_socket(self, conn, address, socket):
        a = True
        while a :
            try:
                data = conn.recv(1096)
                self.server_process(data, socket)

            except ConnectionResetError:
                print(f"connexion perdue avec address{address}")
                self.database.delete_user(address[1]) 
                a = False
                conn.close()
    
    def server_process(self, data, socket):
        data = pickle.loads(data)
        code = data["code"]
        print(code)
        if code == 0:
            self.message_to_server(data, socket)
        else :
            self.message_to_users(data)
    
    def message_to_server(self, data, socket):
        pass

    def message_to_users(self, data):
        text, dest = data["message"], data["destinataire"]
        print(dest)
        coordonate_dest = self.database.searching(dest)
        print(coordonate_dest)
        data_sent= pickle.dumps({"destinataire": dest, "message": text, "code": 99})
        self.user_connections[f"{dest}"].send(data_sent)

        


serveur = Server()
serveur.listen_connexion()

