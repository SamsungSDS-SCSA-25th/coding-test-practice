# bfs를 사용해서 해당 노드의 parent 리스트를 구한다
# 두 노드의 parent 리스트를 root 노드까지 탐색한 뒤, 가장 앞쪽에 공통 숫자를 출력
## 위 방법 메모리초과 뜬다...
# 다른 아이디어??? -> LCA 방법이 있다고 한다.
# depth를 기록하고 같은 depth로 하나씩 올리고 두 숫자의 값이 같으면 된다.
### "트리는 사이클이 없어서 방문행렬 필요없음"

from collections import deque

def bfs(startNode):
    global adjMatrix, n, depth, parent
    q = deque([startNode])

    while q:
        curNode = q.popleft()
        for nxtNode in adjMatrix[curNode]:
            if nxtNode == parent[curNode]: # 부모를 다시만나면 중지
                continue

            q.append(nxtNode)
            parent[nxtNode] = curNode # nxt은 부모는 cur
            depth[nxtNode] = depth[curNode] + 1 # nxt로 갈수록 트리 깊이 깊어짐

    return

tc = int(input())
for i in range(1, tc+1):
    n = int(input())

    adjMatrix = [ [] for _ in range(n+1) ]
    isChild = [False] * (n + 1)
    for _ in range(n-1):
        node1, node2 = map(int, input().split()) # node1 부모 / node2 자식
        adjMatrix[node1].append(node2)
        adjMatrix[node2].append(node1)
        isChild[node2] = True # isChild에 False인 것이 루트노드

    targetNode1, targetNode2 = map(int, input().split())

    # 루트 노드는?
    for node in range(1, n+1):
        if not isChild[node]:
            rootNode = node
    # print(rootNode)

    parent = [0] * (n+1)
    depth = [0] * (n+1)

    # print('x')
    bfs(rootNode)

    while depth[targetNode1] > depth[targetNode2]: # targetNode1이 더 깊어서 쳐내야함
        targetNode1 = parent[targetNode1]
    while depth[targetNode1] < depth[targetNode2]: # targetNode2가 더 깊어서 쳐내야함
        targetNode2 = parent[targetNode2]

    # 위에서 depth가 같은 곳에서 부모노드가 같으면 아래 실행 x
    while targetNode1 != targetNode2: # 위에서 깊이 서로 맞추고 이제 올라가기
        targetNode1 = parent[targetNode1]
        targetNode2 = parent[targetNode2]

    print(targetNode1)