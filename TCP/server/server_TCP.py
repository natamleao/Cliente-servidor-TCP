# Importação das bibliotecas necessárias
import socket  # Para comunicação via socket
import threading  # Para suportar múltiplos clientes simultaneamente
from datetime import datetime  # Para obter a hora atual
import os  # Para manipulação de arquivos e diretórios

# Define o endereço do servidor como localhost (127.0.0.1) e a porta 5000
server_address = ('localhost', 5000)

# Função para criar o diretório de Logs
def create_log_directory(base_directory):
    new_directory_path = os.path.join(base_directory, 'logs')  
    try:
        os.mkdir(new_directory_path.encode('utf-8'))
        return new_directory_path
    except FileExistsError:
        return new_directory_path

# Função para registrar uma conexão em um arquivo de log
def log_connection(client_address):
    base_directory = os.path.join(os.path.dirname(__file__))
    logs_directory = os.path.join(base_directory, 'logs')

    if 'logs' in os.listdir(base_directory):
        if 'server_log' in os.listdir(logs_directory):
            file_path = os.path.join(logs_directory, 'server_log')
        else:
            file_path = os.path.join(logs_directory, 'server_log')
    else:
        os.makedirs(logs_directory)
        file_path = os.path.join(logs_directory, 'server_log')
   
    log_message = [
        '\n+' + 96*'-' + '+',
        f'Conexão estabelecida com: {client_address}',
        '+' + 96*'-' + '+'
    ]

    log_message_ = '\n'.join(log_message)
    with open(file_path, 'a') as log_file:
        log_file.write(log_message_)

# Função para enviar dados com tratamento de erro
def send_with_error_handling(client_socket, data):
    try:
        client_socket.sendall(data.encode('utf-8'))
        
    except BrokenPipeError as e:
        # Em caso de erro ao enviar dados, imprime uma mensagem de erro
        print('\n+' + 96*'-' + '+')
        print(f'+-- Erro ao enviar dados: {str(e)}')
        print('+' + 96*'-' + '+\n')

# Função para verificar se a mensagem está vazia e fechar a conexão se estiver
def check_empty_message(client_socket, client_address, data):
    if not data:
        try:
            client_socket.close()
            # Em caso de conexão fechada, imprime uma mensagem de encerramento
            print('\n+' + 96*'-' + '+')
            print(f'+-- Conexão encerrada por: {client_address}')
            print('+' + 96*'-' + '+\n')
            return True
        
        except Exception as e:
            # Em caso de erro ao fechar a conexão, imprime uma mensagem de erro
            print('\n+' + 96*'-' + '+')
            print(f'+-- Erro ao fechar a conexão: {str(e)}')
            print('+' + 96*'-' + '+\n')
            return False

# Função para enviar uma curiosidade sobre teletransportação quântica
def query_curiosity(client_socket):
    curiosity_message = (
        'Você sabia que a teletransportação quântica é um fenômeno no qual o estado' 
        'quântico de uma partícula, como um fóton, pode ser transmitido para uma'
        'localização distante sem que a partícula em si se mova fisicamente. Isso é'
        'possível devido ao emaranhamento quântico, que permite que partículas estejam'
        'correlacionadas de tal maneira que a medição do estado de uma delas'
        'instantaneamente revele o estado da outra, independentemente da distância entre'
        'elas. Esse fenômeno tem aplicações na área de comunicação quântica, onde a'
        'segurança das comunicações é fundamental, e é uma das características mais'
        'intrigantes da física quântica.'
    )
    
    header = '+' + 42*'-' + ' Curiosidade ' + 41*'-' + '+'
    dashed_line = '+' + 96*'-' + '+'
    line_width = len(dashed_line)
    lines = [curiosity_message[i:i+line_width] for i in range(0, len(curiosity_message), line_width)]
    
    distributed_curiosity_message = '\n'.join([dashed_line + '\n'] + [dashed_line] + [header] + [dashed_line] + lines + [dashed_line])
    send_with_error_handling(client_socket, distributed_curiosity_message)

# Função para enviar a hora atual do servidor
def current_time(client_socket):
    try:
        time = datetime.now()
        current_time_message = [
            '+' + 96*'-' + '+',
            '\n+' + 96*'-' + '+',
            '+' + 39*'-' + ' Hora do servidor ' + 39*'-' + '+',
            '+' + 96*'-' + '+',
            f'Hora: {time.strftime("%H:%M:%S")}',
            '+' + 96*'-' + '+'
        ]
        
        current_time_message_ = '\n'.join(current_time_message)
        send_with_error_handling(client_socket, current_time_message_)
        
    except Exception as e:
        error_message = [
            '+' + 96*'-' + '+',
            '\n+' + 96*'-' + '+',
            f'Erro ao obeter a hora do servidor: {str(e)}',
            '+' + 96*'-' + '+\n'
        ]
        
        error_message_ = '\n'.join(error_message)
        send_with_error_handling(client_socket, error_message_)

