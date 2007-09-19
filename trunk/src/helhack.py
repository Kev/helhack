#!/usr/bin/env python
# helhack.py - Program entry point (__main__).
# Copyright Kevin Smith 2007.
#
# This file is part of HelHack.
#
# HelHack is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, traceback
from core.CursesController import CursesController


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print "Usage: "
        print "   ./helhack.py "
        print ""
        print "Nothing to see here, move along."
        exit()
    #Main game launch goes here
    #It's bad form to use a general try loop, but this one is to prevent the screen
    # getting corrupted
    try:
        debugFile = open("helhack.log", "w")
        debugFile.writelines("Starting game\n")
        game = CursesController()
        debugFile.writelines("Starting turns\n")
        carryOn = True
        while carryOn:
            debugFile.writelines("Taking game turn\n")
            carryOn = game.turn()
        debugFile.writelines("Ending turns\n")
        del game
    except:
        del game
        traceback.print_exc()
    debugFile.close()
