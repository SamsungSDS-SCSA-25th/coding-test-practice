# 아기상어가 최소거리로 이동하며 물고기 먹음(여러마리라면 가장 위,왼쪽 물고기 dir에서 고려) -> BFS
# 1. 자기보다 작은 크기의 물고기만 먹음(처음 아기상어 2) -> 더 이상 물고기 못먹으면 gg
# 2. 크기가 같거나 작은 물고기는 이동가능함
# 3. 물고기를 먹으면 그 칸은 빈칸 -> 물고기 크기 만큼 물고기를 먹으면 1씩 성장 (from 2)

from collections import deque

DIERCTIONS = [(0,1), (-1,0), (1,0), (0,-1)] # 위, 왼쪽 먼저가도록 설계
def bfs(startCol, startRow):
    global matrix, N, sharkSize
    visited = [ [False]*N for _ in range(N) ] # 탐색마다 초기화
    fishList = []

    q = deque([(startCol, startRow, 0)])
    visited[startRow][startCol] = True

    eatFlag, eatVal = False, 0 # (D) eatVal도 처음에 0으로 초기화
    while q:
        curCol, curRow, curMove = q.popleft()
        # print(f'{curCol=},{curRow=},{curMove=}')
        if eatFlag: # (DD) 요 알고리즘 기억하기!!!
            if curMove >= eatVal: # 첫등장하는 거리가 append 되고 pop될때 중단 -> fishList에 append는 이미 다 끝났으므로
                return fishList

        for dx, dy in DIERCTIONS:
            nxtCol, nxtRow, nxtMove = curCol + dx, curRow + dy, curMove + 1
            if 0 <= nxtCol < N and 0 <= nxtRow < N and not visited[nxtRow][nxtCol]:
                if matrix[nxtRow][nxtCol]<=sharkSize: # 상어보다 작거나 같으면 통과가능
                    q.append((nxtCol, nxtRow, nxtMove))
                    visited[nxtRow][nxtCol] = True
                    if 0 < matrix[nxtRow][nxtCol] < sharkSize: # 그중에서 상어보다 작으면 먹음
                        fishList.append((nxtCol, nxtRow, nxtMove))
                        if not eatFlag:
                            eatFlag, eatVal = True, nxtMove # 다 fishList에 append하고 위에서 pop할때 중단하기 위한 flag
                        # print(f'{eatVal=}')

    return fishList # 못찾은 경우

N = int(input())
matrix = [ list(map(int, input().split())) for _ in range(N) ]

# 시작점 찾기
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 9:
            curCol, curRow, curMove = col, row, 0
            matrix[row][col] = 0 # 상어 현재 위치 0으로 초기화

# 물고기 더이상 먹을 수 없을때까지 반복 돌리기
sharkSize = 2
eatCnt = 0
sec = 0
while True:
    fishList = bfs(curCol, curRow)
    if not fishList: # 더 이상 먹을 물고기가 없음
        break

    fishList.sort(key=lambda x: (x[1], x[0])) # 같은거리면 가장 위, 가장 왼쪽 물고기 먹기 (D) 행열 순서 변경...
    curCol, curRow, curMove = fishList[0] # 다음 bfs용 값들 갱신

    matrix[curRow][curCol] = 0 # 먹은 물고기 0으로 초기화
    sec += curMove
    eatCnt += 1

    if eatCnt == sharkSize:
        eatCnt = 0
        sharkSize += 1

print(sec)