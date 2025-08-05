# 아기상어가 최소거리로 이동하며 물고기 먹음(여러마리라면 가장 위,왼쪽 물고기 dir에서 고려) -> BFS
# 1. 자기보다 작은 크기의 물고기만 먹음(처음 아기상어 2) -> 더 이상 물고기 못먹으면 gg
# 2. 크기가 같거나 작은 물고기는 이동가능함
# 3. 물고기를 먹으면 그 칸은 빈칸 -> 물고기 크기 만큼 물고기를 먹으면 1씩 성장 (from 2)
# 방문행렬 필요x -> 물고기 먹으면 0으로 바꾸는 것만 유의
# 1, 1, 12, 12, 12, 123, 123, 123, 123 ...

from collections import deque

DIERCTIONS = [(0,1), (-1,0), (1,0), (0,-1)] # 위, 왼쪽 먼저가도록 설계
def bfs(startCol, startRow):
    global matrix, N
    q = deque([(startCol, startRow, 0)])





N = int(input())
matrix = [ list(map(int, input().split())) for _ in range(N) ]
fishList = [ [] for _ in range(7) ]
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 9:
            startCol, startRow = col, row
            matrix[row][col] = 0
        elif matrix[row][col] == 1:
            fishList[1].append((col, row))
        elif matrix[row][col] == 2:
            fishList[2].append((col, row))
        elif matrix[row][col] == 3:
            fishList[3].append((col, row))
        elif matrix[row][col] == 4:
            fishList[4].append((col, row))
        elif matrix[row][col] == 5:
            fishList[5].append((col, row))
        elif matrix[row][col] == 6:
            fishList[6].append((col, row))





