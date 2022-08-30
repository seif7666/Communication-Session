import socket as sk
serverIP= input("Enter Server IP address: ")
serverPort= int(input("Enter Server Port: "))
clientSocket= sk.socket(sk.AF_INET, sk.SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))
while True:
    data= input("Enter Data or 0 to exit: ")
    if data =='0':
        break
    clientSocket.sendall(data.encode())
    receivedData=clientSocket.recv(1024)
    print(f"Data received from server is \"{receivedData.decode()}\"")
clientSocket.close()