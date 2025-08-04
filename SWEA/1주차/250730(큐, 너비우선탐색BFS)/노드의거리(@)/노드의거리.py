# 최소거리의 간선거리 구하는 문제 -> BFS
# 양방향
## 노드의 거리를 언제 + 할지에 대한 고민 -> dist를 같이 저장하면서 가야함...

from collections import deque

def bfs(startNode):
    global adjMatrix, visitedList, dist, endNode
    q = deque([(startNode, 0)]) # (D) (노드번호, 누적거리)
    visitedList[startNode] = True

    while q:
        curNode, dist = q.popleft()
        for nxtNode in adjMatrix[curNode]:
            if nxtNode == endNode:
                dist += 1
                return

            if not visitedList[nxtNode]:
                visitedList[nxtNode] = True
                q.append((nxtNode, dist + 1))

    dist = 0 # endNode 발견못하고 while문 탈출못하면

t = int(input())
for index in range(t):
    V, E = map(int, input().split())
    connectNodeInfoList = [ tuple(map(int, input().split())) for _ in range(E) ]
    startNode, endNode = map(int, input().split())

    # 인접행렬
    adjMatrix = [ [] for _ in range(V+1) ]
    for connectNodeInfo in connectNodeInfoList:
        node1, node2 = connectNodeInfo[0], connectNodeInfo[1]
        adjMatrix[node1].append(node2)
        adjMatrix[node2].append(node1) # 양방향

    # 방문리스트
    visitedList = [False] * (V+1)
    dist = 0

    bfs(startNode)

    print(f'#{index+1} {dist}')