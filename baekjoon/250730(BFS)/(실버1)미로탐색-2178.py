# 미로의 최단거리 -> BFS
# (1,1) -> (M, N)

from collections import deque

moveList = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(startCol, startRow):
    global visitedMatrix, mazeMatrix, n, m
    q = deque([(startCol, startRow, 1)]) # (D) 처음도 1칸 이동으로 보는 것 같음
    visitedMatrix[startRow][startCol] = True

    while q:
        # print(f'{q=}')
        curColRowDist = q.popleft()
        curCol, curRow, curDist = curColRowDist[0], curColRowDist[1], curColRowDist[2]
        for dx, dy in moveList:
            nxtCol, nxtRow, nxtDist = curCol + dx, curRow + dy, curDist + 1
            if 0<=nxtCol<m and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]:
                if nxtRow == n-1 and nxtCol == m-1:
                    return nxtDist
                q.append((nxtCol, nxtRow, nxtDist))
                visitedMatrix[nxtRow][nxtCol] = True

    # return -> 문제에서 항상 도착가능하다고 함

n, m = map(int, input().split())
mazeMatrix = [ list(map(int, list(input()))) for _ in range(n) ]
visitedMatrix = [ [False]*m for _ in range(n) ]
for row in range(n):
    for col in range(m):
        if mazeMatrix[row][col] == 0: # 벽으로 막혀있으면 방문처리 True
            visitedMatrix[row][col] = True

ans = bfs(0, 0)
print(ans)