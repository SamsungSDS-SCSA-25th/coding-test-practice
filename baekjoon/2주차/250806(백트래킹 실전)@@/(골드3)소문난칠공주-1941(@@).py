#1 백트래킹으로 앞으로 7개의 조합을 찾는다
#2 bfs로 위 7개의 조합이 인접해 있는지 확인한다
''' #1
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
'''
# 조합 + BFS
#1 7명이 앉을 수 있는 조합구하기 -> "2차원의 좌표를 1차원으로 바꿀 수 있어야함"
#2 그 조합의 좌표를 2차원에 넣고, BFS로 이어져 있는지 + 4명이상인지 확인

from itertools import combinations
from collections import deque

DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(startCol, startRow, selected):
    q = deque([(startCol, startRow)])
    visited2d = [[False]*5 for _ in range(5)]
    visited2d[startRow][startCol] = True

    cnt = 1
    while q:
        curCol, curRow = q.popleft()
        for dx, dy in DIRECTIONS:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<5 and 0<=nxtRow<5:
                if not visited2d[nxtRow][nxtCol] and selected[nxtRow][nxtCol] == 1:
                    visited2d[nxtRow][nxtCol] = True
                    q.append((nxtCol, nxtRow))
                    cnt += 1

    return cnt == 7


matrix = [ list(input()) for _ in range(5) ]
answer = 0
for comb in combinations([ n for n in range(25)], 7): # 7공주 조합
    # S가 4개 이상이어야 함...
    sCnt = 0
    for idx in comb:
        col, row = idx % 5, idx // 5
        if matrix[row][col] == 'S':
            sCnt += 1

    if sCnt < 4:
        continue

    # 7공주의 2차원 좌표 꺼내기
    xyInfo = []
    for idx in comb:
        xyInfo.append((idx % 5, idx // 5)) # col, row 순
    # print(xyInfo)

    # bfs 위한 visited2d와 2차원에 7공주 넣기 필요
    selected = [ [0]*5 for _ in range(5) ]
    for col, row in xyInfo:
        selected[row][col] = 1
    # print(selected)
    # -> visited2d는 bfs에서 만들기로
    flag = bfs(xyInfo[0][0], xyInfo[0][1], selected) # 7공주 중 첫좌표에서 출발
    if flag:
        answer += 1

print(answer)