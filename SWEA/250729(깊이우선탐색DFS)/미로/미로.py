# 인접행렬을 사용하지 않고, dxdy를 사용해서 0인 부분을 찾아나감
# 실패시 다시 돌아와야 하므로, 재귀를 사용해야함 -> DFS / BFS도 가능함
## 1 visited에 포함시키기

t = int(input())

moveList = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(currentRow, currentCol):
    # 4방향 / 범위내 / 미방문 / *조건맞으면(벽이아니면)
    global visitedMatrix, mazeMatrix, flag, n
    visitedMatrix[currentRow][currentCol] = True

    for dx, dy in moveList: # 4방향에서
        nxtRow, nxtCol = currentRow + dy, currentCol + dx
        if 0<=nxtRow<n and 0<=nxtCol<n and not visitedMatrix[nxtRow][nxtCol]:
            if mazeMatrix[nxtRow][nxtCol] == 3:
                flag = True
                break
            dfs(nxtRow, nxtCol)


for index in range(1,t+1):
    n = int(input())
    mazeMatrix = [ list(map(int, list(input()))) for _ in range(n) ]

    flag = False
    visitedMatrix = [[False] * n for _ in range(n)] # (D) 1은 True로 바꿔주는 로직필요

    # 시작지점 좌표
    startRow, startCol = 0, 0
    for row in range(n):
        for col in range(n):
            if mazeMatrix[row][col] == 2:
                startRow, startCol = row, col
            elif mazeMatrix[row][col] == 1:
                visitedMatrix[row][col] = True

    dfs(startRow, startCol)

    if flag:
        print(f'#{index} {1}')
    else:
        print(f'#{index} {0}')