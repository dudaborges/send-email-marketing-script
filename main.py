import os
from email_sender import send_email
from firestore import connect_to_firestore, fetch_collection_data


sender_email = 'escritoriostaragency@gmail.com'
password = os.getenv('EMAIL_PASSWORD')

recipients = []
subject = 'Email teste'
body_email = 'Olá, este é um e-mail de teste.'

credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

db = connect_to_firestore(credentials_path)
if db:
    emails = fetch_collection_data(db, 'client')
    for email in emails:
        recipients.append(email)


send_email(sender_email, password, recipients, subject, body_email)