import socket
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('localhost', 4445))
serveur.listen(1)
print("Démarrage du serveur...")
print("Serveur dermarrer :-)")

while True:
    try:
        client, adresse = serveur.accept()
        print(f"Client connecté depuis {adresse}")
        for i in range (5):
            message = client.recv(1024).decode('utf-8')
            print(f"Message reçu: {message}")
            reponse = input("Saisir une réponse: ")
            client.sendall(reponse.encode('utf-8'))

    except ConnectionResetError:
        print("Déconnexion inattendue du client")
        client.close()

    except Exception as e:
        print(f"Erreur: {e}")
        client.close()

    finally:
        print("Toujours en ligne")