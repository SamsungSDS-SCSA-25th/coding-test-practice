#1 백트래킹으로 앞으로 7개의 조합을 찾는다
#2 bfs로 위 7개의 조합이 인접해 있는지 확인한다

from collections import deque

DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(startCol, startRow, selected):
    visited = [[False] * 5 for _ in range(5)]

    q = deque([(startCol, startRow)])
    visited[startRow][startCol] = True

    cnt = 1
    while q:
        curCol, curRow = q.popleft()
        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<5 and 0<=nxtRow<5 and selected[nxtRow][nxtCol] == 1 and not visited[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow))
                visited[nxtRow][nxtCol] = True
                cnt += 1

    return cnt == 7 # 7이면 True, 아니면 False

# 인접 True / 인접x False
def check(lst):
    # lst의 1차원을 좌표형태로 만들기
    xyInfo = []
    for n in lst:
        xyInfo.append((n % 5, n // 5)) # col, row

    # 좌표만들기 -> bfs 위함
    selected = [ [False]*5 for _ in range(5) ] # (D) selected와 visited 구분
    for col, row in xyInfo:
        selected[row][col] = 1

    # 첫좌표에서 쭉 이어져서 cnt 7개 인지 확인
    flag = bfs(xyInfo[0][0], xyInfo[0][1], selected)

    return flag

#1 백트래킹 7개의 조합 찾기
def backTracking(startIdx, sCnt, lst):
    global ansCnt
    # 가지치기
    if len(lst) > 7:
        return
    # 종료조건: 7개 골랐으면 탈출
    if len(lst) == 7:
        # print(sCnt)
        if sCnt >= 4 and check(lst): # (D) S가 4이상인지 확인
            ansCnt += 1
        return
    # 재귀
    for idx in range(startIdx, 25):
        if matrix[idx // 5][idx % 5] == 'S':
            cnt = 1
        else:
            cnt = 0
        backTracking(idx+1, sCnt+cnt, lst+[idx])


matrix = [ list(input()) for _ in range(5) ]

ansCnt = 0
backTracking(0, 0, [])
print(ansCnt)