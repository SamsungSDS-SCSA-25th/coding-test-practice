# for문 한번만 시간초과 유의
# 3가지 방법에 대한 BFS 응용 -> 거리도 튜플에 담기

from collections import deque

def bfs(n, k, visitedSet):
    q = deque([(n, 0)])
    visitedSet.add(n)

    while q:
        curPos, curSec = q.popleft()
        # print(f'{curPos=}')
        if curPos == k:
            return curSec

        # (D) 2를 곱하는 부분 -> 거리 증분이 0이므로 최단거리를 구하는 것에 있어 우선순위가 앞이다.
        nxtPos = curPos * 2
        if 0<=nxtPos<=100000 and nxtPos not in visitedSet: # (D) 경계값 ...
            q.appendleft((nxtPos, curSec)) # (D) appendleft
            visitedSet.add(nxtPos)

        for nxtPos in (curPos-1, curPos+1):
            if 0<=nxtPos<=100000 and nxtPos not in visitedSet: # (D) 경계값...
                q.append((nxtPos, curSec+1))
                visitedSet.add(nxtPos)

    return # 여기 와서는 안됨

n, k = map(int, input().split())
visitedSet = set()
answer = bfs(n, k, visitedSet)
print(answer)