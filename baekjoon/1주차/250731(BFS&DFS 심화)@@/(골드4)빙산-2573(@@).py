## 치즈보다 쉬운 문제
# 빙산이 두덩이 이상되는 최소시간?
# -> BFS로 탐색하면서, cnt 2번 될 때 curSec가 답이다
# 0이 붙어 있는 것 만큼 감소함 -> matrix 업데이트 필요함
''' #1
from collections import deque

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs(startCol, startRow):
    global visited2d
    q = deque([(startCol, startRow)])
    visited2d[startRow][startCol] = True

    while q:
        curCol, curRow = q.popleft()
        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<M and 0<=nxtRow<N and not visited2d[nxtRow][nxtCol] and matrix[nxtRow][nxtCol] > 0: # (D) 다 녹고 음수가 나오는 경우 고려
                q.append((nxtCol, nxtRow))
                visited2d[nxtRow][nxtCol] = True

    return


N, M = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(N) ]

year = 0
while True:
    # 0인 곳 업데이트 -> 초기화 매번 진행
    visited2d = [ [False]*M for _ in range(N) ]
    iceList = []
    for row in range(N):
        for col in range(M):
            if matrix[row][col] <= 0: # (D) 다녹고 0보다 작아질 수도 있음
                visited2d[row][col] = True
            if matrix[row][col] > 0:
                iceList.append((col, row))

    # 빙산구역에서 방문하지 않은 곳 순환하고 cnt하기
    iceCnt = 0
    meltList = []
    for col, row in iceList:
        if matrix[row][col] > 0: # 0보다 큰값
            # 구역보기
            if not visited2d[row][col]: # 방문 안했다면
                bfs(col, row)
                iceCnt += 1 # 구역 더하기
            # (D) 녹일 부분 저장 -> 나중에 한꺼번에 녹여야함
            meltCnt = 0
            for dx, dy in DIRECTIONS:
                nxtCol, nxtRow = col + dx, row + dy
                if 0<=nxtCol<M and 0<=nxtRow<N and matrix[nxtRow][nxtCol] <= 0: # (D) 다녹고 0보다 작아질 수도 있음
                    meltCnt += 1
            meltList.append((col, row, meltCnt))

    if iceCnt >= 2: # 두덩이 이상임
        break
    elif iceCnt == 0: # (D) 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다. -> 다 녹은 상황 고려 (시간초과)
        year = 0 # (D) 위 동
        break

    # 녹이기
    for col, row, meltCnt in meltList:
        matrix[row][col] -= meltCnt

    # print(matrix)

    year += 1

print(year)
'''
#2 -> 0과 닿은 면적 확인하고, 그 이후에 녹여야 함
from collections import deque

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(startCol, startRow):
    global visited
    q = deque([(startCol, startRow)])
    visited[startRow][startCol] = True

    while q:
        curCol, curRow = q.popleft()
        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<M and 0<=nxtRow<N and matrix[nxtRow][nxtCol] > 0 and not visited[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow))
                visited[nxtRow][nxtCol] = True

    return


N, M = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(N) ]

year = 0
while True:

    year += 1

    # 0 빙산 좌표 구하기
    icedList = []
    for row in range(N):
        for col in range(M):
            if matrix[row][col] > 0: # (D) 단순히 빙산 좌표 구할때는 visited 쓰면 안됨
                icedList.append([col, row])

    # 1 0과 닿은 면적 확인
    for iceIdx, [col, row] in enumerate(icedList):
        tempCnt = 0
        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow = col + dx, row + dy
            if 0 <= nxtCol < M and 0 <= nxtRow < N and matrix[nxtRow][nxtCol] == 0:
                tempCnt += 1
        icedList[iceIdx].append(tempCnt)

    # 2 녹이기
    # print(f'{icedList=}')
    for col, row, melt in icedList:
        matrix[row][col] -= melt
        matrix[row][col] = max(0, matrix[row][col])  # 최하한선은 0

    # 3 빙산이 두개 이상인지 확인
    visited = [[False] * M for _ in range(N)]
    icedCnt = 0
    for row in range(N):
        for col in range(M):
            if matrix[row][col] > 0 and not visited[row][col]:
                bfs(col, row)
                icedCnt += 1

    # 빙산이 2개 이상으로 갈라진다면
    if icedCnt >= 2:
        answer = year
        break

    # 전부다 0이라서 icedCnt 할 것이 없음...
    if icedCnt == 0:
        answer = 0
        break

print(answer)