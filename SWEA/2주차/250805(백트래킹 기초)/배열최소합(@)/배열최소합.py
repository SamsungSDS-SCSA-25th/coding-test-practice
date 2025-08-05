'''
# n개를 고르는데 세로로 같은 것 불가 -> 즉 열은 모두 달라야함
# usedCols를 재귀하여 각 호출마다 사본을 가지도록 함

def dfs(curRow, curSum, usedCols):
    global N, matrix, minSum
    # 가지치기 -> 최소값보다 더 크면 중단하고 뒤로 재귀
    if curSum >= minSum:
        return

    # 종료조건
    if curRow == N: #
        minSum = min(minSum, curSum)
        return

    # 재귀
    for curCol in range(N):
        if curCol in usedCols:
            continue
        dfs(curRow+1, curSum+matrix[curRow][curCol], usedCols | {curCol}) # 합집합


tc = int(input())
for i in range(1, tc+1):
    N = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(N) ]
    minSum = float('inf')

    print(f'#{i}', end=' ')
    dfs(0, 0, set())
    print(minSum)
'''
# 방문행렬을 사용하기 -> dfs 템플릿과 유사
def dfs(curRow, curSum):
    global N, matrix, minSum, visited
    # 가지치기 -> 최소값보다 더 크면 중단하고 뒤로 재귀
    if curSum >= minSum:
        return

    # 종료조건
    if curRow == N:
        minSum = min(minSum, curSum)
        return

    for curCol in range(N):
        if not visited[curCol]:
            visited[curCol] = True # 사용
            dfs(curRow+1, curSum+matrix[curRow][curCol])
            visited[curCol] = False # (D) visited 원상복귀


tc = int(input())
for i in range(1, tc+1):
    N = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(N) ]
    minSum = 10**9

    visited = [False] * (N+1)
    print(f'#{i}', end=' ')
    dfs(0, 0)
    print(minSum)