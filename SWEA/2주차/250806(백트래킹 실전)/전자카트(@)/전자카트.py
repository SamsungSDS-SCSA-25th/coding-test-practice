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
    if curDepth == N:
        curMoveSum += matrix[curRoom][0]
        minMove = min(minMove, curMoveSum)
        # print(f'{minMove=}')
        return

    #3-1 세부조건
    if curDepth == N-1: # 마지막 1번방만 더 들어가면 됨
        dfs(curDepth+1, 0, curMoveSum + matrix[curRoom][0])
    #3-2 하부재귀
    for nxtRoom in range(1, N): # 1번방 제외하고 돌기
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