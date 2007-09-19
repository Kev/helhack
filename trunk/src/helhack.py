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

import sys
import traceback
from core.CursesController import CursesController
import logging

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print "Usage: "
        print "   ./helhack.py "
        print ""
        print "Nothing to see here, move along."
        exit()
    logging.basicConfig(level=logging.DEBUG,
                           	format='%(asctime)s %(levelname)s %(message)s',
		                    filename='./helhack.log',
		                    filemode='w')
    #Main game launch goes here
    #It's bad form to use a general try loop, but this one is to prevent the screen
    # getting corrupted
    game = 0
    try:
        logging.info("Starting game")
        game = CursesController()
        logging.info("Starting turns")
        carryOn = True
        while carryOn:
            logging.debug("Taking game turn")
            carryOn = game.turn()
        logging.info("Ending turns\n")
        del game
    except:
        del game
        traceback.print_exc()
    logging.info("Exiting")
