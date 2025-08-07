## 시간초과 이슈로 고민하다가
### 흑 + 백을 나눠서 /2 만큼 시간복잡도 줄임

N = int(input())
matrix = [ list(map(int, input().split())) for _ in range(N)]

# 놓을 수 있는 칸(True) / 막힌 칸(False)
visitedColor = [[matrix[row][col] == 1 for col in range(N)] for row in range(N)]
# 대각선 검사
visitedLU = [False] * (2*N)  # '\' 대각선
visitedRU = [False] * (2*N)  # '/' 대각선

def solve(parity):
    """
    parity==0: (row+col)%2==0인 흑 칸만,
    parity==1: (row+col)%2==1인 백 칸만
    백트래킹한 뒤 가능한 최대 비숍 수를 반환
    """
    maxB = 0
    def backTracking(idx, cnt):
        nonlocal maxB
        if idx == N*N:
            maxB = max(maxB, cnt)
            return

        curRow = idx // N
        curCol = idx % N

        # 이 칸이 내 parity와 다르면, 그냥 다음 칸으로 -> 서로 다른 색끼리는 충돌 x
        # 흑칸이 둘 수 있는 최댓값 + 백칸이 둘 수 있는 최댓값 => 전체 최댓값
        if (curRow + curCol) % 2 != parity:
            backTracking(idx + 1, cnt)
            return

        # 놓을 수 있으면 놓기
        lu = curCol - curRow
        ru = curCol + curRow
        if visitedColor[curRow][curCol] and not visitedLU[lu] and not visitedRU[ru]:
            visitedLU[lu] = True
            visitedRU[ru] = True

            backTracking(idx + 1, cnt + 1)

            visitedLU[lu] = False
            visitedRU[ru] = False

        # 놓지 않는 경우
        backTracking(idx + 1, cnt)

    backTracking(0, 0)
    return maxB

ansBlack = solve(0) # 흑 탐색

# visited 대각선 리셋
visitedLU = [False] * (2*N)
visitedRU = [False] * (2*N)

ansWhite = solve(1) # 백 탐색

print(ansBlack + ansWhite)