## Ajouter un utilisateur dans la base de données

Dès lors qu'une socket de transmission de données est créée, il faut ajouter le client dans la base de données des utilisateurs actifs, les données ajoutées seront :
		- Son nom d'utilisateur (qui lui a été demandé)
		- Son adresse IP (celle associé à la socket côté client)
		- Le port (celui associé à la socket côté client)

On va donc créer la fonction ```insert_user``` qui sera appelée pour ajouter le client à la base.

```python
def insert_user(user_name, ip, port):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    a = '''
        INSERT INTO active_users(user_name, ip, port)            
        VALUES(?,?,?)
        '''
    cursor.execute(a, (user_name, ip, port))
    conn.commit()
    conn.close()
```

## Supprimer un utilisateur

Lorsque que le programme server détecte la fin d'une connexion, il faut enlever l'utilisateur qui s'est déconnecté de la base des utilisateurs actifs. Cela empêchera les autres utilisateurs d'envoyer un message à quelqu'un qui n'est pas connecté

C'est la fonction ```delete_user``` qui sera appelée pour effectuer cette tâche, elle prend en argument uniquement l'adresse IP.

```python
def delete_user(ip):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    a = '''DELETE FROM active_users
            WHERE ip = ?'''
    cursor.execute(a, (ip,))
    conn.commit()
    conn.close()
```
