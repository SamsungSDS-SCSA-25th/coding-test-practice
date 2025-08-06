# 최소 배터리 사용량
# 간 곳은 또 방문하지 않음 -> visited (순열)
# 끝은 무조건 1번방이라는 조건!!!
# 백트래킹
# row: curRoom / col: nxtRoom

def dfs(curDepth, curRoom, curMoveSum):
    global N, matrix, minMove, visited
    #1 가지치기
    if curMoveSum >= minMove:
        return

    #2 종료조건
    if curDepth == N-1:
        curMoveSum += matrix[curRoom][0] # 맨 마지막에는 1번방 비용 더하기
        minMove = min(minMove, curMoveSum)
        # print(f'{minMove=}')
        return

    #3 하부재귀
    for nxtRoom in range(N):
        if not visited[nxtRoom] and curRoom != nxtRoom: # curRoom != nxtRoom
            visited[nxtRoom] = True
            dfs(curDepth + 1, nxtRoom, curMoveSum + matrix[curRoom][nxtRoom])
            visited[nxtRoom] = False


tc = int(input())
for i in range(1, tc+1):
    N = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(N) ]

    visited = [True] + [False] * (N-1)
    minMove = 100*11
    dfs(0, 0, 0)
    print(f'#{i} {minMove}')