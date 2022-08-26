import socket as sk
import os


SERVER_IP = input('Enter server IP address: ')
SERVER_PORT = int(input('Enter Server port: '))

sock = sk.socket(sk.AF_INET,  sk.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

duration = 1  # seconds

print('Server listening...')
while True:
    data, addr = sock.recvfrom(1024) 
    print(data[0]*256+data[1])
    # number= min(800,data[0]*256+data[1])
    # print(number)
    # os.system('play -nq -t alsa synth {} sine {}'.format(duration, number))


    