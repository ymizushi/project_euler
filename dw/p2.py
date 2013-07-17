#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
 
ROW = 10
COLUMN = 10
 
class Tile:
    def __init__(self,kind,x,y):
        self.kind = kind
        self.beforeTile = None
        self.searched = False
        self.x = x
        self.y = y
 
tileArray = []

tile_map = [
["#","S","#","#","#","#","#","#",".","#"],
[".",".",".",".",".",".","#",".",".","#"],
[".","#",".","#","#",".","#","#",".","#"],
[".","#",".",".",".",".",".",".",".","."],
["#","#",".","#","#",".","#","#","#","#"],
[".",".",".",".","#",".",".",".",".","#"],
[".","#","#","#","#","#","#","#",".","#"],
[".",".",".",".","#",".",".",".",".","."],
[".","#","#","#","#",".","#","#","#","."],
[".",".",".",".","#",".",".",".","G","#"],
]

for y in range(COLUMN):
    for x in range(ROW):
        tileArray += [Tile(tile_map[y][x],x,y)]

def getTileByXY(x, y):
    if x<0 or y < 0:
        return None
    if x >= ROW or y >= COLUMN:
        return None
    return tileArray[y*ROW + x]
 
def check(x,y):
    if x<0 or y < 0:
        return False
    if x >= ROW or y >= COLUMN:
        return False
    tile = getTileByXY(x,y)
    if tile.searched:
        return False
    if tile.kind is "#":
        return False
    return True
 
def surroundTiles(tile):
    tiles = []
    if check(tile.x,tile.y-1):
        tiles += [getTileByXY(tile.x,tile.y-1)]
    if check(tile.x+1,tile.y):
        tiles += [getTileByXY(tile.x+1,tile.y)]
    if check(tile.x,tile.y+1):
        tiles += [getTileByXY(tile.x,tile.y+1)]
    if check(tile.x-1,tile.y):
        tiles += [getTileByXY(tile.x-1,tile.y)]
    return tiles
 
def choiceTile(tile):
    tiles = surroundTiles(tile)
    if tiles:
        choice = tiles[0]
        choice.beforeTile = tile
        choice.searched = True
        return choice
    return choiceTile(tile.beforeTile)
 
def scan(tile):
    if(tile.kind == "G"):
        return
    else:
        return scan(choiceTile(tile))
#  
tileArray[1].beforeTile = None
tileArray[1].searched = True
scan(tileArray[1])
for i in tileArray:
    if i.beforeTile == None:
        print "current:", i.x, i.y, i.kind
    else:
        print "before:", i.beforeTile.x, i.beforeTile.y, "current:", i.x, i.y , "kind",i.kind
print ""

stack = []
def path(tile,count):
    if tile.beforeTile:
        stack.append(tile)
        return path(tile.beforeTile, count+1)
    if tile.beforeTile == None:
        print "tile_xy,kind", tile.x,tile.y,tile.kind
        return count

lastTile = filter(lambda x:x.kind == "G", tileArray)
 
print path(lastTile[0],0)