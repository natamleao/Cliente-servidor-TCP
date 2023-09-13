import socket

HOST = '127.0.0.1'
PORT = 5000

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    welcome_message = client_socket.recv(4096)
    print(welcome_message.decode())

    try:
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            print(data.decode())

            choice = input("Informe a opção: ")
            client_socket.send(choice.encode())
            
            if int(choice) == 0:
                response = client_socket.recv(4096)
                print(response.decode())
                break
            else:
                response = client_socket.recv(4096)
                print(response.decode())
    except KeyboardInterrupt:
        print('\n\n+' + 81*'-' + '+')
        print('+-- O programa foi encerrado')
        print('+' + 81*'-' + '+\n')
    finally:
        client_socket.close()

if __name__ == '__main__':
    main()