## X
#(D) 퀸의 경우 방문행렬 탐색할 때 유의해야함
# 방문행렬 뒤에 퀸이 갈수도 있기 때문

'''
def bfs(startCol, startRow):
    global visitedMatrix, n, m
    q = deque([(startCol, startRow)])
    # visitedMatrix[startRow][startCol] = True # 이미 아래에서 완료함

    while q:
        print(f'{q=}')
        curCol, curRow = q.popleft()
        for dx, dy in qMove:
            nxtCol, nxtRow = curCol + dx, curRow + dy
            if 0<=nxtCol<m and 0<=nxtRow<n and not visitedMatrix[nxtRow][nxtCol]:
                q.append((nxtCol, nxtRow))
                visitedMatrix[nxtRow][nxtCol] = True # 방문처리하여 먹히는 곳 표시
'''
kMove = [(1,2),(2,1),(2,-1),(1,-2), (-1,-2),(-2,-1),(-1,2),(-2,1)]
qMove = [(1,0),(-1,0),(0,1),(0,-1), (1,1),(-1,1),(-1,-1),(1,-1)]

n, m = map(int, input().split())
qList = list(map(int, input().split()))
qNum = qList[0]
qCRList = []
for idx in range(1, len(qList)-1, 2):
    r, c = qList[idx], qList[idx+1]
    qCRList.append((c-1, r-1))
kList = list(map(int, input().split()))
kNum = kList[0]
kCRList = []
for idx in range(1, len(kList)-1, 2):
    r, c = kList[idx], kList[idx+1]
    kCRList.append((c-1, r-1))
pList = list(map(int, input().split()))
pNum = pList[0] # (D) 오타...
pCRList = []
for idx in range(1, len(pList)-1, 2):
    r, c = pList[idx], pList[idx+1]
    pCRList.append((c-1, r-1))

visitedMatrix = [ [0]*m for _ in range(n) ]
# p가 있는 곳을 먼저 방문처리 -> 장애물역할만 함
for col, row in pCRList:
    visitedMatrix[row][col] = 1
# k도 있는 곳은 장애물임
for col, row in kCRList:
    visitedMatrix[row][col] = 1
# q가 있는곳도 장애물
for col, row in qCRList:
    visitedMatrix[row][col] = 1
######### ok

# 퀸 bfs 한번 돌리기 -> 앞에서 방문처리한 장애물들을 제외하고 가는 것임 -> 모두 True로 바뀌ㅏㅁ... (D)
# bfs가 아니라 한번에 가는 것... bfs 삭제
### (D) 퀸 방문행렬 재구조화, 0: 방문가능 / 1: 물리적점유 / 2: 방문처리한곳 (퀸 검사해야하는 척도)
for col, row in qCRList:
    for dx, dy in qMove:
        tempCnt = 0
        while True:
            tempCnt += 1
            nxtCol, nxtRow = col + dx*tempCnt, row + dy*tempCnt
            if 0<=nxtCol<m and 0<=nxtRow<n and (visitedMatrix[nxtRow][nxtCol] == 0 or visitedMatrix[nxtRow][nxtCol] == 2):
                visitedMatrix[nxtRow][nxtCol] = 2 # 퀸의 방문
            else:
                break

# print(visitedMatrix)

# 마지막으로 기사가 방문가능한 곳도 방문처리 -> 장애물의 제약없고 8방향만 체크
for col, row in kCRList:
    for dx, dy in kMove:
        nxtCol, nxtRow = col + dx, row + dy
        if 0<=nxtCol<m and 0<=nxtRow<n and visitedMatrix[nxtRow][nxtCol] == 0:
            visitedMatrix[nxtRow][nxtCol] = 2 # 기사의 방문

# print(visitedMatrix)

# 마지막으로 방문처리 안한 공간 탐색
cnt = 0
for row in range(n):
    for col in range(m):
        if visitedMatrix[row][col] == 0:
            cnt += 1
print(cnt)