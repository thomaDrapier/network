```python
def listen_connexion():

    while True:
        socket.listen()
	        conn, address = socket.accept() # Connexion d'un client au serveur mais pas encore connecté à la base de données
        print(f"{address} vient de se connecter")
        
        # Nouveau thread pour ajouter ou on le client à la base de données
        thread = threading.Thread(target=select_username, args=(conn,address))
        thread.start()
```