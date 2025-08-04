# bfs를 사용해서 해당 노드의 parent 리스트를 구한다
# 두 노드의 parent 리스트를 root 노드까지 탐색한 뒤, 가장 앞쪽에 공통 숫자를 출력
## 위 방법 메모리초과 뜬다...
# 다른 아이디어??? -> LCA 방법이 있다고 한다.
# depth를 기록하고 같은 depth로 하나씩 올리고 두 숫자의 값이 같으면 된다.
### "트리는 사이클이 없어서 방문행렬 필요없음"

from collections import deque

def bfs(startNode):
    global adjMatrix, parent, depth, n
    q = deque([startNode])

    while q:
        curNode = q.popleft()
        for nxtNode in adjMatrix[curNode]:
            if nxtNode == parent[curNode]: # 이미 등록된 경우?
                continue
            q.append(nxtNode)
            parent[nxtNode] = curNode # nxt(부모) - cur(자식)
            depth[nxtNode] = depth[curNode] + 1 # 자식노드는 depth가 하나 아래

    return

t = int(input())
for _ in range(t):
    n = int(input())
    adjMatrix = [ [] for _ in range(n+1) ]
    isChild = [False] * (n+1)

    for idx in range(n-1):
        node1, node2 = map(int, input().split())
        adjMatrix[node2].append(node1) # 트리는 방향이 없음
        adjMatrix[node1].append(node2)
        isChild[node2] = True # node1이 부모, node2가 자식 -> False면 부모가 없음

    # (D) 루트는 한 번도 자식으로 등장하지 않은 노드
    for idx in range(1, n + 1): # temp용인 0 idx는 생략
        if not isChild[idx]:
            rootNode = idx
            break

    targetNode1, targetNode2 = map(int, input().split())

    # print(adjMatrix)

    parent = [0] * (n+1)
    depth = [0] * (n+1)
    # visited = [False] * (n+1) -> 트리라 방문행렬 필요없음

    bfs(rootNode)


    # 깊이 맞추기
    diff = depth[targetNode1] - depth[targetNode2]
    if diff > 0: # node1이 더 깊음
        for _ in range(diff):
            parentNode1 = parent[targetNode1]
            targetNode1 = parentNode1

    elif diff < 0: # node1이 더 깊음
        for _ in range(diff):
            parentNode2 = parent[targetNode2]
            targetNode2 = parentNode2

    # 동시에 부모로 올라가며 공통 조상 찾기
    while targetNode1 != targetNode2:
        targetNode1 = parent[targetNode1]
        targetNode2 = parent[targetNode2]





