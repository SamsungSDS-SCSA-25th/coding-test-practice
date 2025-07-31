# XO
# 여러가지 방법으로 탐색 + 최소시간 -> BFS
# set을 사용하여 visited 운용 -> 메모리 이슈 -> (D) 그래도 메모리 초과?...
# (D) 튜플을 이용하여 거리를 제야함

''' #1
from collections import deque

def bfs(startNode, endNode):
    global visitedSet
    q = deque([(startNode, 0)])
    visitedSet.add(startNode) # set

    while q:
        curNode, curSec = q.popleft()
        # print(f'{curNode=}')
        if curNode == endNode:
            return curSec

        #1 x-1
        nxtNode, nxtSec = curNode - 1, curSec + 1
        if 0<=nxtNode<=100000 and nxtNode not in visitedSet: # (D) nxtNode는 범위 안에 있어야 함
            q.append((nxtNode, nxtSec))
            visitedSet.add(nxtNode)
        #2 x+1
        nxtNode, nxtSec = curNode + 1, curSec + 1
        if 0<=nxtNode<=100000 and nxtNode not in visitedSet: # (D) nxtNode는 범위 안에 있어야 함
            q.append((nxtNode, nxtSec))
            visitedSet.add(nxtNode)
        #3 2*x
        nxtNode, nxtSec = curNode*2, curSec + 1
        if 0<=nxtNode<=100000 and nxtNode not in visitedSet: # (D) nxtNode는 범위 안에 있어야 함
            q.append((nxtNode, nxtSec))
            visitedSet.add(nxtNode)

    return -1 # 이런 경우는 없을 것으로 생각 +1, -1이 있기 때문

n, k = map(int, input().split())
visitedSet = set()
minSec = bfs(n, k)
print(minSec)
'''
#2
from collections import deque

def bfs(startNode, endNode):
    global visitedSet
    q = deque([(startNode, 0)])
    visitedSet.add(startNode)

    while q:
        curNode, curSec = q.popleft()
        if curNode == endNode:
            return curSec

        for nxtNode in (curNode-1, curNode+1, curNode*2): # ok
            if 0<=nxtNode<=100000 and nxtNode not in visitedSet: # ok
                q.append((nxtNode, curSec+1))
                visitedSet.add(nxtNode)

    return -1 # 1씩 좌우로 왔다갔다 하기에 여기로 오면 안됨

n, k = map(int, input().split())
visitedSet = set()
minSec = bfs(n, k)
print(minSec)