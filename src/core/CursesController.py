# CursesController.py - Main class for a curses game.
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

import curses
import logging
from dungeon import Dungeon 

class CursesController:
	def __init__(self):
		""" Set up the terminal.
		"""
		self.screen = curses.initscr()
		curses.noecho()
		curses.cbreak()
		#FIXME we need to check for colour first
		curses.start_color()
		self.screen.clear()
		self.row = 0
		self.column = 0
		self.screen.refresh()
		logging.debug("Rarr, controller created")
	
	def __del__(self):
		""" Clear up the terminal before dying.
		"""
		curses.nocbreak()
		curses.echo()
		curses.endwin()
		logging.debug("Arr, fate be a harsh mistress; controller down.")
	
	def render(self):
		logging.debug("Painting")
		
	def turn(self):
		""" Take one turn of the game.
		"""
		logging.debug("Taking a turn")
		
		self.render()
		return False