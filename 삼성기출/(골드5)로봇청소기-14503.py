## validate
# 0은 청소되지 않은 칸 -> visited로 처리
# 1은 벽 -> matrix에서 1인 칸 못가도록 처리
# 4칸을 바라보고 행동 -> BFS사용

from collections import deque
DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]
def bfs(startCol, startRow, startDir):
    global visited, answer
    q = deque([(startCol, startRow, startDir)])
    visited[startRow][startCol] = True

    while q:
        curCol, curRow, curDir = q.popleft()
        print(f'{curCol=}, {curRow=}, {curDir=}')
        #1 4칸 확인
        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            #2-1 청소 진행하면됨 -> 무조건 청소할 곳이 있음
            if 0 <= nxtCol < M and 0 <= nxtRow < N and not visited[nxtRow][nxtCol] and visited[nxtRow][nxtCol] == 0:
                # 반복문
                idx = 0
                nnxtDir = (curDir - 1) % 4
                nnxtCol, nnxtRow = curCol + DIRECTIONS[nnxtDir][0], curRow + DIRECTIONS[nnxtDir][1]
                while True:
                    # 반시계방향 회전 -> curDir에서 1씩 빼고 % 4
                    if idx:
                        nnxtDir = (nnxtDir-1) % 4
                        nnxtCol, nnxtRow = nnxtCol + DIRECTIONS[nnxtDir][0], nnxtRow + DIRECTIONS[nnxtDir][1]
                    print(f'{nnxtDir=}')
                    print(f'{q=}')
                    # 바라보는 방향이 빈칸인지 확인 -> 빈칸이면 반복문 탈출
                    if matrix[nnxtRow][nnxtCol] == 0 and not visited[nnxtRow][nnxtCol]:
                        # q에 넣고 , cnt 올리고, 방문처리
                        q.append((nnxtCol, nnxtRow, nnxtDir))
                        print(f'{q=}')
                        visited[nnxtRow][nnxtCol] = True
                        answer += 1
                        break

                    idx += 1
        else:
            ## 위 4방향 확인 후 -> 청소진행가능한 곳이 없었음
            #2-2 4방향 모두 청소됨
            # curDir에서 2 더하고 % 4 방향으로 후진 반복
            nxtDir = (curDir + 2) % 4
            nxtCol, nxtRow = curCol + DIRECTIONS[nxtDir][0], curRow + DIRECTIONS[nxtDir][1]
            idx = 0
            while True:
                print(f'{answer=}')
                # 후진한 곳이 갈 수 있는 곳이라면
                if 0<=nxtCol<M and 0<=nxtRow<N and matrix[nxtRow][nxtCol] == 0:
                    if idx:
                        nxtCol, nxtRow = nxtCol + DIRECTIONS[nxtDir][0], nxtRow + DIRECTIONS[nxtDir][1]
                # 후진 하는 방향이 벽이면 그대로 멈춘다.
                if matrix[nxtRow][nxtCol] == 1:
                    break

                idx += 1


# 0 북 / 1 동 / 2 남 / 3 서
N, M = map(int, input().split())
startRow, startCol, startDir = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(N) ]

visited = [ [False]*M for _ in range(N) ]
answer = 1 # 처음에 빈칸은 청소하지 않은 상태
bfs(startCol, startRow, startDir)
print(answer)