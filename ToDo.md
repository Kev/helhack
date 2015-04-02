# Technical stuff #

  * Python
  * curses library
  * network support

# First release #

  * Randomized dungeon with monsters to fight and items to pick up and equip
  * Saves current state to a file whenever the user quits
  * Stores character in high scores upon death

# (Code) Classes #

  * Dungeon: Stores levels in a list
  * Level: Stores rooms in a list
  * Room: Stores lists of tiles in a list so it can be accessed using
  * the index operator like tiles[row](row.md)[column](column.md). Has a print method.
  * Tile: Stores color, ASCII character, passable, has a print method.

# Future releases #

  * Town/overworld with NPCs
  * Quests
  * Plot
  * Dungeon editor
  * Dungeon master mode

