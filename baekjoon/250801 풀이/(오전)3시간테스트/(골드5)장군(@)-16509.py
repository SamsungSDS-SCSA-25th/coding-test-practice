# bfs
### (D) 상이 가능길에 왕이 겹치는 경우 고려해야함

from collections import deque

moveList = [((0,1),(1,1),(2,3)),
            ((1,0),(2,1),(3,2)),
            ((1,0),(2,-1),(3,-2)),
            ((0,-1),(1,-2),(2,-3)),
            ((0,-1),(-1,-2),(-2,-3)),
            ((-1,0),(-2,-1),(-3,-2)),
            ((-1,0),(-2,1),(-3,2)),
            ((0,1),(-1,2),(-2,3))]

def bfs(startRow, startCol, endRow, endCol):
    global visitedMatrix
    q = deque([(startCol, startRow, 0)])
    visitedMatrix[startRow][startCol] = True

    while q:
        # print(f'{q=}')
        curCol, curRow, curDist = q.popleft()
        if curCol == endCol and curRow == endRow:
            return curDist

        for d1, d2, d3 in moveList: # (D) 증분값으로 사용하기
            check1X, check1Y = curCol + d1[0], curRow + d1[1]
            check2X, check2Y = curCol + d2[0], curRow + d2[1]
            if (check1Y == endRow and check1X == endCol) or (check2Y == endRow and check2X == endCol):
                # print('x')
                continue

            nxtCol, nxtRow, nxtDist = curCol + d3[0], curRow + d3[1], curDist + 1
            if 0 <= nxtRow < 10 and 0 <= nxtCol < 9 and not visitedMatrix[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow, nxtDist))
                visitedMatrix[nxtRow][nxtCol] = True

    return -1

# row 10 / col 9
startRow, startCol = map(int, input().split())
endRow, endCol = map(int, input().split())

visitedMatrix = [ [False]*9 for _ in range(10) ]
answer = bfs(startRow, startCol, endRow, endCol)

print(answer)