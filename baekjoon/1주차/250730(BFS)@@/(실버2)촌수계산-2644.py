# 양방향 그래프 탐색 -> BFS, DFS 모두 가능
# 시간을 줄이기 위해서 BFS 사용

from collections import deque

def bfs(startP):
    global visitedList, adjMatrix, endP
    q = deque([(startP, 0)])
    visitedList[startP] = True

    while q:
        # print(q)
        curPDist = q.popleft()
        curP, curDist = curPDist[0], curPDist[1]
        for nxtP in adjMatrix[curP]:
            if not visitedList[nxtP]:
                if nxtP == endP:
                    curDist += 1
                    return curDist
                q.append([nxtP, curDist + 1])
                visitedList[nxtP] = True # (D) 못찾는 경우 무한루프 도는 경우 방문리스트 확인!

    # q를 다 털고도 못찾으면
    return -1

n = int(input()) # 전체사람수
startP, endP = map(int, input().split())
m = int(input()) # 관계의 개수
pInfoMatrix = [ list(map(int, input().split())) for i in range(m) ] # 자식, 부모

# 인접행렬
adjMatrix = [ [] for _ in range(n+1) ]
for pInfoList in pInfoMatrix:
    start, end = pInfoList[0], pInfoList[1]
    adjMatrix[start].append(end) # 양방향
    adjMatrix[end].append(start)

# 방문리스트
visitedList = [False] * (n+1)
ans = bfs(startP)
print(ans)