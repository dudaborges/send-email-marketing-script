import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import logging


load_dotenv() 

logging.basicConfig(level=logging.INFO)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


def send_email(sender_email: str, password: str, recipients: list[str], 
    subject: str, body_email: str) -> None:
    """
    Envia um e-mail utilizando SMTP.

    :param sender_email: E-mail do remetente
    :param password: Senha do e-mail do remetente
    :param recipients: Lista de e-mails dos destinatários
    :param subject: Titulo do e-mail
    :param body_email: Corpo do e-mail
    """
    try:
        msg = MIMEText(body_email, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipients)

        server_email = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server_email.starttls()
        server_email.login(sender_email, password) 
        server_email.sendmail(sender_email, recipients, msg.as_string())
        logging.info('E-mail enviado com sucesso!')

    except Exception as e:
        logging.error(f'Erro ao enviar o e-mail: {e}')

    finally:
        server_email.quit()
