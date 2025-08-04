# 네트워크는 양방향이다
# 모든 경우의수를 보아야 하기에 DFS이다

def dfs(currentNode):
    global visited, cnt, adjMatrix, flag
    visited[currentNode] = True

    for nxtNode in adjMatrix[currentNode]: # -1하지 않는다
        if not visited[nxtNode]:
            cnt += 1
            dfs(nxtNode)

computerN = int(input()) # <= 100
networkingN = int(input())
networkingList = [ tuple(map(int, input().split())) for _ in range(networkingN) ]

adjMatrix = [[] for _ in range(computerN+1)]
for start, end in networkingList:
    adjMatrix[start].append(end)
    adjMatrix[end].append(start)

visited = [False for _ in range(computerN+1)]
flag = False
cnt = 0
dfs(1)

print(cnt)