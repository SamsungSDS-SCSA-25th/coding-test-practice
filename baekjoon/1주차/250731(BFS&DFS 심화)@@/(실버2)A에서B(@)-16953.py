# 아이디어 -> 최소값 BFS
# 뭐를 BFS? -> 곱하기2 / 끝에 1붙이기
# 연산한 것을 방문으로 카운트하고 q에 집어넣기
# 방문리스트을 어떻게 만들지? -> 그 값을 idx로 방문리스트 true/false

## 메모리가 초과했는데, 방문리스트 개수가 너무 많아서 그럼
## 미리 방문리스트를 쫙 만들지 말고, 실제로 방문한 곳만 -> 방문사전

from collections import deque

def bfs(startNode, endNode):
    global visitedDict
    q = deque([(startNode, 1)])
    visitedDict[startNode] = 1

    while q:
        curNode, curDist = q.popleft()
        if curNode == endNode:
            return curDist

        #1 : 2곱하기
        nxtNode, nxtDist = curNode*2, curDist+1
        if nxtNode <= endNode and nxtNode not in visitedDict:
            q.append((nxtNode, nxtDist))
            visitedDict[nxtNode] = 1
        #2 : 1붙이기
        nxtNode, nxtDist = int(str(curNode)+'1'), curDist+1
        if nxtNode <= endNode and nxtNode not in visitedDict:
            q.append((nxtNode, nxtDist))
            visitedDict[nxtNode] = 1

    return -1

a, b = map(int, input().split())
# visitedList = [False] * ((b-1)*2 + 1) # (b-1)*2 가 최댓값
visitedDict = {}
cnt = bfs(a, b)
print(cnt)