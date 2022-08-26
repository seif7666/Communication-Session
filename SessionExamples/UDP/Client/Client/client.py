import socket as sk
import os


SERVER_IP = input('Enter server IP address: ')
SERVER_PORT = int(input('Enter Server port: '))
sock= sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

number=0
while True:
    data= [0,0]
    data[0]= number// 256
    data[1]= number % 256
    print(f'Sent {number}')
    number+=1
    number= number%(2*256)
    address= (SERVER_IP,SERVER_PORT)
    sock.sendto(bytearray(data), address)

    