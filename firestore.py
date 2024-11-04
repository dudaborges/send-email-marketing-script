from google.cloud import firestore
from dotenv import load_dotenv
import logging
import re

load_dotenv()
logging.basicConfig(level=logging.INFO)


def connect_to_firestore(credentials_path: str) -> None:
    """
    Inicia conexão com o Firestore.

    :param credentials_path: Caminho do arquivo da chave privada do banco
    """
    try:
        if not credentials_path:
            raise EnvironmentError('O caminho da chave privada não está configurada.')

        db = firestore.Client()
       
        logging.info('Conexão com o Firestore estabelecida com sucesso.')
        return db
    
    except EnvironmentError as e:
        logging.error(f'Erro de ambiente: {e}')

    except Exception as e:
        logging.error(f'Erro ao conectar ao Firestore: {e}')


def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def fetch_collection_data(db: str, collection_name: str) -> list:
    try:
        if not db:
            raise ConnectionError("Cliente Firestore não inicializado.")

        collection_ref = db.collection(collection_name)
        
        docs = collection_ref.stream()

        emails = set()
        for doc in docs:
            document_name = 'dataClient'
            data_document = doc.to_dict().get(document_name)
            email = data_document.get('email')

            if email and is_valid_email(email):
                emails.add(email)
        
        if emails:
            logging.info('Dados recuperados com sucesso')
            return list(emails)
        else:
            logging.info('Nenhum dado encontrado na coleção.')

    except ConnectionError as e:
        logging.error(f'Erro de conexão: {e}')

    except firestore.exceptions.NotFound:
        logging.error(f'A coleção {collection_name} não foi encontrada no Firestore')

    except Exception as e:
        logging.error(f'Erro ao recuperar dados da coleção {collection_name}: {e}')

    return []
