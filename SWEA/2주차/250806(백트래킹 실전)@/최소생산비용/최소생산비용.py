# 최소생산비용, N이 미지수, 가능성 여러가지 -> 백트래킹
# N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산
### -> visited를 사용하자...

def dfs(curRow, curSum):
    global N, matrix, minSum, visited
    #1 가지치기
    if minSum <= curSum:
        return

    #2 종료조건
    if curRow == N:
        minSum = min(minSum, curSum)
        # print(f'{minSum=}')
        return

    #3 하부재귀
    for curCol in range(N):
        if not visited[curCol]:
            visited[curCol] = True
            dfs(curRow+1, curSum+matrix[curRow][curCol])
            visited[curCol] = False


tc = int(input())
for i in range(1, tc+1):
    N = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(N) ]
    visited = [False] * N

    minSum = 100*10
    dfs(0, 0)
    print(f'#{i} {minSum}')