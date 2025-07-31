# 양방향 + 인접행렬 오름차순

from collections import deque

def dfs(curNode, connectList=[]):
    global adjMatrix, visitedMatrix
    visitedMatrix[curNode] = True
    connectList.append(curNode)

    for nxtNode in adjMatrix[curNode]:
        if not visitedMatrix[nxtNode]:
            # print(f'{nxtNode=}')
            # connectList.append(nxtNode) # (D) 재귀로 하기 때문에 여기서 append 안함
            # print(f'{connectList=}')
            visitedMatrix[nxtNode] = True
            dfs(nxtNode)

    return connectList

def bfs(startNode, connectList=[]):
    global adjMatrix, visitedMatrix
    q = deque([startNode])
    visitedMatrix[startNode] = True
    connectList.append(startNode)

    while q:
        curNode = q.popleft()
        # print(f'{curNode=}')
        for nxtNode in adjMatrix[curNode]:
            if not visitedMatrix[nxtNode]:
                # print(f'{nxtNode=}')
                q.append(nxtNode)
                visitedMatrix[nxtNode] = True
                connectList.append(nxtNode)

    return connectList

nodeNum, vertexNum, startNode = map(int, input().split())
adjMatrix = [[] for _ in range(nodeNum+1) ]
for _ in range(vertexNum):
    node1, node2 = map(int, input().split())
    adjMatrix[node1].append(node2)
    adjMatrix[node2].append(node1)
for adjList in adjMatrix: # (D) 오름차순 정렬
    adjList.sort()
# print(adjMatrix)

visitedMatrix = [False]*(nodeNum+1)
connectList = dfs(startNode)
print(*connectList)

visitedMatrix = [False]*(nodeNum+1) # (D) 방문행렬 한번 썼으니 다시 초기화
connectList = bfs(startNode)
print(*connectList)