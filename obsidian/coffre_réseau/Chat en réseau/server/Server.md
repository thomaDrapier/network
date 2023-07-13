[[Ecoute demande connexions]]
[[Ecoute transmission données]]


Le serveur a pour missions de gérer les demandes de connexions entrantes qu'il reçoit, pour cela il doit être en écoute permanente.
Il reçoit également tout les messages des utilisateurs, il doit ensuite les envoyer aux bons destinataires.

Pour cela dans mon script python j'ai eu recours à du multithreading grâce au module ```threading```. 
Le multithreading est une fonctionnalité du langage Python qui nous permet d'exécuter un programme en parallèle dans le même processus.

Le thread principal correspond à la fonction d'écoute des connexions entrantes. Dès qu'une connexion est acceptée une nouvelle socket est créée, c'est la connexion qui servira à transmettre les données entre ce client et le serveur. Et cette socket doit être écouté en permanence également afin de détecter à tout moment des données reçues par le serveur (envoyées par le client). 
Pour on va créer un nouveau thread qui écoute cette socket, le nombre de threads total est égal à ```nombre de clients + 1 (écoute du serveur)```.
