import socket
import threading
from datetime import datetime
import os

HOST = 'localhost'
PORT = 5000

def send_with_error_handling(conn, data):
    try:
        conn.send(data.encode())
    except BrokenPipeError:
        print('\n+' + 81*'-' + '+')
        print('+-- Erro ao enviar dados: a conexão foi fechada pelo cliente')
        print('+' + 81*'-' + '+\n')
        
def check_empty_message(conn, addr, data):
    if not data:
        print('\n+' + 81*'-' + '+')
        print(f'+-- Conexão encerrada por: {addr}')
        print('+' + 81*'-' + '+\n')
        conn.close()
        return True
    return False

def send_welcome_message(conn):
    welcome_message = [
        '\n+' + 81*'-' + '+',
        '+' + 30*'-' + ' Bem-vindo ao Órion ' + 31*'-' + '+',
        '+' + 81*'-' + '+'
    ]
    
    welcome_message_ = '\n'.join(welcome_message)
    send_with_error_handling(conn, welcome_message_)
    
def send_options_message(conn):
    options_message = [
        '\n+' + 81*'-' + '+',
        '+' + 31*'-' + ' Opções do servidor ' + 30*'-' + '+',
        '+' + 81*'-' + '+',
        '+-- 1 - Consulta',
        '+' + 81*'-' + '+',
        '+-- 2 - Hora',
        '+' + 81*'-' + '+', 
        '+-- 3 - Arquivo',
        '+' + 81*'-' + '+',
        '+-- 4 - Listar',
        '+' + 81*'-' + '+',
        '+-- 0 - Sair',
        '+' + 81*'-' + '+',
        '+' + 81*'-' + '+',
    ]

    options_message_ = '\n'.join(options_message)
    send_with_error_handling(conn, options_message_)

def query(conn):
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
    
    header = '+' + 34*'-' + ' Curiosidade ' + 34*'-' + '+'
    dashed_line = '+' + 81*'-' + '+'
    line_width = len(dashed_line)
    lines = [curiosity_message[i:i+line_width] for i in range(0, len(curiosity_message), line_width)]
    
    distributed_curiosity_message = '\n'.join([dashed_line + '\n'] + [dashed_line] + [header] + [dashed_line] + lines + [dashed_line])
    send_with_error_handling(conn, distributed_curiosity_message)

def hour(conn):
    try:
        time = datetime.now()
        current_time_message = [
            '+' + 81*'-' + '+',
            '\n+' + 81*'-' + '+',
            '+' + 31*'-' + ' Hora do servidor ' + 32*'-' + '+',
            '+' + 81*'-' + '+',
            f'Hora: {time.strftime("%H:%M:%S")}',
            '+' + 81*'-' + '+'
        ]
        
        current_time_message_ = '\n'.join(current_time_message)
        send_with_error_handling(conn, current_time_message_)
        
    except Exception as e:
        error_message = [
            '+' + 81*'-' + '+',
            '\n+' + 81*'-' + '+',
            f'Erro ao obeter a hora do servidor: {str(e)}',
            '+' + 81*'-' + '+\n'
        ]
        
        error_message_ = '\n'.join(error_message)
        send_with_error_handling(conn, error_message_)
    
def file(conn, file_name):
    directory = os.path.join(os.path.dirname(__file__), 'file')
    try:
        if file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'rb') as file:
                data = file.read()
                send_with_error_handling(conn, data)
        else:
            error_message = [
                '+' + 81*'-' + '+',
                '\n+' + 81*'-' + '+',
                f'O arquivo "{file_name}" não foi encontrado no banco de dados do servidor',
                '+' + 81*'-' + '+\n'
            ]
            
            error_message_ = '\n'.join(error_message)
            send_with_error_handling(conn, error_message_)
    except Exception as e:
        error_message = [
            '+' + 81*'-' + '+',
            '\n+' + 81*'-' + '+',
            f'Erro ao enviar o arquivo: {str(e)}',
            '+' + 81*'-' + '+\n'
        ]
        
        error_message_ = '\n'.join(error_message)
        send_with_error_handling(conn, error_message_)
        
def list(conn):
    directory = os.path.join(os.path.dirname(__file__), 'file')
    try:
        files = os.listdir(directory)
        saved_files_message = [
            '+' + 81*'-' + '+',
            '\n+' + 81*'-' + '+',
            '+' + 29*'-' + ' Arquivos no servidor ' + 30*'-' + '+',
            '+' + 81*'-' + '+',
        ]
        
        for file in files:
            saved_files_message.append('+-- ' + file)
        #    if file != files[-1]:
            saved_files_message.append('+' + 81*'-' + '+')
        #saved_files_message.append('+' + 81*'-' + '+\n')

        saved_files_message_ = '\n'.join(saved_files_message)
        send_with_error_handling(conn, saved_files_message_)
    except Exception as e:
        error_message = [
            '+' + 81*'-' + '+',
            '\n+' + 81*'-' + '+',
            f'Erro ao obter os arquivos no servidor: {str(e)}',
            '+' + 81*'-' + '+\n'
        ]
        error_message_ = '\n'.join(error_message)
        send_with_error_handling(conn, error_message_)
    
def request_file_name(conn, addr):
    request_message = [
        '+' + 81*'-' + '+',
        '\n+' + 81*'-' + '+',
        'Informe o nome do arquivo: '
    ]
    
    request_message_ = '\n'.join(request_message)
    send_with_error_handling(conn, request_message_)
    
    data = conn.recv(4096)
    
    if not check_empty_message(conn, addr, data):
        file(conn, data.decode().strip().lower())
    
def exit(conn, addr):
    print('\n+' + 81*'-' + '+')
    print(f'+-- Fechando a conexão com: {addr}')
    print('+' + 81*'-' + '+\n')
    
    goodbye_message = [
        '+' + 81*'-' + '+',
        '\n+' + 81*'-' + '+',
        f'Adeus {addr}',
        '+' + 81*'-' + '+'
    ]
    
    goodbye_message_ = '\n'.join(goodbye_message)
    send_with_error_handling(conn, goodbye_message_)
    conn.close()

def handle_client(conn, addr):
    print('+' + 81*'-' + '+')
    print(f'+-- Conectado em: {addr}')
    print('+' + 81*'-' + '+')
    
    send_welcome_message(conn)
    
    while True:
        send_options_message(conn)
        data = conn.recv(4096)   
        if check_empty_message(conn, addr, data):
            break
        
        choice = data.decode().strip()
        try:
            choice = int(choice)
        except ValueError:
            error_message = [
                '+' + 81*'-' + '+',
                '\n+' + 81*'-' + '+',
                'O valor digitado é inválido',
                '+' + 81*'-' + '+\n'
            ]
            
            error_message_ = '\n'.join(error_message)
            send_with_error_handling(conn, error_message_)
        
        match choice:
            case 0:
                exit(conn, addr)
                break
            case 1:
                query(conn)
            case 2:
                hour(conn)
            case 3:
                request_file_name(conn, addr)
            case 4:
                list(conn)

def main():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((HOST, PORT))
    servidor_socket.listen()
    
    print('\n+' + 81*'-' + '+')
    print('+' + 29*'-' + ' Servidor em execução ' + 30*'-' + '+')
    print('+' + 81*'-' + '+\n')    

    while True:
        conn, addr = servidor_socket.accept()                    
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
        
if __name__ == '__main__':
    main()