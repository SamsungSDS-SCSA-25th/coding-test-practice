# 최단거리 -> BFS응용
# 시작하는 칸과 끝나는 칸도 포함해서 센다.
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
## 완전 탐색으로 0을 하나씩 1로 바꾼다 -> 그 후 bfs 진행
''' # 완전탐색 -> 시간초과
from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 벽하나 뿌수는 거 가능한거 고고하자
def bfs(startCol, startRow):
    global n, m, visited, matrix
    q = deque([(startCol, startRow, 1)])
    visited[startRow][startCol] = True

    while q:
        curCol, curRow, curMove = q.popleft()
        # print(curCol, curRow, curMove)
        if curCol == m-1 and curRow == n-1: # 도착
            # print('x')
            return curMove # 성공시

        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow, nxtMove = curCol + dx, curRow + dy, curMove + 1
            if 0<=nxtCol<m and 0<=nxtRow<n:
                if matrix[nxtRow][nxtCol] == 0 and not visited[nxtRow][nxtCol]:
                    visited[nxtRow][nxtCol] = True
                    q.append((nxtCol, nxtRow, nxtMove))
    # 실패시
    return -1


n, m = map(int, input().split())
matrix = [ list(map(int, list(input()))) for _ in range(n) ]
# print(matrix)

minMove = n*m + 1
for row in range(n):
    for col in range(m):
        if (row == 0 and col == 0) or (row == n-1 and col == m-1):
            continue

        if matrix[row][col] == 1:
            matrix[row][col] = 0 # 원소 하나 1로 바꿈

            # 방문행렬 초기화 및 벽 true로 세팅
            visited = [[False] * m for _ in range(n)]
            for row in range(n):
                for col in range(m):
                    if matrix[row][col] == 1:
                        visited[row][col] = True

            move = bfs(0, 0)
            # print(f'{move=}')
            if move != -1:
                minMove = min(minMove, move)
            matrix[row][col] = 1 # 원상복귀

print(minMove)
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