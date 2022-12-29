
# (c) mohdsabahat

import logging
logging.basicConfig(level = logging.DEBUG,
                     format="%(asctime)s - %(name)s - %(message)s - %(levelname)s")

logger = logging.getLogger(__name__)

import os

if os.path.exists('testconfig.py'):
    from testconfig import Config
else:
    from config import Config

from helper_func.dbhelper import Database as Db
db = Db().setup()

Session_String = Config.Session_String

import pyrogram
logging.getLogger('pyrogram').setLevel(logging.WARNING)


if __name__ == '__main__':

    if not os.path.isdir(Config.DOWNLOAD_DIR):
        os.mkdir(Config.DOWNLOAD_DIR)

    plugins = dict(root='plugins')
    if Session_String:
        app = pyrogram.Client(
        session_string = Session_String,
        api_id = Config.APP_ID,
        api_hash = Config.API_HASH,
        plugins = plugins
    )
    else:
        app = pyrogram.Client(
            'Subtitle Muxer',
            bot_token = Config.BOT_TOKEN,
            api_id = Config.APP_ID,
            api_hash = Config.API_HASH,
            plugins = plugins
        )
    app.run()
