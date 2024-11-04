# Projeto de Envio de E-mails Marketing 📧

> Este projeto em Python foi desenvolvido para o envio de e-mails de marketing de forma automatizada, utilizando a biblioteca `smtplib` para comunicação via SMTP, além de integração com um banco de dados Firebase para gerenciar a lista de destinatários. 

## Linguagem
<table>
  <tr>
    <td>Python</td>
  </tr>
  <tr>
    <td>3.12.7</td>
  </tr>
</table>

## Pré-requisitos

1. **Instalar dependências**:
   - Baixe as dependências listadas no arquivo `requirements.txt`:
     
     ```bash
     pip install -r requirements.txt
     ```

2. **Configurar Firebase**:
   - Adicione a chave do banco Firebase para permitir o carregamento dos dados dos destinatários.

3. **Defina a senha do e-mail a ser utlizado**:
   - Crie um arquivo `.env` no diretório do projeto com a seguinte variável de ambiente:
     
     ```
     EMAIL_PASSWORD=<sua_senha_de_e-mail>
     ```

## Como Executar

No terminal, execute o código principal para enviar o e-mail de marketing:
   
   ```
   python main.py
  ```
