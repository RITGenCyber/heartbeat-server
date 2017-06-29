import socket
import sys
import threading
import random

def getVal(a, b):
	return random.randint(a, b)

def ready():
	file = open("vals.txt")
	line = file.readline()
	split = line.split(" ")
	return int(split[0]), int(split[1]), int(split[2]), int(split[3])

def sockThread(clientsock):
	miny, lowy, highy, maxy = ready()
	highy = str(getVal(highy, maxy))
	lowy = str(getVal(miny, lowy))
	clientsock.send(highy)
	clientsock.send(lowy)
	clientsock.close()
	
def mainSock(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((ip, port))
	sock.listen(40)
	while True:
		clientsock, clientaddr = sock.accept()
		threading.Thread(target=sockThread, args=(clientsock,)).start()		

def readconfig():
	file = open("config.txt")
	line = file.readline()
	split = line.split(" ")
	return split[0], int(split[1])

def main():
	ip, port = readconfig()
	mainSock(ip, port)	

main()
