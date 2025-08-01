# 인접리스트 만들어서 관리 -> 그래프
# 가장빨리 누르는 것?
# 간선간의 길이를 구해야함 -> BFS
### 임의의 벽을 만들어서 쉽게 그래프 만들기 가능

from collections import deque

adjDict = {
    'Q': ['W', 'A'],
    'W': ['Q', 'A', 'S', 'E'],
    'A': ['Q', 'W', 'S', 'Z'],
    'S': ['W', 'E', 'D', 'X', 'A', 'Z'],
    'E': ['W', 'S', 'D', 'R'],
    'D': ['E', 'S', 'X', 'C', 'F', 'R'],
    'R': ['E', 'D', 'F', 'T'],
    'F': ['R', 'T', 'G', 'V', 'C', 'D'],
    'T': ['R', 'F', 'G', 'Y'],
    'G': ['F', 'T', 'V', 'Y', 'H', 'B'],
    'Y': ['G', 'T', 'H', 'U'],
    'H': ['Y', 'U', 'G', 'J', 'B', 'N'],
    'U': ['Y', 'H', 'J', 'I'],
    'J': ['U', 'I', 'H', 'K', 'N', 'M'],
    'I': ['U', 'J', 'K', 'O'],
    'K': ['I', 'J', 'M', 'L', 'O'],
    'O': ['I', 'K', 'L', 'P'],
    'L': ['O', 'P', 'K'],
    'P': ['O', 'L'],
    'Z': ['A', 'S', 'X'],
    'X': ['Z', 'S', 'D', 'C'],
    'C': ['X', 'D', 'F', 'V'],
    'V': ['C', 'F', 'G', 'B'],
    'B': ['V', 'G', 'H', 'N'],
    'N': ['B', 'H', 'J', 'M'],
    'M': ['N', 'J', 'K']
}

def bfs(startNode, endNode):
    global adjDict, visitedSet
    q = deque([(startNode, 0)])
    visitedSet.add(start)

    while q:
        # print(f'{q=}')
        curNode, curDist = q.popleft()
        if curNode == endNode:
            # print(f'{curNode=} {curDist=}')
            return curDist

        for nxtNode in adjDict[curNode]:
            if nxtNode not in visitedSet:
                q.append((nxtNode, curDist + 1))
                visitedSet.add(nxtNode)


t = int(input())
for _ in range(t):
    sec = 0
    moji = list(input())
    for idx, ji in enumerate(moji):
        if idx == len(moji) - 1:
            sec += 1
            break
        sec += 1
        start = moji[idx]
        end = moji[idx+1]
        visitedSet = set() # bfs할때마다 초기화
        if start != end:
            dist = bfs(start, end)
            sec += 2*dist

    print(sec)