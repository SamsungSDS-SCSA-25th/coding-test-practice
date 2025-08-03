# BFS 응용 -> curMove 만큼 2방향으로 탐색

from collections import deque

n = int(input())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

def bfs(matrix, visitedMatrix):
    q = deque([(0, 0)])
    visitedMatrix[0][0] = True

    while q:
        curCol, curRow = q.popleft()
        curMove = matrix[curRow][curCol]
        curDirections = [(curMove, 0), (0, curMove)]

        if matrix[curRow][curCol] == -1:
            return 'HaruHaru'

        for dx, dy in curDirections:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<n and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]: # (D) 방문행렬 방문안했을때
                q.append((nxtCol, nxtRow))
                visitedMatrix[nxtRow][nxtCol] = True

    return 'Hing'

visitedMatrix = [ [False]*n for _ in range(n) ]
print(bfs(matrix, visitedMatrix))