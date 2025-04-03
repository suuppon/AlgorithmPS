import sys
input = sys.stdin.readline

class Dice:
    def __init__(self):
        self.top, self.bottom, self.north, self.south, self.east, self.west = 0, 0, 0, 0, 0, 0
        
    def turn_north(self):
        self.top, self.north, self.bottom, self.south = self.south, self.top, self.north, self.bottom
        
    def turn_south(self):
        self.top, self.north, self.bottom, self.south = self.north, self.bottom, self.south, self.top
        
    def turn_east(self):
        self.top, self.east, self.bottom, self.west = self.west, self.top, self.east, self.bottom

    def turn_west(self):
        self.top, self.east, self.bottom, self.west = self.east, self.bottom, self.west, self.top

N, M, x, y, K = map(int, input().split())

Map = list()

for _ in range(N):
    row = list(map(int, input().split()))
    Map.append(row)

command_list = list(map(int, input().split()))

dice = Dice()

r, c = x, y
dr = [None, 0, 0, -1, 1]
dc = [None, 1, -1, 0, 0]

for cmd in command_list:
    nr = r + dr[cmd] 
    nc = c + dc[cmd]
    
    if not (0 <= nr < N and 0 <= nc < M):
        continue
    
    r, c = nr, nc
    
    if cmd == 1:
        dice.turn_east()
    elif cmd == 2:
        dice.turn_west()
    elif cmd == 3:
        dice.turn_north()
    elif cmd == 4:
        dice.turn_south()
        
    if Map[r][c] == 0:
        Map[r][c] = dice.bottom
    else:
        dice.bottom = Map[r][c]
        Map[r][c] = 0
    
    print(dice.top)