# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

@pyrogram.Client.on_message(pyrogram.filters.media)
async def fwdmedia(bot, update):
    bot_id = await bot.get_me()
    await bot.forward_messages(
    chat_id=Config.TRACK_CHANNEL,
    from_chat_id=f"{bot_id}",
    message_ids=update.message_id
)
