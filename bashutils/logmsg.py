#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bash color
Bash log

Print and log message like lsb init-functions

@author: Olivier BLIN
"""


import sys
import colors

# --------------------------------
# Bash logger
MESSAGE = ""

MESSAGE_LOG = {
    -1: ["FFF", ("????",)],
    0: ["OK", (" OK ", "green",)],
    1: ["FAIL", ("FAIL", "red",)],
    2: ["WARNING", ("/!!\\", "yellow",)],
    3: ["ERROR", ("ERROR", "red",)],
}

for elem in MESSAGE_LOG.keys():
    locals()["LOG_" + MESSAGE_LOG[elem][0].replace(" ", "_")] = elem


def log_success_msg(message):
    """
    print success message
    """
    log_begin_message(message)
    log_end_message(0)


def log_failure_msg(message):
    """
    print failure message
    """
    log_begin_message(message)
    log_end_message(1)


def log_warning_msg(message):
    """
    print warning message
    """
    log_begin_message(message)
    log_end_message(2)


def log_error_msg(message):
    """
    print error message
    """
    log_begin_message(message)
    log_end_message(3)


def log_begin_message(message):
    """
    Create and print a new log message
    waiting for an end log message
    """
    global MESSAGE
    MESSAGE = message
    sys.stdout.write("[....] ")
    sys.stdout.write(message)
    sys.stdout.flush()


def log_end_message(log):
    """
    End a log message with a status
    defined by log
    """
    if not log in MESSAGE_LOG.keys():
        log = -1

    res = colors.color_text(*MESSAGE_LOG[log][1])

    sys.stdout.write("\r[" + res + "] " + MESSAGE + "\n")


def log_end_msg_pre(message, log):
    """
    Prefix the previous begin log message
    and end it with the log status
    """
    global MESSAGE
    MESSAGE = message + MESSAGE
    log_end_message(log)


def log_end_msg_post(message, log):
    """
    Suffix the previous begin log message
    and end it with the log status
    """
    global MESSAGE
    MESSAGE = MESSAGE + message
    log_end_message(log)
