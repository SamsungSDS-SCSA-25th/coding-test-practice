# 4방향 델타로 0이나 범위초과이면 둘레로 간주

DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]

n = int(input())
xyList = [ tuple(map(int, input().split())) for _ in range(n) ]
paper = [ [0]*100 for _ in range(100) ]
for x, y in xyList:
    for tempRow in range(y, y+10):
        for tempCol in range(x, x+10):
            paper[tempRow][tempCol] = 1

roundLen = 0
for row in range(100):
    for col in range(100):
        if paper[row][col] == 1:
            for dx, dy in DIRECTIONS:
                nxtCol, nxtRow = col + dx, row + dy
                if not (0<=nxtCol<100 and 0<=nxtRow<100 and paper[nxtRow][nxtCol] == 1):
                    roundLen += 1

print(roundLen)