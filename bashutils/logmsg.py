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

MESSAGE = ""

MESSAGE_LOG = {
    -1: ["none", ("????",)],
    0: ["OK", (" OK ", "green",)],
    1: ["FAIL", ("FAIL", "red",)],
    2: ["WARNING", ("WARN", "yellow",)],
    3: ["ERROR", ("ERR-", "red",)],
}

for elem in MESSAGE_LOG.keys():
    locals()["LOG_" + MESSAGE_LOG[elem][0].replace(" ", "_").upper()] = elem


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


def log_msg_pre(message):
    """
    Prefix the previous begin log message
    """
    global MESSAGE
    MESSAGE = message + MESSAGE
    

def log_msg_post(message):
    """
    Suffix the previous begin log message
    """
    global MESSAGE
    MESSAGE = MESSAGE + message


def log_end_msg_pre(message, log):
    """
    Prefix the previous begin log message
    and end it with the log status
    """
    log_msg_pre(message)
    log_end_message(log)


def log_end_msg_post(message, log):
    """
    Suffix the previous begin log message
    and end it with the log status
    """
    log_msg_post(message)
    log_end_message(log)


if __name__ == "__main__":
    log_begin_message("ersgfsdgfdxhb f hgfdh fg")
    log_end_msg_post("POST", LOG_NONE)
