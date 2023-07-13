import socket
import threading
import pickle


class Client ():
    HOST = 'localhost'
    PORT = 5000

    messages = {
        'serveur': 
        '''
            Bonjour vous avez solicité de l'aide, voici les options :  
            2. Liste des utilisateurs actif
            3. Quitter le serveur
        ''',
        'user_name': "Veuillez choisir votre nom d'utilisateur : \n"
        }
    
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_server(self):
        try:
            self.socket.connect((self.HOST, self.PORT))
            if self.send_user_name(self.socket):
                thread1 = threading.Thread(target=self.send_message, args=(self.socket,))
                thread2 = threading.Thread(target=self.received_message, args=(self.socket,))
                thread1.start()
                thread2.start()
            else :
                self.connect_server()
        except:
            pass
            
    def send_user_name(self, socket):
        name = input("Choissisez un nom d'utilisateur:\n")
        data = {"destinataire": "serveur", "text": f"{name}", "code":0}
        data = pickle.dumps(data)
        socket.send(data)
        received_data = socket.recv(1096).decode()
        if received_data == "connected":
            print("Vous êtes maintenant connecté")
            return True
        else :
            return False

    
    def send_message(self, socket):
        while True:
            texte = input("votre message :\n")
            destinataire = input("A qui voulez l'envoyer ?\n")
            if destinataire == "serveur":
                code = 0
            else:
                code = 99
            data = pickle.dumps({'destinataire': f"{destinataire}", 'message': f'{texte}', 'code': f'{code}' })
            socket.send(data)

    def received_message(self, socket):
        while True :
            data = pickle.loads(socket.recv(1096))
            print(f"{data['message']}")

client = Client()
client.connect_server()


