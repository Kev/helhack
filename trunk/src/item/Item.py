# Item.py - Base class for all objects ingame, including scenery, 
#           potions, whatever.
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

class Item:
	""" Base class for all ingame objects, including creatures and scenery
	"""
	
	def blocking(self):
		""" Does this item prevent movement on a map?
		"""
	
	def carryable(self):
		""" Can this item be carried in a backpack?
		"""

	def glyph(self):	
		""" The character used to render this in curses.
		"""
		return "@"
	
	def colour(self):
		""" The colour used to render this tile in curses.
		"""
		