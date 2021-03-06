#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tile:
    def __init__(self,kind,x,y):
        self.kind = kind
        self.before_tile = None
        self.searched = False
        self.x = x
        self.y = y

class P2():
    def __init__(self, filename):
        self.tile_map = []
        self.row = 10
        self.column = 10
        self.tile_list = []
        self.tile_que = []
        self.tile_map = self.parse(filename)

        for y in range(self.column):
            for x in range(self.row):
                self.tile_list += [Tile(self.tile_map[y][x],x,y)]

        start_tile = filter(lambda x:x.kind == "S", self.tile_list)[0]
        self.tile_que += [start_tile]

    def calc(self):
        tile, count = self.choice_tile(self.tile_que,0)
        end_tile = filter(lambda x:x.kind == "G", self.tile_list)[0]
        return self.count_path(end_tile,0)

    # ファイルからテストデータ読み込み
    def parse(self, filename):
        data = []
        with open(filename) as f:
            for line in f:
                data += [list(line.strip('\n'))]
        return data

    def get_tile_by_x_y(self, x, y):
        if x<0 or y < 0:
            return None
        if x >= self.row or y >= self.column:
            return None
        return self.tile_list[y*self.row + x]
     
    def check(self, x,y):
        if x<0 or y < 0:
            return False
        if x >= self.row or y >= self.column:
            return False
        tile = self.get_tile_by_x_y(x,y)
        if tile.searched:
            return False
        if tile.kind is "#":
            return False
        return True
     
    def surround_tiles(self, tile):
        tiles = []
        if self.check(tile.x,tile.y-1):
            next_tile = self.get_tile_by_x_y(tile.x,tile.y-1)
            next_tile.before_tile = tile
            tiles += [next_tile]
        if self.check(tile.x+1,tile.y):
            next_tile = self.get_tile_by_x_y(tile.x+1,tile.y)
            next_tile.before_tile = tile
            tiles += [next_tile]
        if self.check(tile.x,tile.y+1):
            next_tile = self.get_tile_by_x_y(tile.x,tile.y+1)
            next_tile.before_tile = tile
            tiles += [next_tile]
        if self.check(tile.x-1,tile.y):
            next_tile = self.get_tile_by_x_y(tile.x-1,tile.y)
            next_tile.before_tile = tile
            tiles += [next_tile]
        return tiles

    def choice_tile(self, tile_que,count):
        tile = tile_que.pop(0)
        tile.searched = True
        if tile.kind == "G":
            return tile,count
        tiles = self.surround_tiles(tile)
        tile_que += tiles
        if tile_que:
            return self.choice_tile(tile_que,count+1)
        return tile,count

    def count_path(self, tile,count):
        if tile.before_tile and tile.kind != "S":
            return self.count_path(tile.before_tile, count+1)
        return count
