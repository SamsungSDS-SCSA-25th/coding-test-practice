# 최단거리 -> BFS응용
# 시작하는 칸과 끝나는 칸도 포함해서 센다.
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
'''
### 아이디어: visited를 3차원으로 구성한다.
# broke | 0: 벽부수기 가능 1: 불가
from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(startCol, startRow):
    global matrix, visited3d, n, m
    q = deque([(startCol, startRow, 0, 1)])
    visited3d[startRow][startCol][0] = True

    while q:
        curCol, curRow, broke, curDist = q.popleft()
        if curCol == m-1 and curRow == n-1:
            return curDist

        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow, nxtDist = curCol + dx, curRow + dy, curDist + 1
            if 0<=nxtCol<m and 0<=nxtRow<n:
                if not visited3d[nxtRow][nxtCol][broke] and matrix[nxtRow][nxtCol] == 0: # 일반적으로
                    q.append((nxtCol, nxtRow, broke, nxtDist))
                    visited3d[nxtRow][nxtCol][broke] = True

                if not broke and matrix[nxtRow][nxtCol] == 1 and not visited3d[nxtRow][nxtCol][1]:
                    # 벽을 부수고 전환
                    q.append((nxtCol, nxtRow, 1, nxtDist))
                    visited3d[nxtRow][nxtCol][1] = True

    # 도착지까지 방문 못한 경우
    return -1

n, m = map(int, input().split())
matrix = [ list(map(int, list(input().rstrip()))) for _ in range(n) ]
visited3d = [ [ [False]*2 for _ in range(m) ] for _ in range(n) ]

answer = bfs(0, 0)
print(answer)
'''
#2 -> 벽을 부수는 순간 visited는 초기화된다고 생각 -> 최단거리 탐색시 새로운 상황이 발생한 것이라 왔던 길도 돌아갈 수 있다
# -> 3차원의 visited []순서 유의
from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(startCol, startRow):
    global N, M
    q = deque([])
    visited3d = [ [ [False]*2 for _ in range(M)] for _ in range(N) ]

    q.append((0, 0, 1, 0)) # col / row / 거리 / 벽부섰는지 0->1
    visited3d[startRow][startCol][0] = True

    while q:
        curCol, curRow, curDist, broke = q.popleft()
        if curCol == M-1 and curRow == N-1:
            return curDist

        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow, nxtDist = curCol + dx, curRow + dy, curDist + 1
            if 0<=nxtCol<M and 0<=nxtRow<N:
                # print(f'{nxtCol=}, {nxtRow=}, {nxtDist=}, {broke=}')
                # 일반적인 경우
                if not visited3d[nxtRow][nxtCol][broke] and matrix[nxtRow][nxtCol] != 1:
                    q.append((nxtCol, nxtRow, nxtDist, broke))
                    visited3d[nxtRow][nxtCol][broke] = True

                # 위 외, 벽을 만난다면? 벽수기 기회 한번 제공
                elif matrix[nxtRow][nxtCol] == 1 and broke == 0: # broke가 1로 바뀌면 이 loop 못옴
                    q.append((nxtCol, nxtRow, nxtDist, 1)) # 앞으로 broke는 1만 전파될 것
                    visited3d[nxtRow][nxtCol][1] = True

    return -1


N, M = map(int, input().split())
matrix = [ list(map(int, list(input().rstrip()))) for _ in range(N) ]

answer = bfs(0, 0)
print(answer)