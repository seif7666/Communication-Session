import socket as sk
import threading

closeThreads=False
numberOfConnections= 0

def manageClient(clientSocket:sk.socket, addr):
    global numberOfConnections
    while not closeThreads:
        data = clientSocket.recv(1024)
        if not data:
            break
        data=data.decode()
        print(f'[{addr[0]}:{addr[1]}]:{data}')
        message= f'I received from you this message : \"{data}\"'
        clientSocket.sendall(message.encode('UTF-8'))
    print(f'Closing Connection to client: {addr[0]}:{addr[1]}')
    clientSocket.close()
    numberOfConnections-=1

connectionThreads= []
server_port= 100

server_socket= sk.socket(sk.AF_INET, sk.SOCK_STREAM)
hostname=sk.gethostname()   
server_ip=sk.gethostbyname(hostname) 
while True:
    try:
        server_socket.bind(('',server_port))
        break
    except:
        server_port+=1
server_socket.listen(5)
print(f'Listening on IP: {server_ip} and Port: {server_port}...')
try:
    while True:
        print(f'Number of connections= {numberOfConnections}')
        client_sock, client_addr= server_socket.accept()
        print(f"Connected to {client_addr}")
        thread= threading.Thread(target=manageClient, args=(client_sock,client_addr,))
        numberOfConnections+=1
        thread.start()
        connectionThreads.append(thread)
except:
    server_socket.close()
    closeThreads= True