# 방향전환에 대한 아이디어

col, row = map(int, input().split())
k = int(input())

directions = [(0,1),(1,0),(0,-1),(-1,0)]

matrix = [ [0]*col for _ in range(row) ]

curCol, curRow = 0, 0
matrix[0][0] = 1
num = 1
directionIdx = 0 # nxt가 (1) 범위 초과면, (2) 0이 아니면 +1 해줌
flag = True
while num < k:
    if num == col*row:
        flag = False
        break

    dx, dy = directions[directionIdx]
    nxtCol, nxtRow = curCol + dx, curRow + dy
    if nxtCol >= col or nxtCol < 0 or nxtRow >= row or nxtRow < 0 or matrix[nxtRow][nxtCol] != 0: # 방향전환
        directionIdx = (directionIdx+1) % 4
        dx, dy = directions[directionIdx]
        nxtCol, nxtRow = curCol + dx, curRow + dy

        num += 1
        matrix[nxtRow][nxtCol] = num
        curCol, curRow = nxtCol, nxtRow
        # print(f'{curCol=} {curRow=} {num=}')
        continue

    # 일반
    num += 1
    matrix[nxtRow][nxtCol] = num
    curCol, curRow = nxtCol, nxtRow
    # print(f'{curCol=} {curRow=} {num=}')

# print(matrix)
if flag:
    print(curCol+1, curRow+1)
else:
    print(0)