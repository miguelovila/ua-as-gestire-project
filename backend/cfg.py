import os

SERVER_PATH  = os.path.abspath(os.path.dirname(__file__))
STORAGE_PATH = os.path.normpath(os.path.join(SERVER_PATH, './database'))
DB_PATH = os.path.normpath(os.path.join(STORAGE_PATH, './database.db'))
LOCKER_SECRET = 'farto_da_papelada_de_analise_de_sistemas'
