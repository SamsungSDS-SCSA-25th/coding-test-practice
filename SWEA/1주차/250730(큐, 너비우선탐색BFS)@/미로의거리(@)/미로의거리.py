# 거리를 어떻게 저장할지
# 1. 동훈프로님 -> 좌표값에 거리를 튜플 형태로 같이 저장 (x, y, 거리) -> 이 방법이 편한듯
# 2. 그래프의 0인 값을 그냥 하나씩 더해감 -> BFS만 가능. 왜냐하면 뒤로 재귀하지 않기 때문

from collections import deque

moveList = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(startCol, startRow):
    global visitedMatrix, mazeMatrix, n
    q = deque([[startCol, startRow, 0]])
    visitedMatrix[startRow][startCol] = True

    while q:
        # print(q)
        curColRowDist  = q.popleft()
        curCol, curRow, curDist = curColRowDist[0], curColRowDist[1], curColRowDist[2]
        # print(curCol, curRow, curDist)
        for dx, dy in moveList:
            nxtCol, nxtRow, nxtDist = curCol + dx, curRow + dy, curDist + 1
            if 0<=nxtCol<n and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]:
                # print(nxtRow, nxtCol)
                if mazeMatrix[nxtRow][nxtCol] == 3: # 도착좌표를 만나면
                    return nxtDist-1
                q.append([nxtCol, nxtRow, nxtDist]) # (D) q에 append해줘야 함
                visitedMatrix[nxtRow][nxtCol] = True

    # q를 다 털고도 3을 못찾은 경우
    return 0

t = int(input())
for index in range(t):
    n = int(input())
    mazeMatrix = [ list(map(int, list(input()))) for _ in range(n) ]
    startInfo = []
    visitedMatrix = [ [False]*n for _ in range(n) ]
    for row in range(n):
        for col in range(n):
            if mazeMatrix[row][col] == 2: # 시작좌표 저장 (x, y)
                startInfo.append([col, row])
            elif mazeMatrix[row][col] == 1:
                visitedMatrix[row][col] = True # 미로에서 벽은 방문표시 처리

    # print(startInfo)
    answer = bfs(startInfo[0][0], startInfo[0][1])

    print(f'#{index+1} {answer}')