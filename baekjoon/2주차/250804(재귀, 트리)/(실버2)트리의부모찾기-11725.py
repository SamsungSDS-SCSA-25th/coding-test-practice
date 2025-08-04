# bfs 문제로 풀이 -> 인접행렬
# 부모인지 판단기준, root와 더 가까움 -> bfs 시 nxt로 가는 것이 자식임

from collections import deque

def bfs(startNode):
    global visited, adjMatrix, parent
    q = deque([startNode])
    visited[startNode] = True

    while q:
        curNode = q.popleft()
        for nxtNode in adjMatrix[curNode]:
            if not visited[nxtNode]:
                q.append(nxtNode)
                # (D) nxt의 부모는 cur이다! -> cur이 root와 더 가까움
                parent[nxtNode] = curNode
                visited[nxtNode] = True

    return

n = int(input())
# 간선 = 노드 - 1
adjInfo = [ tuple(map(int, input().split())) for _ in range(n-1) ]

adjMatrix = [ []*n for _ in range(n+1) ]
for node1, node2 in adjInfo:
    adjMatrix[node1].append(node2)
    adjMatrix[node2].append(node1)
# print(adjMatrix)

parent = [0] * (n+1)
visited = [False] * (n+1)
bfs(1)

for parentNode in parent[2:]:
    print(parentNode)