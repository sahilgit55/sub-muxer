
# (c) mohdsabahat

#Logging
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

import os
import pyrogram
from chat import Chat
from config import Config
logging.getLogger('pyrogram').setLevel(logging.WARNING)
Auth_Chat = int(Config.Auth_Chat)


@pyrogram.Client.on_message(pyrogram.filters.command(['help']))
async def help_user(bot, update):

    if update.chat.id==Auth_Chat:
        await bot.send_message(
            update.chat.id,
            Chat.HELP_TEXT,
            disable_web_page_preview = True,
            reply_to_message_id = update.id
        )

    else:

        await bot.send_message(
            update.chat.id,
            Chat.NO_AUTH_USER,
            reply_to_message_id = update.id
        )

@pyrogram.Client.on_message(pyrogram.filters.command(['start']))
async def start(bot, update):
    print(update.from_user.id)

    if update.chat.id!=Auth_Chat:
        return await bot.send_message(
            update.chat.id,
            Chat.NO_AUTH_USER,
            reply_to_message_id = update.id
        )

    await bot.send_message(
        chat_id = update.chat.id,
        text = Chat.START_TEXT,
        reply_to_message_id = update.id
    )
