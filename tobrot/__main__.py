#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52

import io
import logging
import os
import sys
import traceback

from pyrogram import Client, filters
from pyrogram.handlers import CallbackQueryHandler, MessageHandler

from tobrot import (
    API_HASH,
    APP_ID,
    AUTH_CHANNEL,
    CANCEL_COMMAND_G,
    CLEAR_THUMBNAIL,
    CLONE_COMMAND_G,
    DOWNLOAD_LOCATION,
    GET_SIZE_G,
    GLEECH_COMMAND,
    GLEECH_UNZIP_COMMAND,
    GLEECH_ZIP_COMMAND,
    LEECH_COMMAND,
    LEECH_UNZIP_COMMAND,
    LEECH_ZIP_COMMAND,
    LOG_COMMAND,
    LOGGER,
    PYTDL_COMMAND,
    RENEWME_COMMAND,
    SAVE_THUMBNAIL,
    STATUS_COMMAND,
    TELEGRAM_LEECH_UNZIP_COMMAND,
    TELEGRAM_LEECH_COMMAND,
    TG_BOT_TOKEN,
    UPLOAD_COMMAND,
    YTDL_COMMAND,
    GYTDL_COMMAND,
    GPYTDL_COMMAND,
)
from tobrot.helper_funcs.download import down_load_media_f
from tobrot.plugins.call_back_button_handler import button

# the logging things
from tobrot.plugins.choose_rclone_config import rclone_command_f
from tobrot.plugins.custom_thumbnail import clear_thumb_nail, save_thumb_nail
from tobrot.plugins.incoming_message_fn import (
    g_clonee,
    g_yt_playlist,
    incoming_message_f,
    incoming_purge_message_f,
    incoming_youtube_dl_f,
    rename_tg_file,
)
from tobrot.plugins.new_join_fn import help_message_f, new_join_f
from tobrot.plugins.rclone_size import check_size_g, g_clearme
from tobrot.plugins.status_message_fn import (
    cancel_message_f,
    eval_message_f,
    exec_message_f,
    status_message_f,
    upload_document_f,
    upload_log_file,
)

#if __name__ == "__main__":
    # create download directory, if not exist
#if not os.path.isdir(DOWNLOAD_LOCATION):
#os.makedirs(DOWNLOAD_LOCATION)
    #
app = Client(
   "LeechBot",
   bot_token=TG_BOT_TOKEN,
   api_id=APP_ID,
   api_hash=API_HASH,
   workers=343,
)
app.add_handler(
    MessageHandler(
        incoming_message_f,
        filters=filters.command(
            [
                LEECH_COMMAND,
                LEECH_UNZIP_COMMAND,
                LEECH_ZIP_COMMAND,
                GLEECH_COMMAND,
                GLEECH_UNZIP_COMMAND,
                GLEECH_ZIP_COMMAND,
            ]
        )
        & filters.chat(chats=AUTH_CHANNEL),
    )
)    
#
app.add_handler(
    MessageHandler(
        down_load_media_f,
        filters=filters.command(
            [
                TELEGRAM_LEECH_COMMAND,
                TELEGRAM_LEECH_UNZIP_COMMAND,

            ]
        )
        & filters.chat(chats=AUTH_CHANNEL),
    )
)    
                             
    #
app.add_handler(
    MessageHandler(
        incoming_purge_message_f,
        filters=filters.command(
            ["purge"]
        )
        & filters.chat(chats=AUTH_CHANNEL),
    )
)    
    #
app.add_handler(
    MessageHandler(
        g_clearme,
        filters=filters.command(
            [f"{RENEWME_COMMAND}"]
        )
        & filters.chat(chats=AUTH_CHANNEL),
    )
)    
    #

    #

app.add_handler(
    MessageHandler(
        status_message_f,
        filters=filters.command(
            [f"{STATUS_COMMAND}"]
        )
        & filters.chat(chats=AUTH_CHANNEL),
    )
)    

    #
    
    #
app.add_handler(
    MessageHandler(
        cancel_message_f,
        filters=filters.command(
            [f"{CANCEL_COMMAND_G}"]
        )
        & filters.chat(chats=AUTH_CHANNEL),
    )
)    


    #

    #
if __name__ == "__main__":
    app.run()
