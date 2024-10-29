import socket

def client_program():
    host=socket.gethostname()
    port=8080
    client_socket=socket.socket()
    client_socket.connect((host,port))
    username=input("Username: ")
    message=input(">>>")
    while message.lower().strip()!="quit":
        message=username+": "+message
        client_socket.send(message.encode())
        data=client_socket.recv(1024).decode()

        print('Recieved from server: '+data)
        mesage=input(">>>")
    client_socket.close()

client_program()