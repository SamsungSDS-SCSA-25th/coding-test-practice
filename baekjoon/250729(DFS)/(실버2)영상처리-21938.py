# rgb의 평균값으로 행렬을 새로 만들어서 풀이

##### -> 삼성은 sys 사용불가... 고려x
import sys
sys.setrecursionlimit(250000) #재귀호출 기본 값 1000 => 10000

moveList = [(1,0),(0,1),(-1,0),(0,-1)]

def dfs(curRow,curCol):
    global visitedMatrix
    visitedMatrix[curRow][curCol] = True

    for dx, dy in moveList:
        nxtRow, nxtCol = curRow+dy, curCol+dx
        if 0<=nxtRow<n and 0<=nxtCol<m and not visitedMatrix[nxtRow][nxtCol]:
            dfs(nxtRow, nxtCol)


n, m = map(int, input().split())
displayMatrix = [ list(map(int, input().split())) for _ in range(n) ]
t = int(input())

# 평균값 matrix으로 변경 -> 하나로 합쳐도 괜춘함
displayAvgMatrix = []
for row in range(n): # 3개씩 시작하는 좌표
    tempList = []
    for col in range(0, m*3, 3): # ---------
        tempSum = 0
        for tempCol in range(col,col+3): # 좌표 세개 선택
            tempSum += displayMatrix[row][tempCol]
        tempList.append(255 if tempSum / 3 >= t else 0)
    displayAvgMatrix.append(tempList)

# print(displayAvgMatrix)

# 0인 것들 전부 True로 변경
visitedMatrix = [ [False]*m for _ in range(n) ]
for row in range(n):
    for col in range(m):
        if displayAvgMatrix[row][col] == 0:
            visitedMatrix[row][col] = True

# dfs를 통해 붙어 있는 것 솎아내자 -> 배추농사하기 와 유사
objectCnt = 0
for row in range(n):
    for col in range(m):
        if not visitedMatrix[row][col]:
            dfs(row,col)
            objectCnt += 1

print(objectCnt)