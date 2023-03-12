#
# Copyright (C) 2023 Giovanni Gualtieri (Giovix92)
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from telegramma.api import Module, assert_min_api_version

assert_min_api_version(1)

from telegram import BotCommand
from telegram.ext import CommandHandler

from telegramma.modules.sepol.main import (
	sepol,
)

class SepolModule(Module):
	NAME = "sepol"
	VERSION = "1.4.1"
	HANDLERS = [
		CommandHandler(["sepol"], sepol),
	]
	COMMANDS = [
		BotCommand("sepol", "Get a denial fix on-the-go."),
	]

module = SepolModule()
