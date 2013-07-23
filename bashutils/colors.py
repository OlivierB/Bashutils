# -*- coding: utf-8 -*-

"""
Bash colors

Create a formated text with bash colors

Text and background colors available:
none, black, red, green, yellow, blue, magenta, cyan, white

Text effects:
none, bold, underscore, blink, reverse, concealed

see : http://www.csc.uvic.ca/~sae/seng265/fall04/tips/s265s047-tips/bash-using-colors.html

@author: Olivier BLIN
"""


import sys


COLOR_ON = True
COLOR_RESET = "\033[0m"
COLOR_CODE_TEXT = {
    "none": 39,
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
}
COLOR_CODE_BG = {
    "none": 49,
    "black": 40,
    "red": 41,
    "green": 42,
    "yellow": 43,
    "blue": 44,
    "magenta": 45,
    "cyan": 46,
    "white": 47,
}
COLOR_EFFET = {
    "none": 0,
    "bold": 1,
    "underscore": 4,
    "blink": 5,
    "reverse": 7,
    "concealed": 9,
}


def set_color_on(on):
    """
    Enable or disable bash color
    """
    global COLOR_ON
    if on:
        COLOR_ON = True
    else:
        COLOR_ON = False


def color_text(text, color="none", bcolor="none", effect="none"):
    """
    Return a formated text with bash color
    """
    istty = False
    try:
        istty = sys.stdout.isatty()
    except:
        pass
    if not istty or not COLOR_ON:
        return text
    else:
        if not effect in COLOR_EFFET.keys():
            effect = "none"
        if not color in COLOR_CODE_TEXT.keys():
            color = "none"
        if not bcolor in COLOR_CODE_BG.keys():
            bcolor = "none"

        v_effect = COLOR_EFFET[effect]
        v_color = COLOR_CODE_TEXT[color]
        v_bcolor = COLOR_CODE_BG[bcolor]

        if effect == "none" and color == "none" and bcolor == "none":
            return text
        else:
            return "\033[%d;%d;%dm" % (v_effect, v_color, v_bcolor) + text + COLOR_RESET


def color_parser(text):
    """
    Removes markers and replaces them by colored text
    """
    return text
