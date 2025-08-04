# bfs를 사용해서 해당 노드의 parent 리스트를 구한다
# 두 노드의 parent 리스트를 root 노드까지 탐색한 뒤, 가장 앞쪽에 공통 숫자를 출력
# A가 B의 부모라는 뜻

from collections import deque

def bfs(startNode):
    global adjMatrix, visited, parent, n
    q = deque([startNode])
    visited[startNode] = True

    while q:
        curNode = q.popleft()
        for nxtNode in adjMatrix[curNode]:
            if not visited[nxtNode]:
                q.append(nxtNode)
                visited[nxtNode] = True
                parent[nxtNode] = curNode # nxt(부모) - cur(자식)

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
    visited = [False] * (n+1)

    bfs(rootNode)

    # print(parent)

    parentList1, parentList2 = [], [] # 두개의 교집합이 있으면 break
    parentList1.append(targetNode1)
    parentList2.append(targetNode2)
    while True:
        tempParent1 = parent[targetNode1]
        parentList1.append(tempParent1)
        targetNode1 = tempParent1
        if tempParent1 == rootNode:
            break

    while True:
        tempParent2 = parent[targetNode2]
        parentList2.append(tempParent2)
        targetNode2 = tempParent2
        if tempParent2 == rootNode:
            break

    # print(f'{parentList1}, {parentList2}')
    flag = False
    for parent1 in parentList1:
        for parent2 in parentList2:
            if parent1 == parent2:
                answer = parent1
                flag = True
                break
        if flag:
            break

    print(answer)