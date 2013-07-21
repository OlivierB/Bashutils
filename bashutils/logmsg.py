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
    -1: ["NONE", ("????",)],
    0: ["OK", (" OK ", "green",)],
    1: ["FAIL", ("FAIL", "red",)],
    2: ["ERROR", ("ERR-", "red",)],
}


class LOG():

    """All logs Type"""
    pass


for elem in MESSAGE_LOG.keys():
    setattr(LOG, MESSAGE_LOG[elem][0], elem)


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


def log_error_msg(message):
    """
    print error message
    """
    log_begin_message(message)
    log_end_message(3)


def log_msg_type(message, log):
    log_begin_message(message)
    log_end_message(log)


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


def add_log_type(name, display, color, bcolor):
    """
    name : call name (A-Z and '_')
    display : display message in [-]
    color : text color (see bashutils.colors)
    bcolor : background color (see bashutils.colors)
    """
    global MESSAGE_LOG
    v_name = name.replace(" ", "_").upper()
    val = 0
    lkey = MESSAGE_LOG.keys()
    while val in lkey:
        val += 1

    MESSAGE_LOG[val] = [v_name, (display, color, bcolor,)]
    setattr(LOG, v_name, val)
