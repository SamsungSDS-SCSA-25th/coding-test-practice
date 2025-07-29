# 배추(노드)가 좌표평면에 존재 -> 인접행렬 사용하는 문제가 아님
# DFS로 풀이 -> 모두 방문할 때까지 cnt해야 함
# 중복카운트를 안하는 방법은 방문한 것은 모두 방문처리해서 validate해야 함

moveList = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(curRow, curCol):
    global visitedMatrix, cabbageMatrix
    visitedMatrix[curRow][curCol] = True

    for dx, dy in moveList:
        nxtRow = curRow + dy
        nxtCol = curCol + dx
        if 0<=nxtRow<n and 0<=nxtCol<m and not visitedMatrix[nxtRow][nxtCol]: # 부호방향 유의
            dfs(nxtRow, nxtCol)

t = int(input())

for index in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추의 개수
    cabbageInfoList = [ tuple(map(int, input().split())) for _ in range(k) ]

    # 배추행렬 만들기
    cabbageMatrix = [ [0]*m for _ in range(n) ]
    for cabbageInfo in cabbageInfoList:
        tempRow, tempCol = cabbageInfo[1], cabbageInfo[0]
        cabbageMatrix[tempRow][tempCol] = 1

    visitedMatrix = [ [False]*m for _ in range(n) ]
    wormCnt = 0

    # 0을 모두 방문처리
    for row in range(n):
        for col in range(m):
            if cabbageMatrix[row][col] == 0:
                visitedMatrix[row][col] = True

    for row in range(n):
        for col in range(m):
            if cabbageMatrix[row][col] == 1 and not visitedMatrix[row][col]: # (D) 조건을 걸고 DFS 하는 방법도 있음
                dfs(row, col)
                wormCnt += 1

    print(wormCnt)