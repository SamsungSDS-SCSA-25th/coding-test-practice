# 최단거리 BFS
### (만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)
### (D) 범위 유의, down에 -붙이기

from collections import deque

def bfs(startFloor):
    global visitedSet, end
    q = deque([(startFloor, 0)])
    visitedSet.add(startFloor)

    while q:
        curFloor, curCnt = q.popleft()
        if curFloor == end:
            return curCnt

        for move in (up, -down):
            nxtFloor, nxtCnt = curFloor + move, curCnt + 1
            if 1<=nxtFloor<top+1 and nxtFloor not in visitedSet:
                q.append((nxtFloor, nxtCnt))
                visitedSet.add(nxtFloor)

    return -1

top, start, end, up, down = map(int, input().split())
visitedSet = set()
flag = False
answer = bfs(start)
if answer == -1:
    print("use the stairs")
else:
    print(answer)