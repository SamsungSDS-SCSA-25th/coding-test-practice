# bfs로 카운트하는 방법을 사용
# 문제 이해를 확실히 하고 구현할 필요가 있음
# (D) 아무지역도 물에 잠기지 않을 수 있다... -> 비가 0인 경우도 있다는 소리

from collections import deque

moveList = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(startCol, startRow):
    global visitedMatrix, areaMatrix, n
    q = deque([(startCol, startRow)]) # 거리를 세야함
    visitedMatrix[startRow][startCol] = True

    safeAreaCnt = 1
    while q:
        curCol, curRow = q.popleft()
        for dx, dy in moveList:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<n and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow))
                visitedMatrix[nxtRow][nxtCol] = True
                safeAreaCnt += 1

    # q를 다텀 -> 더이상 갈 곳이 없음
    return safeAreaCnt

n = int(input())
areaMatrix = [ list(map(int, input().split())) for _ in range(n) ]
maxHeight = max( max(colList) for colList in areaMatrix )

maxTotalSafeAreaList = []
for rainHeight in range(0, maxHeight+1):
    # 방문행렬 전처리하고 bfs 들어가야 함
    visitedMatrix = [ [False] * n for _ in range(n) ] # bfs 반복할 때마다 방문행렬 초기화
    for row in range(n):
        for col in range(n):
            if areaMatrix[row][col] <= rainHeight: # 물에 잠기면
                visitedMatrix[row][col] = True

    # area행렬 순회하며 영역 카운트 bfs
    tempTotalSafeAreaList = []
    for row in range(n):
        for col in range(n):
            if areaMatrix[row][col] > rainHeight and not visitedMatrix[row][col]:
                safeAreaCnt = bfs(col, row)
                # print(f'{safeAreaCnt=}')
                tempTotalSafeAreaList.append(safeAreaCnt)
    # if not tempTotalSafeAreaList: # (D) 안전영역이 없는 경우 예외처리
    #     maxTotalSafeAreaList.append(0)
    # else:
    maxTotalSafeAreaList.append(len(tempTotalSafeAreaList))

print(max(maxTotalSafeAreaList))