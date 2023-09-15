<div align="justify">
  <h1>Trabalho de Redes: Servidor de Comunicação Multifuncional</h1>
</div>


<div style="margin-left: 20px;">
Este projeto é um exemplo de servidor de comunicação multifuncional desenvolvido como parte de um trabalho acadêmico na disciplina de Redes de Computadores. O servidor é capaz de lidar com múltiplos clientes simultaneamente e oferece várias funcionalidades, incluindo consulta de curiosidades sobre física quântica, obtenção da hora atual do servidor, envio de arquivos e listagem de arquivos no servidor.
</div>
  
<div align="justify">
  
## Funcionalidades Principais

### 1. Curiosidades sobre Física Quântica
Os clientes podem solicitar curiosidades sobre física quântica ao servidor. O servidor responde com informações fascinantes sobre tópicos relacionados à física quântica, como teletransportação quântica e emaranhamento quântico.

### 2. Hora do Servidor
Os clientes podem solicitar a hora atual do servidor. O servidor responde com a hora atual no formato HH:MM:SS.

### 3. Envio de Arquivos
Os clientes podem solicitar o envio de arquivos específicos do servidor. O servidor verifica a existência do arquivo solicitado e, se encontrado, envia o arquivo para o cliente.

### 4. Listagem de Arquivos no Servidor
Os clientes podem solicitar uma lista de arquivos disponíveis no servidor. O servidor responde com a lista de arquivos no diretório de arquivos do servidor.

## Funcionamento Geral
O servidor é implementado em Python e utiliza soquetes (sockets) para estabelecer conexões com os clientes. O código é estruturado de forma a lidar com exceções e erros de comunicação de maneira robusta, garantindo uma experiência confiável aos clientes.

## Como Usar
1. Clone este repositório em sua máquina local.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Execute o servidor com o comando `python ./server/server_TCP.py`. O servidor estará em execução e aguardando conexões de clientes.
4. Execute o cliente com o comando `python ./client/client_TCP.py` e estabeleça uma conexão com o servidor.
5. Utilize as opções do cliente para interagir com o servidor, como solicitar curiosidades, obter a hora atual, enviar ou listar arquivos no servidor.

Este projeto é uma demonstração de um servidor de comunicação versátil que pode ser usado como base para aplicações mais complexas de rede. Ele também serve como uma oportunidade de aprendizado para entender os conceitos de comunicação cliente-servidor em redes de computadores.

* **Autores:** Eliziane, Lara e Natam
* **Instituição:** Universidade Federal do Ceará (UFC) - Campus Russas
* **Disciplina:** Redes de Computadores
* **Data de Conclusão:** 18/09/2023
</div>
