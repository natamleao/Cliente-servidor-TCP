# Servidor de Comunicação Multifuncional

![Language](https://img.shields.io/badge/language-Python-blue)
![Protocol](https://img.shields.io/badge/protocol-TCP-green)
![Architecture](https://img.shields.io/badge/architecture-client--server-orange)
![Networking](https://img.shields.io/badge/networking-sockets-lightgrey)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Sobre o projeto

> [!NOTE]
> Este projeto implementa um **servidor de comunicação multifuncional em Python**, capaz de atender múltiplos clientes simultaneamente utilizando **sockets TCP**.

O sistema permite que clientes se conectem ao servidor e utilizem diferentes funcionalidades, incluindo:

- consulta de curiosidades sobre física quântica  
- obtenção da hora atual do servidor  
- envio de arquivos  
- listagem de arquivos disponíveis  

O foco do projeto está na exploração de **comunicação cliente-servidor**, tratamento de conexões e organização de funcionalidades em um único serviço.

---

> [!IMPORTANT]
> ## Tecnologias utilizadas
>
> * **Python**
> * **Sockets TCP**
> * Arquitetura **cliente-servidor**

---

## Conceitos aplicados

Este projeto trabalha conceitos fundamentais de redes e sistemas distribuídos:

- comunicação via sockets (`socket`)  
- modelo cliente-servidor  
- manipulação de conexões simultâneas  
- envio e recebimento de dados pela rede  
- tratamento de exceções em comunicação  
- organização de protocolos simples de interação  

---

## Funcionalidades

### Curiosidades sobre física quântica

O cliente pode solicitar informações ao servidor, que responde com curiosidades sobre tópicos como:

- emaranhamento quântico  
- teletransporte quântico  

---

### Hora do servidor

O servidor retorna a hora atual no formato:

```

HH:MM:SS

```

---

### Envio de arquivos

O cliente pode requisitar arquivos disponíveis no servidor.

O sistema:

- verifica se o arquivo existe  
- realiza o envio via socket  
- trata erros de forma segura  

---

### Listagem de arquivos

O cliente pode solicitar a lista de arquivos disponíveis no servidor.

O servidor responde com os arquivos presentes no diretório configurado.

---

## Funcionamento

O sistema é dividido em dois componentes principais:

- **Servidor** → responsável por gerenciar conexões e responder requisições  
- **Cliente** → responsável por enviar comandos e receber respostas  

A comunicação ocorre via **TCP**, garantindo entrega confiável dos dados.

---

## Estrutura do projeto

```

Client-Server/
│
├── server/        # Implementação do servidor
├── client/        # Implementação do cliente
│
├── files/         # Diretório de arquivos disponíveis para envio
│
├── README.md      # Documentação
└── LICENSE        # Licença 

````

---

## Instalação

Clone o repositório:

```bash
git clone git@github.com:natamleao/Client-Server.git
cd Client-Server
````

---

## Execução

### Iniciar o servidor

```bash
python ./server/server_TCP.py
```

---

### Iniciar o cliente

Em outro terminal:

```bash
python ./client/client_TCP.py
```

---

## Como usar

Após iniciar o cliente:

* conectar ao servidor
* escolher a funcionalidade desejada
* interagir via terminal

---

## Observações

> [!IMPORTANT]
> Este projeto é uma implementação simplificada com foco em aprendizado de comunicação em rede e organização de serviços.

> [!WARNING]
> Não inclui:
>
> * autenticação
> * criptografia
> * controle avançado de concorrência

---

> [!WARNING]
> ## Licença
> 
> Este projeto está licenciado sob a **MIT License**.

---

## Autor

**Natam Leão Ferreira**

Conclusão: **2023**

---
