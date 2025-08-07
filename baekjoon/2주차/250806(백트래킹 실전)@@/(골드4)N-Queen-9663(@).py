# 행순으로 정사각형아래로 퀸을 두는 차례가 내려감
# 확인해봐야 할 것
# 1. 서로 다른 열을 사용하는가
# 2. 두 대각행렬에 포함하지 않은가 ( / -> 행열의 합 | \ -> 행열의 차 )
# 마지막 행까지 안전하게 도착하면 경우의수 +1
# 따라서 3개의 visited 사용

def backTracking(curRow):
    global answer
    #가지치기 x -> 재귀시 모두 걸러짐
    # 종료조건
    if curRow == N:
        answer += 1
        return
    # 재귀
    for curCol in range(N):
        if not visitedCol[curCol] and not visitedRightUp[curCol+curRow] and not visitedLeftUP[curCol-curRow+(N-1)]:
            visitedCol[curCol] = True
            visitedRightUp[curCol+curRow] = True
            visitedLeftUP[curCol-curRow+(N-1)] = True
            backTracking(curRow + 1)
            visitedCol[curCol] = False
            visitedRightUp[curCol + curRow] = False
            visitedLeftUP[curCol - curRow + (N - 1)] = False


N = int(input())
visitedCol = [False] * (N*N)
visitedRightUp = [False] * (2*N-1)
visitedLeftUP = [False] * (2*N-1) # 인덱스 유의

answer = 0
backTracking(0)
print(answer)