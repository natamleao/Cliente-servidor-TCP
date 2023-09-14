# Importação das bibliotecas necessárias
import socket  # Para comunicação via socket
import sys     # Para manipulação de erros e saída do programa
import os      # Para manipulação de arquivos e diretórios

# Define o endereço do servidor como localhost (127.0.0.1) e a porta 5000
server_address = ('127.0.0.1', 5000)

# Função para enviar dados com tratamento de erro
def send_with_error_handling(client_socket, data):
    try:
        client_socket.sendall(data.encode('utf-8'))
    except OSError as e:
        # Em caso de erro ao enviar dados, imprime uma mensagem de erro
        print('\n+' + 81*'-' + '+')
        print(f'+-- Erro ao enviar dados: {str(e)}')
        print('+' + 81*'-' + '+\n')

# Função para verificar se a mensagem está vazia e fechar a conexão se estiver
def check_empty_message(client_socket, data):
    if not data:
        try:
            client_socket.close()
            # Em caso de conexão fechada, imprime uma mensagem de encerramento
            print('+' + 81*'-' + '+')
            print('+' + 81*'-' + '+')
            print('\n+' + 81*'-' + '+')
            print(f'+-- Conexão encerrada por: {client_socket}')
            print('+' + 81*'-' + '+\n')
            return True
        except Exception as e:
            # Em caso de erro ao fechar a conexão, imprime uma mensagem de erro
            print('+' + 81*'-' + '+')
            print('+' + 81*'-' + '+')
            print('\n+' + 81*'-' + '+')
            print(f'+-- Erro ao fechar a conexão: {str(e)}')
            print('+' + 81*'-' + '+\n')
            return False

# Função de mensagem de boas-vindas
def welcome_message():
    print('\n+' + 81*'-' + '+')
    print('+' + 30*'-' + ' Bem-vindo ao Órion ' + 31*'-' + '+')
    print('+' + 81*'-' + '+')

# Função de exibição das opções do servidor
def options_message():
    print('\n+' + 81*'-' + '+')
    print('+' + 31*'-' + ' Opções do servidor ' + 30*'-' + '+')
    print('+' + 81*'-' + '+')
    print('+-- 1 - Consulta')
    print('+' + 81*'-' + '+')
    print('+-- 2 - Hora')
    print('+' + 81*'-' + '+')
    print('+-- 3 - Arquivo')
    print('+' + 81*'-' + '+')
    print('+-- 4 - Listar')
    print('+' + 81*'-' + '+')
    print('+-- 0 - Sair')
    print('+' + 81*'-' + '+')
    print('+' + 81*'-' + '+')

# Função para receber arquivos
def file_receive(client_socket, file_name):    
    directory = os.path.join(os.path.dirname(__file__), 'file')
    file_path = os.path.join(directory, file_name)
    
    try:
        file_size_str = client_socket.recv(1024).decode()
        file_size = int(file_size_str)
        
        with open(file_path, 'wb') as file:
            bytes_received = 0
            while bytes_received < file_size:
                file_part = client_socket.recv(1000000)
                if not file_part:
                    break
                file.write(file_part)
                bytes_received += len(file_part)
        
        # Imprime uma mensagem quando o arquivo é recebido com sucesso
        print('+' + 81*'-' + '+')
        print('+' + 81*'-' + '+')
        print('\n+' + 81*'-' + '+')
        print(f'+-- O arquivo "{file_name}" foi recebido e salvo na pasta "file"')
        print('+' + 81*'-' + '+')
        
    except FileNotFoundError:
        # Em caso de arquivo não encontrado, imprime uma mensagem de erro
        print('+' + 81*'-' + '+')
        print('+' + 81*'-' + '+')
        print('\n+' + 81*'-' + '+')
        print(f'+-- O diretório "file" não existe. Crie-o antes de receber arquivos.')
        print('+' + 81*'-' + '+')
        
    except Exception as e:
        # Em caso de erro ao receber arquivo, imprime uma mensagem de erro
        print('+' + 81*'-' + '+')
        print('+' + 81*'-' + '+')
        print('\n+' + 81*'-' + '+')
        print(f'+-- Erro ao receber arquivo: {str(e)}')
        print('+' + 81*'-' + '+')

# Função principal do programa
def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)
        
    except socket.error as e:
        # Em caso de erro de socket, imprime uma mensagem de erro e sai do programa
        print('\n\n+' + 81*'-' + '+')
        print(f'+-- Erro de socket: {str(e)}')
        print('+' + 81*'-' + '+\n')
        sys.exit()
        
    welcome_message()

    try:
        while True:
            options_message()
            choice = input('+-- Informe a opção escolhida: ')
            print('+' + 81*'-' + '+')
            
            if int(choice) in [0, 1, 2, 3, 4]:
            
                send_with_error_handling(client_socket, choice)
                data = client_socket.recv(2048)

                if check_empty_message(client_socket, data):
                    break
                
                if int(choice) == 0:
                    print(data.decode())
                    break
                
                elif int(choice) == 3:
                    file_name = input(data.decode())
                    send_with_error_handling(client_socket, file_name)
                    file_receive(client_socket, file_name)

                else:
                    print(data.decode())
                
            else:
                # Em caso de opção inválida, imprime uma mensagem de erro
                print('\n\n+' + 81*'-' + '+')
                print(f'+-- O valor "{choice}" não é uma opção válida')
                print('+' + 81*'-' + '+\n')
                 
    except KeyboardInterrupt:
        # Em caso de interrupção pelo usuário, imprime uma mensagem de encerramento
        print('\n\n+' + 81*'-' + '+')
        print('+-- O programa foi encerrado')
        print('+' + 81*'-' + '+\n')
        
    finally:
        # Fecha o socket antes de sair do programa
        client_socket.close()
    
if __name__ == '__main__':
    main()