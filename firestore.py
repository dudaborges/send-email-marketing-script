from google.cloud import firestore
from dotenv import load_dotenv
import logging
import os


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


def fetch_collection_data(db: str, collection_name: str) -> None:
    try:
        if not db:
            raise ConnectionError("Cliente Firestore não inicializado.")

        collection_ref = db.collection(collection_name)
        
        docs = collection_ref.stream()

        results = []
        for doc in docs:
            results.append({doc.id: doc.to_dict()})
        
        if results:
            logging.info('Dados recuperados com sucesso:')
            for result in results:
                print(result)
        else:
            print("Nenhum dado encontrado na coleção.")

    except ConnectionError as e:
        logging.error(f'Erro de conexão: {e}')

    except firestore.exceptions.NotFound:
        logging.error(f'A coleção {collection_name} não foi encontrada no Firestore')

    except Exception as e:
        logging.error(f'Erro ao recuperar dados da coleção {collection_name}: {e}')


credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

db = connect_to_firestore(credentials_path)
if db:
    fetch_collection_data(db, 'client')
