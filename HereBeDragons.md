# Introduction #

Lest it be said that all I do is crack jokes on IRC while others do the coding: here is a list of areas that we may need to discuss at some point, off the top of my head. Naturally, I do not mean to imply I am the only one thinking about these things.

Please keep in mind that my direct experience with Roguelikes is limited.

# Details #

  * Generating dungeons. Wouldn't it be a bit easier to just edit one manually at first? Or would that tempt us to never write a proper dungeon generator? It just seems clumsy to work on the game engine and the dungeon generator at the same time. (Of course, it could be split up between people...)
  * The simulation loop. This will require careful design. E.g. you can't just move the player when he wants, he might be ensnared or something. (Carefully reading the wow patch notes leads one to conclude that Blizzard doesn't have a particular clean design for this themselves...)
  * The combat system. I have only a vague clue how this works in Roguelikes (is it a new mode or not?), but these can grow quite convoluted.
  * The random seed. When we do generate dungeons, it should all come one random seed to make testing easier. Probably painfully obvious.

More when I think of it.
