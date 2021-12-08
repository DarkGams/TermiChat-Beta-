import socket
import select
from colorama import *

serv = socket.socket()
host, port = "127.0.0.1", 8080
serv.bind((host, port))
serv.listen(4)
ClientCo = True
socket_objs = [serv]

init()

print(Fore.BLUE + """  _______                      _   _____  _             _   
 |__   __|                    (_) / ____|| |           | |  
    | |  ___  _ __  _ __ ___   _ | |     | |__    __ _ | |_ 
    | | / _ \| '__|| '_ ` _ \ | || |     | '_ \  / _` || __|
    | ||  __/| |   | | | | | || || |____ | | | || (_| || |_ 
    |_| \___||_|   |_| |_| |_||_| \_____||_| |_| \__,_| \__|
                                    BETA by Gam's - Serveur               
                                                            """)

print(Fore.GREEN + "Bienvenue dans TermiChat !\nLe serveur est connecté , vous pouvez y connecter des clients")

while ClientCo:
	liste_lu, liste_acce_Ecrit, exeption = select.select(socket_objs, [], socket_objs)
	for socket_obj in liste_lu:
		if socket_obj is serv:
			client, adresse = serv.accept()
			print(f"Client socket : {adresse}")
			socket_objs.append(client)

		else:
			data_r = socket_obj.recv(128).decode("utf-8")
			if data_r:
				print(data_r)
			else:
				socket_objs.remove(socket_obj)
				print(Fore.RED + "1 personne s'est déconnectée")
				print(f"{len(socket_objs) - 1} personnes restantes")
