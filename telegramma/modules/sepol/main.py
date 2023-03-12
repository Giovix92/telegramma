#
# Copyright (C) 2022 Sebastiano Barezzi
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from telegram import Chat, Message, Update, User
from telegram.ext import CallbackContext
from telegram.constants import ParseMode
from telegram.helpers import escape_markdown
import re

def gen_fix(string):
    try:
        test = re.search("{", string)
        test2 = re.search("}", string)
        se_context = string[test.span()[0]:test2.span()[0] + 1]
        test = re.search("scontext", string)
        scontext = string[(test.span()[0]):].split(":")[2]
        test = re.search("tcontext", string)
        tcontext = string[(test.span()[0]):].split(":")[2]
        test = re.search("tclass", string)
        tclass = string[(test.span()[0]):].split("=")[1].split(" ")[0]
        if scontext == tcontext:
            tcontext = "self"
        fix = f"allow {scontext} {tcontext}:{tclass} {se_context};\n"
        if tclass == "binder" and "call" in se_context or "transfer" in se_context:
            fix = f"binder_call({scontext}, {tcontext})\n"
        if "prop" in tcontext:
            if "read" in se_context or "getattr" in se_context or "ioctl" in se_context or "lock" in se_context or "open" in se_context:
                fix = f"get_prop({scontext}, {tcontext})\n"
            if "write" in se_context or "set" in se_context or "append" in se_context:
                fix = f"set_prop({scontext}, {tcontext})\n"
        return fix
    except Exception as e:
         return "Invalid denial"

async def sepol(update: Update, context: CallbackContext):
    try:
        command = update.message.text.split(' ', 1)[1]
        text = gen_fix(command).strip("\n")
        
        response = f"Fix: {escape_markdown(text, 2)}"

        await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN_V2)
    except Exception as e:
        await update.message.reply_text(f"Usage: /sepol <denial>")