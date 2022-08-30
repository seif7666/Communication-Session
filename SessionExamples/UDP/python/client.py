import socket as sk
import os

SERVER_IP = input('Enter server IP address: ')
SERVER_PORT = int(input('Enter Server port: '))
sock= sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

while True:
    number= int(input('Enter Frequency: '))
    data= [0,0]
    data[0]= number// 256
    data[1]= number % 256
    address= (SERVER_IP,SERVER_PORT)
    sock.sendto(bytearray(data), address)

    