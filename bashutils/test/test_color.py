# -*- coding: utf-8 -*-

from bashutils import colors


def test():
    print "COLORS LIST :"
    for color in colors.COLOR_CODE_TEXT:
        print colors.color_text("My Text", color), color

    print ""
    print "------------------------------"
    print "BACKGROUND COLORS LIST :"
    for bcolor in colors.COLOR_CODE_BG:
        print colors.color_text("My Text", bcolor=bcolor), bcolor

    print ""
    print "------------------------------"
    print "EFFECTS :"
    for effect in colors.COLOR_EFFET:
        print colors.color_text("My Text", effect=effect), effect

    print ""
    print "------------------------------"
    print "ALL :"
    for color in colors.COLOR_CODE_TEXT:
        for bcolor in colors.COLOR_CODE_BG:
            for effect in colors.COLOR_EFFET:
                print colors.color_text("My Text", color, bcolor, effect), color.ljust(10), bcolor.ljust(10), effect


if __name__ == "__main__":
    test()
