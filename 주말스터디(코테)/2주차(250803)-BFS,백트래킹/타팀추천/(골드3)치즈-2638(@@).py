# (0,0)에서 시작하여 BFS로 방문 -> 방문처리 되면 밖, 안되면 안
# 매 초마다 visited 초기화 및 밖, 안 구분
# 매 초마다 visited True 인 0값이 2개 이상 존재하면 치즈가 녹는 것으로 봄

''' #1
from collections import deque

DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
def bfs(visited, matrix):
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        curCol, curRow = q.popleft()
        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<m and 0<=nxtRow<n and matrix[nxtRow][nxtCol] == 0 and not visited[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow))
                visited[nxtRow][nxtCol] = True

    return

n, m = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

sec = 0
endFlag = False
targetMatrix = [ [0]*m for _ in range(n) ]
while not endFlag:

    if matrix == targetMatrix:
        endFlag = True
        break

    #1 0이 안과 밖인지 구분 -> 안: False, 밖: True
    visited = [ [False]*m for _ in range(n) ] # 초기화
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 1:
                visited[row][col] = True

    # print('x')
    bfs(visited, matrix)
    # print('x')

    #2 1인 부분에서 밖인 0(True)이 2개 이상이면 녹음
    #3 (D) 녹는 좌표 따로 저장
    meltList = []
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 1:
                # print(row, col)
                tempCnt = 0
                for dx, dy in DIRECTIONS:
                    nxtCol, nxtRow = col + dx, row + dy
                    if matrix[nxtRow][nxtCol] == 0 and visited[nxtRow][nxtCol]:
                        # print(f'{nxtCol}, {nxtRow}')
                        tempCnt += 1
                # print(tempCnt)
                if tempCnt >= 2:
                    meltList.append((col, row)) # (D) 좌표를 기억하고 나중에 0으로 일괄 수정으로 바꿈

    #4 matrix에서 meltList의 좌표 녹이기
    for col, row in meltList:
        matrix[row][col] = 0

    # print(matrix)
    sec += 1

print(sec)
'''
#2
# visited 계속 업데이트 -> visited가 false인 0은 안쪽에 있는 0 -> visited true인 0과 접촉한 것만 녹이기
# bfs 반복하고, visited 초기화해야함

from collections import deque

directions = [(1,0), (0,1), (-1,0), (0,-1)]
def bfs(startCol, startRow): #
    global visited, n, m
    q = deque([(startCol, startRow)])
    visited[startRow][startCol] = True

    while q:
        curCol, curRow = q.popleft()
        for dx, dy in directions:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<m and 0<=nxtRow<n and not visited[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow))
                visited[nxtRow][nxtCol] = True
    return

n, m = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

sec = 0
while True:
    if matrix == [ [0]*m for _ in range(n) ]:
        break

    #1 방문행렬 초기화
    visited = [ [False]*m for _ in range(n) ]
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 1:
                visited[row][col] = True

    #2 bfs로 visited True인 0 찾기 -> 가장자리는 치즈가 없다고 가정
    bfs(0, 0)

    #3-1 위 0을 만족하는 치즈를 찾고
    meltList = []
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 1:
                tempCnt = 0
                for dx, dy in directions:
                    nxtCol, nxtRow = col + dx, row + dy
                    if matrix[nxtRow][nxtCol] == 0 and visited[nxtRow][nxtCol]:
                        tempCnt += 1
                if tempCnt >= 2:
                    meltList.append((col, row))

    #3-2 치즈 녹이기
    for meltCol, meltRow in meltList:
        matrix[meltRow][meltCol] = 0

    sec += 1
print(sec)