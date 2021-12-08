import socket 
from colorama import *

init()

print(Fore.BLUE + """  _______                      _   _____  _             _   
 |__   __|                    (_) / ____|| |           | |  
    | |  ___  _ __  _ __ ___   _ | |     | |__    __ _ | |_ 
    | | / _ \| '__|| '_ ` _ \ | || |     | '_ \  / _` || __|
    | ||  __/| |   | | | | | || || |____ | | | || (_| || |_ 
    |_| \___||_|   |_| |_| |_||_| \_____||_| |_| \__,_| \__|
                                     BETA y Gam's - Client                       
                                                            """)

client_socket = socket.socket()
host, port = "127.0.0.1", 8080
client_socket.connect((host, port))

nom = input("Pseudo : ")
print("Bienvenue , ", nom, "\nLe client est connecte au serveur")

if __name__ == "__main__":

	while True:

		message = input(f"{nom} > ")
		client_socket.send(f"{nom} > {message}".encode("utf-8"))
