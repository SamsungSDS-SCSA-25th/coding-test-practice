## OO
# bfs, dfs 모두 가능 -> 시간을 줄이기 위해 bfs
## (D) 거리를 세는 것이 아니라, apt를 카운트하는 알고리즘이 필요함
## dfs로도 풀어보자 -> 재귀를 생각해야 해서 bfs보다 좀 어려운 것 같음 -> "재귀한 횟수를 더해주면됨" (중요)
''' #1
from collections import deque

moveList = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(startCol, startRow):
    global visitedMatrix, aptMatrix, n
    q = deque([(startCol, startRow)])
    visitedMatrix[startRow][startCol] = True # (D) row, col 구분 잘하자...

    aptCnt = 1
    while q: # 끝까지 가야지 apt의 단지의 크기 알 수 있음
        curColRow = q.popleft()
        curCol, curRow = curColRow[0], curColRow[1]
        # print(f'{q=}')
        # print(f'{aptCnt=}')
        for dx, dy in moveList:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<n and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]:
                visitedMatrix[nxtRow][nxtCol] = True
                # print(f'{q=}')
                q.append((nxtCol, nxtRow))
                aptCnt += 1 # 1인 곳을 찾으면 무조건 카운트

    # q를 다 털어낼때까지의 거리를 구해야함
    return aptCnt

def dfs(startCol, startRow):
    global visitedMatrix, aptMatrix, n
    visitedMatrix[startRow][startCol] = True

    aptCnt = 1
    for dx, dy in moveList:
        nxtCol, nxtRow = startCol + dx, startRow + dy
        if 0<=nxtCol<n and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]:
            visitedMatrix[nxtRow][nxtCol] = True
            aptCnt += dfs(nxtCol, nxtRow) # (중요) 재귀함수의 값을 더해주면 인접한 1들을 모두 카운트가능

    # 재귀 이후의 결과 -> 현재노드를 기준으로 aptCnt 반환
    return aptCnt


n = int(input())
aptMatrix = [ list(map(int, list(input()))) for _ in range(n) ]
# print(aptMatrix)
visitedMatrix = [ [False]*n for _ in range(n) ]
for row in range(n):
    for col in range(n):
        if aptMatrix[row][col] == 0: # 0인 곳은 방문처리 True
            visitedMatrix[row][col] = True

aptList = []
for row in range(n):
    for col in range(n):
        if aptMatrix[row][col] == 1 and not visitedMatrix[row][col]: # (D) 1인 곳이고 아직 방문 안했으면
            # aptCnt = bfs(col, row)
            aptCnt = dfs(col, row)
            aptList.append(aptCnt)

aptList.sort()
print(len(aptList))
print(*aptList, sep='\n')
'''
#2
from collections import deque

moveList = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(startCol, startRow):
    global visitedMatrix, aptMatrix, n
    q = deque([(startCol, startRow)])
    visitedMatrix[startRow][startCol] = True

    aptCnt = 1
    while q:
        curCol, curRow = q.popleft()
        for dx, dy in moveList:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<n and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]:
                visitedMatrix[nxtRow][nxtCol] = True
                q.append((nxtCol, nxtRow))
                aptCnt += 1

    return aptCnt


n = int(input())
aptMatrix = [ list(map(int, list(input()))) for _ in range(n) ]
visitedMatrix = [ [False]*n for _ in range(n) ]
for row in range(n):
    for col in range(n):
        if aptMatrix[row][col] == 0:
            visitedMatrix[row][col] = True

aptList = []
for row in range(n):
    for col in range(n):
        if aptMatrix[row][col] == 1 and not visitedMatrix[row][col]:
            aptCnt = bfs(col, row)
            aptList.append(aptCnt)

aptList.sort()
print(len(aptList))
print(*aptList, sep='\n')