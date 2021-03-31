# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup

from helper_funcs.chat_base import TRChatBase

@pyrogram.Client.on_message(pyrogram.filters.regex(pattern=".*xnxx.*"))
async def xnxx(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/xnxx")
    await bot.send_message(
        chat_id=update.chat.id,
        text="No Porn!",
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
