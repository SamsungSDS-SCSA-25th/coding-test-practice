# 미로탐색이랑 동일하고 4방향 -> 8방향
# 나이트의 이동dx,dy 정리하고 bfs로 탐색하면 될듯

from collections import deque

# 시계 방향으로 돈다 -> 8방향 (D) 방향 설정 잘하기...
moveList = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

def bfs(startXY, endXY):
    global visitedMatrix
    startCol, startRow = startXY[0], startXY[1]
    endCol, endRow = endXY[0], endXY[1]

    q = deque([(startCol, startRow, 0)])
    visitedMatrix[startRow][startCol] = True

    while q:
        curColRowDist = q.popleft()
        curCol, curRow, curDist = curColRowDist[0], curColRowDist[1], curColRowDist[2]
        for dx, dy in moveList:
            nxtCol, nxtRow, nxtDist = curCol + dx, curRow + dy, curDist + 1
            if 0<=nxtCol<n and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]:
                if nxtCol == endCol and nxtRow == endRow:
                    return nxtDist
                q.append((nxtCol, nxtRow, nxtDist))
                visitedMatrix[nxtRow][nxtCol] = True

    # bfs다 검색(q없음)해도 안나오는 경우
    return 0

t = int(input())
for index in range(t):
    n = int(input())
    startXY = tuple(map(int, input().split()))
    endXY = tuple(map(int, input().split()))

    # 인접행렬 필요x
    visitedMatrix = [ [False]*n for _ in range(n) ]

    ans = bfs(startXY, endXY)
    print(ans)