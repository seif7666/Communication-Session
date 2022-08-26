from email import message
import socket as sk

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
        client_sock, client_addr= server_socket.accept()
        print(f"Connected by {client_addr}")
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            print(data)
            message= 'HTTP/1.1 200 OK\r\ncontent-length: 11\r\ncontent-type: text/html\r\n\r\nHello World'
            print(message)
            client_sock.sendall(message.encode('UTF-8'))
            
except:
    server_socket.close()