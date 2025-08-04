# 단방향 그래프
# 끝까지 같는지가 중요한 그래프탐색이라 -> DFS 사용해야 함

t = int(input())

def dfs(currentNode):
    global visited, adjMatrix, flag

    visited[currentNode] = True

    for nxtNode in adjMatrix[currentNode]:
        if not visited[nxtNode]: # 방문 x
            if nxtNode == endNode:
                flag = True
                break
            dfs(nxtNode)

for index in range(1, t+1):
    v, e = map(int, input().split())
    adjMatrix = [[] for _ in range(v+1)]
    for _ in range(e):
        start, end = map(int, input().split())
        adjMatrix[start].append(end)
    startNode, endNode = map(int, input().split())

    visited = [False for _ in range(v+1)]
    flag = False
    dfs(startNode)

    if flag:
        print(f'#{index} {1}')
    else:
        print(f'#{index} {0}')