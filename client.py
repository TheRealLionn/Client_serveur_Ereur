import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 4445))
print("connexionn etalie avec succés")
for i in range (5):
    message = input("Saisir un message: ")
    client.sendall(message.encode('utf-8'))

    reponse = client.recv(1024).decode('utf-8')
    print(f"Réponse reçue du serveur: {reponse}")
client.close()
