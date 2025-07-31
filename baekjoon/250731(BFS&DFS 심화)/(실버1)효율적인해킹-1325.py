# 컴퓨터가 신뢰관계 즉 네트워킹 되어 있음 -> 그래프탐색(영역구하기) -> BFS로 풀자
# A가 B를 신뢰하면 B가 A를 해킹가능

from collections import deque

def bfs(startNode):
    q = deque([startNode])
    visitedList[startNode] = True

    hackCnt = 1
    while q:
        curNode = q.popleft()
        for nxtNode in adjMatrix[curNode]:
            if not visitedList[nxtNode]:
                q.append(nxtNode)
                visitedList[nxtNode] = True
                hackCnt += 1

    return hackCnt

n, m = map(int, input().split())
networkInfoList = [ tuple(map(int, input().split())) for _ in range(m) ]
adjMatrix = [ [] for _ in range(n+1) ]
for networkInfo in networkInfoList:
    node1, node2 = networkInfo[0], networkInfo[1]
    adjMatrix[node2].append(node1) # (D) 단방향 유의

hackCntList = []
maxhackCnt = float('-inf')
for cmpIdx in range(1, n+1):
    visitedList = [False] * (n + 1) # (D) 방문리스트 초기화
    hackCnt = bfs(cmpIdx)
    maxhackCnt = max(maxhackCnt, hackCnt)
    hackCntList.append((cmpIdx, hackCnt))

hackCntList.sort(key=lambda x: (-x[1], x[0])) # hackCnt 내림차순, cmpIdx 오름차순
for hackCnt in hackCntList:
    cmpIdx, hackCnt = hackCnt[0], hackCnt[1]
    if hackCnt == maxhackCnt:
        print(cmpIdx, end=' ')