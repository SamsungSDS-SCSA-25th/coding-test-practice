# BFS
# 여러개의 정점이 연결되어 있을 경우에는 낮은번호의 정점을 우선적으로 방문한다. 양방향

from collections import deque

def bfs(startNode):
    global visitedList, adjMatrix, ansList
    q = deque([startNode])
    visitedList[startNode] = True
    ansList.append(startNode)

    while q: # 더이상 이웃노드 없을때까지
        curNode = q.popleft()
        for nxtNode in adjMatrix[curNode]:
            if not visitedList[nxtNode]:
                q.append(nxtNode)
                visitedList[nxtNode] = True
                ansList.append(nxtNode)
                # print(ansList)

t = int(input())
for index in range(t):
    V, E = map(int, input().split())
    xyInfoList = [ tuple(map(int, input().split())) for _ in range(E) ]
    adjMatrix = [[] for _ in range(V + 1)]
    for xyInfo in xyInfoList:
        start, end = xyInfo[0], xyInfo[1]
        adjMatrix[start].append(end)
        adjMatrix[end].append(start) # 양방향이다
    # print(adjList)

    visitedList = [False] * (V + 1)
    ansList = []
    bfs(1)

    print(f'#{index+1}', *ansList)