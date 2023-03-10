import datetime
from os import linesep

import constants

logfile = open("latest.log", mode="w", encoding="utf-8")
debug_logfile = open("latest_debug.log", mode="w", encoding="utf-8")


class LogLevel:
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
