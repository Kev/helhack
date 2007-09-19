# Level.py - A single level of the dungeon.
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

import numpy

import item.Wall

class Level:
	""" Represents a single level of the dungeon.
	"""
	
	def __init__(self, tiles):
		self.tiles = tiles
	
	def buildRandom():
		tiles = numpy.zeros((5,5))
		for i in range(0,5):
			tiles[0,i] = Wall()
			tiles[4,i] = Wall()
			tiles[i,0] = Wall()
			tiles[i,4] = Wall()
	    return Level(tiles)