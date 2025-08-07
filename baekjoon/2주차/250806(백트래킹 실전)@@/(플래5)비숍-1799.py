# 색이 없는 곳으로만 이동가능
# 대각행렬 2개 + 색칠한부분 -> visited 3개
# 백트래킹 row 기준으로 아래로 내려가기 -> col은 row가 증가해도 모두 방문해볼 수 있도록 설계

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 놓을 수 있는 칸(True) / 막힌 칸(False)
visitedColor = [[matrix[row][col] == 1 for col in range(N)] for row in range(N)]
# 대각선 검사
visitedLU = [False] * (2*N)  # '\'
visitedRU = [False] * (2*N)  # '/'

maxBishops = 0
def backTracking(idx, cnt):
    global maxBishops
    # 종료조건
    if idx == N*N:
        if cnt > maxBishops:
            maxBishops = cnt
        return

    curCol = idx % N
    curRow = idx // N
    # 2) (curCol, curRow)에 비숍 놓을 수 있으면 놓기 -> 놓을 수 있는 칸 True
    if visitedColor[curRow][curCol] and not visitedLU[curCol - curRow + (N-1)] and not visitedRU[curCol + curRow]:
        visitedLU[curCol - curRow + (N-1)] = True
        visitedRU[curCol + curRow]     = True

        backTracking(idx + 1, cnt + 1)

        visitedLU[curCol - curRow + (N-1)] = False
        visitedRU[curCol + curRow]     = False

    # 3) 놓지 않는 경우
    backTracking(idx + 1, cnt)

# 시작
backTracking(0, 0)
print(maxBishops)