import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_CONFIG = {
    'token': os.getenv("8021132299:AAG9haTe1lstxdtxXREE6OgSKW42nXT_5pI"),
    'chat_id': '-1002079781875',
    'message_thread_id': 2
}

SBER_CONFIG = {
    'client_id': os.getenv("SBER_CLIENT_ID"),
    'client_secret': os.getenv("SBER_CLIENT_SECRET"),
    'base_url': 'https://iftfintech.testsbi.sberbank.ru:9443 ',
    'auth_url': 'https://efs-sbbol-ift-web.testsbi.sberbank.ru:9443/ic/sso/api/v2/oauth ',
    'scope': 'openid GET_STATEMENT_ACCOUNT GET_STATEMENT_TRANSACTION'
}