#  ModLibrary, a Minecraft mod manager.
#  Copyright (C) 2023 iamliuzy
#
#  This file is part of ModLibrary.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#   any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see https://www.gnu.org/licenses/.

import datetime
from os import linesep

logfile = open("latest.log", mode="w", encoding="utf-8")
debug_logfile = open("latest_debug.log", mode="w", encoding="utf-8")


class LogLevel(object):
    debug = "DEBUG"
    info = "INFO"
    warn = "WARN"
    error = "ERROR"
    critical = "CRITICAL"


def log(s: str, level=LogLevel.info):
    time = datetime.datetime.today().strftime("%c")
    result_debug = ""
    result = ""
    result_debug = result_debug + "[" + time + "]" + "(" + level + ")"
    result_debug = result_debug + " " + s
    if not level == LogLevel.debug:
        result = result + "[" + time + "]" + "(" + level + ")"
        result = result + " " + s
    logfile.write(result + linesep)
    debug_logfile.write(result_debug + linesep)


def debug(s: str):
    log(s, LogLevel.debug)


def info(s: str):
    log(s, LogLevel.info)


def warn(s: str):
    log(s, LogLevel.warn)


def error(s: str):
    log(s, LogLevel.error)


def critical(s: str):
    log(s, LogLevel.critical)
