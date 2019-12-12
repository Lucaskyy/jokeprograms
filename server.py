#!/usr/bin/python3
import urllib.request
import socket
import msvcrt
import sys

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.1.56'
port = 7777 #Port to listen on 

#Binding to socket
serversocket.bind((host, port)) #Host will be replaced/substitued with IP, if changed and not running on host

#Starting TCP listener
serversocket.listen(3)

print("Press 'q' to kill the server.")

while True:
    def connect():
        #Starting the connection 
	    clientsocket,address = serversocket.accept()
        print("Received a connection from %s " % str(address))
        resp = input("""Please choose what you want to do with %s:
        1. Send message
        2. Play game
        3. Disconnect from server
        Your choice: """ % str(address))
    
        if resp == '1':
           message = input("Please enter the message you want to send: ")
           result = message + "\r\n"
           clientsocket.send(result.encode())
           connect()
        elif resp == '2':
           print("Coming soon!")
           connect()
        elif resp == '3':
           r2 = "You have been kicked from the server!" + "\r\n"
           clientsocket.send(r2.encode())
           clientsocket.close()
        elif resp >= '4':
           print("Thats not a valid option!")
           connect()