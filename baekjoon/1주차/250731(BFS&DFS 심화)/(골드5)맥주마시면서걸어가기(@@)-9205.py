# XO
# 맨해튼 거리 공식 이용 -> x,y 좌표상에서 1000번 이동했을때 어디 좌표까지 이동이 가능할까요?
# 20개로 50m씩 가면, 1000m까지 이동이 가능함
#!! 맨허튼 거리 내에 편의점이 있는지 확인해야함(있으면 그래프 연결) -> 편의점이 있는 경우만 앞으로 계속 탐색하는 것임 !!

''' #1
from collections import deque

def bfs():
    global adjMatrix, visitedList, nodeXYList
    q = deque([0]) # 노드 0번, 즉 시작점부터 출발
    visitedList[0] = True # 시작점 방문처리

    while q:
        curNode = q.popleft()
        if curNode == n+1: # 노드 번호 맨마지막까지 갔다면 페스티벌 도착한 것
            return 'happy'

        for nxtNode in adjMatrix[curNode]:
            if not visitedList[nxtNode]:
                q.append(nxtNode)
                visitedList[nxtNode] = True

    return 'sad' # 목적지까지 간선으로 연결되어 있지 않다면?

t = int(input())
for _ in range(t):
    n = int(input())
    nodeXYList = [ tuple(map(int, input().split())) for i in range(n+2) ] # 모든 노드의 xy좌표 저장

    # (D) 인접행렬 만드는 아이디어 이해하기 -> "노드의 간선을 연결해서 그래프를 만드는 과정"
    adjMatrix = [ [] for _ in range(n+2) ] # (n+2)인 이유는 노드의 개수이기 때문이다
    for node1Idx in range(n+2): # 0~n+1 인덱스 까지 노드 번호 존재
        x1, y1 = nodeXYList[node1Idx] # 0은 시작노드 / n+1은 도착노드
        for node2Idx in range(node1Idx+1, n+2):
            x2, y2 = nodeXYList[node2Idx]
            if abs(x1-x2) + abs(y1-y2) <= 1000: # 20개의 맥주를 가지고 갈 수 있는 좌표범위
                adjMatrix[node1Idx].append(node2Idx) # 양방향 -> 서로 편의점을 탐색하면서 앞으로 나아갈 수 있음
                adjMatrix[node2Idx].append(node1Idx)

    visitedList = [False]*(n+2)
    emotion = bfs()
    print(emotion)
'''
#2 -> 맨해튼 거리를 이용한 아이디어 중요
# 맨해튼 거리는 2차원에서 이동할 수 있는거리와 두 좌표간의 관계 (암기)
# 편의점을 노드로 사용해서, 집->페스티발까지의 연결여부를 구하는 문제 -> 1차원 그래프탐색

from collections import deque

def bfs(startNode, endNode): # 1차원 그래프
    q = deque([startNode])
    visitedList[startNode] = True

    while q:
        curNode = q.popleft()
        if curNode == endNode:
            return 'happy'

        for nxtNode in adjMatrix[curNode]:
            if not visitedList[nxtNode]:
                q.append(nxtNode)
                visitedList[nxtNode] = True

    return 'sad'

t = int(input())
for _ in range(t):
    n = int(input())
    nodeXYList = [()]
    for _ in range(n+2):
        x, y = map(int, input().split())
        nodeXYList.append((x, y))

    adjMatrix = [ [] for _ in range(n+2 + 1) ]
    for node1 in range(1, n+2 + 1): # nC2 2개 조합해서
        for node2 in range(node1+1, n+2 + 1):
            x1, y1 = nodeXYList[node1][0], nodeXYList[node1][1]
            x2, y2 = nodeXYList[node2][0], nodeXYList[node2][1]
            if abs(x1-x2) + abs(y1-y2) <= 1000: # node간의 이동거리가 1000m(50m*20개) 이내
                adjMatrix[node1].append(node2) # 양방향 -> 편의점 방향제한 x
                adjMatrix[node2].append(node1)

    visitedList = [False]*(n+2 + 1)
    emotion = bfs(1, n+2) # 시작노드 번호, 끝노드 번호
    print(emotion)