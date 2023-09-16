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
        print('\n+' + 96*'-' + '+')
        print(f'+-- Erro ao enviar dados: {str(e)}')
        print('+' + 96*'-' + '+\n')

# Função para verificar se a mensagem está vazia e fechar a conexão se estiver
def check_empty_message(client_socket, data):
    if not data:
        try:
            client_socket.close()
            # Em caso de conexão fechada, imprime uma mensagem de encerramento
            print('\n+' + 96*'-' + '+')
            print(f'+-- Conexão encerrada por: {client_socket}')
            print('+' + 96*'-' + '+\n')
            return True
        
        except Exception as e:
            # Em caso de erro ao fechar a conexão, imprime uma mensagem de erro
            print('\n+' + 96*'-' + '+')
            print(f'+-- Erro ao fechar a conexão: {str(e)}')
            print('+' + 96*'-' + '+\n')
            return False

# Função de mensagem de boas-vindas
def welcome_message():
    print('\n+' + 96*'-' + '+')
    print('+' + 36*'-' + ' Bem-vindo à Rede Órion ' + 36*'-' + '+')
    print('+' + 96*'-' + '+')

# Função de exibição das opções do servidor
def options_message():
    print('\n+' + 96*'-' + '+')
    print('+' + 38*'-' + ' Opções do servidor ' + 38*'-' + '+')
    print('+' + 96*'-' + '+')
    print('+-- 1 - Consultar uma curidosidade')
    print('+' + 96*'-' + '+')
    print('+-- 2 - Horário atual do servidor')
    print('+' + 96*'-' + '+')
    print('+-- 3 - Fazer download de arquivo')
    print('+' + 96*'-' + '+')
    print('+-- 4 - Listar todos os arquivos do servidor')
    print('+' + 96*'-' + '+')
    print('+-- 0 - Sair')
    print('+' + 96*'-' + '+')
    print('+' + 96*'-' + '+')

# Função para criar um novo diretório de download
def create_directory(directory_name):
    base_directory = os.path.join(os.path.dirname(__file__))
    new_directory_path = os.path.join(base_directory, directory_name)
    try:
        os.mkdir(new_directory_path.encode('utf-8'))
        return new_directory_path
    
    except FileExistsError:
        return new_directory_path

# Função para encontrar um diretório de download
def find_directory():
    base_directory = os.path.join(os.path.dirname(__file__))
    try:
        items_base_directory = os.listdir(base_directory)
        for item in items_base_directory:
            item_path = os.path.join(base_directory, item)
            if os.path.isdir(item_path) and item.lower() in ['download', 'downloads']:
                return item_path
            elif os.path.isdir(item_path):
                return item_path
            
        return create_directory('download')

    except FileNotFoundError:
        print('+' + 96*'-' + '+')
        print('+' + 96*'-' + '+')
        print('\n+' + 96*'-' + '+')
        print(f'+-- O diretório "{base_directory}" não foi encontrado')
        print('+' + 96*'-' + '+')
        return

# Função para receber arquivos
def file_receive(client_socket, directory, file_name):        
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
        print('+' + 96*'-' + '+')
        print('+' + 96*'-' + '+')
        print('\n+' + 96*'-' + '+')
        print(f'+-- O arquivo "{file_name}" foi recebido e salvo na pasta "{os.path.basename(directory)}"')
        print('+' + 96*'-' + '+')
        
    except Exception as e:
        # Em caso de erro ao receber arquivo, imprime uma mensagem de erro
        print('+' + 96*'-' + '+')
        print('+' + 96*'-' + '+')
        print('\n+' + 96*'-' + '+')
        print(f'+-- Erro ao receber arquivo: {str(e)}')
        print('+' + 96*'-' + '+')

# Função principal do programa
def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)
        
    except socket.error as e:
        # Em caso de erro de socket, imprime uma mensagem de erro e sai do programa
        print('\n\n+' + 96*'-' + '+')
        print(f'+-- Erro de socket: {str(e)}')
        print('+' + 96*'-' + '+\n')
        sys.exit()
        
    welcome_message()

    try:
        while True:
            options_message()
            choice = input('+-- Informe a opção escolhida: ')
            print('+' + 96*'-' + '+')
            
            if int(choice) in [0, 1, 2, 3, 4]:
            
                send_with_error_handling(client_socket, choice)
                data = client_socket.recv(2048)

                if check_empty_message(client_socket, data):
                    break
                
                if int(choice) == 0:
                    print(data.decode())
                    break
                
                elif int(choice) == 3:
                    directory = find_directory()
                    file_name = input(data.decode())
                    send_with_error_handling(client_socket, file_name)
                    file_receive(client_socket, directory, file_name)

                else:
                    print(data.decode())
                
            else:
                # Em caso de opção inválida, imprime uma mensagem de erro
                print('\n\n+' + 96*'-' + '+')
                print(f'+-- O valor "{choice}" não é uma opção válida')
                print('+' + 96*'-' + '+\n')
                 
    except KeyboardInterrupt:
        # Em caso de interrupção pelo usuário, imprime uma mensagem de encerramento
        print('\n\n+' + 96*'-' + '+')
        print('+' + 35*'-' + ' O programa foi encerrado ' + 35*'-' + '+')
        print('+' + 96*'-' + '+\n')
        
    finally:
        # Fecha o socket antes de sair do programa
        client_socket.close()
    
if __name__ == '__main__':
    main()