# Função para enviar um arquivo ao cliente
def research_file(client_socket, file_name):
    directory = os.path.join(os.path.dirname(__file__), 'files')
    try:
        if file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            file_size = os.path.getsize(file_path)
            client_socket.send(str(file_size).encode())
            with open(file_path, 'rb') as file:
                for file_part in file.readlines():
                    client_socket.send(file_part)
        else:
            error_message = [
                '+' + 96*'-' + '+',
                '\n+' + 96*'-' + '+',
                f'O arquivo "{file_name}" não foi encontrado no banco de dados do servidor',
                '+' + 96*'-' + '+\n'
            ]
            
            error_message_ = '\n'.join(error_message)
            send_with_error_handling(client_socket, error_message_)
            
    except Exception as e:
        error_message = [
            '+' + 96*'-' + '+',
            '\n+' + 96*'-' + '+',
            f'Erro ao enviar o arquivo: {str(e)}',
            '+' + 96*'-' + '+\n'
        ]
        
        error_message_ = '\n'.join(error_message)
        send_with_error_handling(client_socket, error_message_)

# Função para listar os arquivos no servidor
def files_list(client_socket):
    directory = os.path.join(os.path.dirname(__file__), 'files')
    try:
        files = os.listdir(directory)
        saved_files_message = [
            '+' + 96*'-' + '+',
            '\n+' + 96*'-' + '+',
            '+' + 37*'-' + ' Arquivos no servidor ' + 37*'-' + '+',
            '+' + 96*'-' + '+',
        ]
        
        for file in files:
            saved_files_message.append('+-- ' + file)
            saved_files_message.append('+' + 96*'-' + '+')

        saved_files_message_ = '\n'.join(saved_files_message)
        send_with_error_handling(client_socket, saved_files_message_)
        
    except Exception as e:
        error_message = [
            '+' + 96*'-' + '+',
            '\n+' + 96*'-' + '+',
            f'Erro ao obter os arquivos no servidor: {str(e)}',
            '+' + 96*'-' + '+\n'
        ]
        error_message_ = '\n'.join(error_message)
        send_with_error_handling(client_socket, error_message_)

# Função para solicitar o nome do arquivo ao cliente
def request_file_name(client_socket, client_address):
    request_message = [
        '+' + 96*'-' + '+',
        '\n+' + 96*'-' + '+',
        'Informe o nome do arquivo: '
    ]
    
    request_message_ = '\n'.join(request_message)
    send_with_error_handling(client_socket, request_message_)
    
    file_name = client_socket.recv(1024).decode().strip()
    
    if not check_empty_message(client_socket, client_address, file_name):
        research_file(client_socket, file_name)

# Função para encerrar a conexão com o cliente
def exit(client_socket, client_address):
    print('\n+' + 96*'-' + '+')
    print(f'+-- Fechando a conexão com: {client_address}')
    print('+' + 96*'-' + '+\n')
    
    goodbye_message = [
        '+' + 96*'-' + '+',
        '\n+' + 96*'-' + '+',
        f'Adeus {client_address}',
        '+' + 96*'-' + '+'
    ]
    
    goodbye_message_ = '\n'.join(goodbye_message)
    send_with_error_handling(client_socket, goodbye_message_)
    client_socket.close()

# Função para lidar com um cliente
def handle_client(client_socket, client_address):
    log_connection(client_address)
    
    print('+' + 96*'-' + '+')
    print(f'+-- Conectado em: {client_address}')
    print('+' + 96*'-' + '+')
    
    while True:
        data = client_socket.recv(1024)   
        if check_empty_message(client_socket, client_address, data):
            break
        
        choice = data.decode().strip()
        try:
            choice = int(choice)
            
        except ValueError:
            error_message = [
                '+' + 96*'-' + '+',
                '\n+' + 96*'-' + '+',
                'O valor digitado é inválido',
                '+' + 96*'-' + '+\n'
            ]
            
            error_message_ = '\n'.join(error_message)
            send_with_error_handling(client_socket, error_message_)

        match choice:
            case 0:
                exit(client_socket, client_address)
                break
            case 1:
                query_curiosity(client_socket)
            case 2:
                current_time(client_socket)
            case 3:
                request_file_name(client_socket, client_address)
            case 4:
                files_list(client_socket)
                
# Função principal do servidor
def main():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(server_address)
    servidor_socket.listen()
    
    print('\n+' + 96*'-' + '+')
    print('+' + 37*'-' + ' Servidor em execução ' + 37*'-' + '+')
    print('+' + 96*'-' + '+\n')    

    while True:
        client_socket, client_address = servidor_socket.accept()                    
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
        
if __name__ == '__main__':
    main()