#!/usr/bin/env python3
import os
import socket
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

# get token path
scriptpath = os.path.realpath(__file__)
scriptdir, _ = os.path.split(scriptpath)
tokenpath = scriptdir + "/token"

# check if token file exists
if not os.path.exists(tokenpath):
    print("Please add file 'token' with Telegram API token.")
    exit()

# read token file
with open(tokenpath, "r") as f:
    token = f.readline().strip()

# create updater object
updater = Updater(token, use_context=True)

# start function
def start(update: Update, context: CallbackContext):
    update.message.reply_text("This bot is used to get the local IP of a running machine.")

# help function
def help(update: Update, context: CallbackContext):
    update.message.reply_text("\ip: get IP of machine")

# ip function
def ip(update: Update, context: CallbackContext):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname+".local")
    update.message.reply_text(ip_address)

# unknown command
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

# add dispacher handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('ip', ip))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# start listening
updater.start_polling()
