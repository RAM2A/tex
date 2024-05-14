import re, os, time
import datetime

class Config:
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "6700540841:AAEzEG75XEQXqfTGmIvy136zVclAUBxQKOI")
    API_HASH = os.environ.get('API_HASH', "beb7e4b83ada668fa85f9a9b56338f1d")
    API_ID = int(os.environ.get('API_ID', "24665357"))
    OWNER_ID = int(os.environ.get('OWNER_ID', "1717511106")) #Admin UserId
    DB_URI = os.environ.get('DB_URI') #May Be In Future.
    
