import os
from email_sender import send_email


sender_email = 'escritoriostaragency@gmail.com'
password = os.getenv('EMAIL_PASSWORD')

recipients = ['duda.pborges92@gmail.com']
subject = 'Email teste'
body_email = 'Olá, este é um e-mail de teste.'

send_email(sender_email, password, recipients, subject, body_email)