
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', "")
    APP_ID = os.environ.get('APP_ID', "")
    API_HASH = os.environ.get('API_HASH', "")

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','').split('5968806660,')]
    print(BOT_TOKEN, APP_ID, API_HASH, ALLOWED_USERS)
    DOWNLOAD_DIR = 'downloads'
