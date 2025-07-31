# OO
# 유기농 배추와 비슷한 문제로 보임
# 직사각형이 칠해진 곳을 True로 바꾸고 dxdy하면 될듯

##### -> 삼성은 sys 사용불가... 고려x

import sys
sys.setrecursionlimit(10000) #재귀호출 기본 값 1000 => 10000

''' #1
moveList = [(1,0), (0,1), (-1,0), (0,-1)]

def dfs(curRow, curCol):
    global visitedMatrix, tempCnt
    visitedMatrix[curRow][curCol] = True

    for dx, dy in moveList:
        nxtRow, nxtCol = curRow+dy, curCol+dx
        if 0<=nxtRow<m and 0<=nxtCol<n and not visitedMatrix[nxtRow][nxtCol]:
            tempCnt += 1
            dfs(nxtRow, nxtCol)


m, n, k = map(int, input().split()) # <=100 자연수 오른쪽 위 (N, M)
xyxyList = []
visitedMatrix = [[False]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    xyxyList.append([x1, y1, x2, y2])
    for row in range(y1, y2): # True값 채워넣기
        for col in range(x1, x2):
            visitedMatrix[row][col] = True

cntList = []
for row in range(m):
    for col in range(n):
        if not visitedMatrix[row][col]:
            tempCnt = 1
            dfs(row, col)
            cntList.append(tempCnt)

        # print(tempCnt)

cntList.sort()
print(len(cntList))
print(*cntList)
'''
#2
# 카운트 시점이 언제인지 살짝 고민함

import sys
sys.setrecursionlimit(10000) #재귀호출 기본 값 1000 => 10000

moveList = [(1,0), (0,1), (-1,0), (0,-1)]

# row, col 인수로서의 위치 유의
def dfs(startCol, startRow):
    global visitedMatrix, paperMatrix, r, c, squareCnt
    visitedMatrix[startRow][startCol] = True

    for dx, dy in moveList:
        nxtRow, nxtCol = startRow+dy, startCol+dx
        if 0<=nxtRow<r and 0<=nxtCol<c and not visitedMatrix[nxtRow][nxtCol]:
            visitedMatrix[nxtRow][nxtCol] = True
            squareCnt += 1
            dfs(nxtCol, nxtRow)

    return squareCnt


r, c, k = map(int, input().split())
paperMatrix = [ [0]*c for _ in range(r)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(y1, y2):
        for col in range(x1, x2):
            paperMatrix[row][col] += 1

visitedMatrix = [ [False]*c for _ in range(r) ]
for row in range(r):
    for col in range(c):
        if paperMatrix[row][col] > 0:
            visitedMatrix[row][col] = True

squareList = []
for row in range(r):
    for col in range(c):
        squareCnt = 1 # (D) dfs 들어가기 전에 1로 초기화
        if not visitedMatrix[row][col]:
            squareCnt = dfs(col, row)
            squareList.append(squareCnt)

squareList.sort()
print(len(squareList))
print(*squareList)