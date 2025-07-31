## XO

''' 중요포인트
1. 다섯알의 전, 후도 탐색해서 딱 다섯알만 있는지 확인해야함
2. 오른쪽으로 돌이 놓아진다는 보장이 없어, 첫번째 돌이 가장 왼쪽에 있다는 보장이 없어 정렬해야함
3. 완전탐색은 델타를 8개에서 4개로 줄여도 됨
4. 범위 조건은 앞에 나와야 함...
'''
''' #1
moveList = [(1,0),(1,1),(0,1),(-1,1)]
goMatrix = [ list(map(int, input().split())) for _ in range(19) ]

winFlag = False
for row in range(19):
    for col in range(19):
        if goMatrix[row][col] != 0: # 1과 2중에 검색시작
            curColor = goMatrix[row][col]
            for dx, dy in moveList:

                prevRow, prevCol = row - dy, col - dx # 한 칸전 체크
                if 0<=prevRow<19 and 0<=prevCol<19 and goMatrix[prevRow][prevCol] == curColor: # (D) 범위조건은 앞에 나와야 함
                    continue

                tempCnt = 1
                tempGoXYList = [(col, row)]
                for dist in range(1, 5): # 앞으로 4칸을 더 확인하고 카운트
                    nxtRow, nxtCol = row + dy*dist, col + dx*dist
                    if 0<=nxtRow<19 and 0<=nxtCol<19 and goMatrix[nxtRow][nxtCol] == curColor:
                        tempGoXYList.append((nxtCol, nxtRow))
                        tempCnt += 1

                if tempCnt == 5: # 다섯개의 돌이 나란히
                    lastRow, lastCol = row + dy*5, col + dx*5
                    if not (0<=lastRow<19 and 0<=lastCol<19 and goMatrix[lastRow][lastCol] == curColor): # 다음 칸에 또 돌이 안들어오면 / not ()도 가능
                        winFlag = True
                        tempGoXYList.sort(key = lambda x: x[0])
                        ansColor, ansRow, ansCol = curColor, tempGoXYList[0][1]+1, tempGoXYList[0][0]+1

        if winFlag:
            break
    if winFlag:
        break

if winFlag:
    print(ansColor)
    print(ansRow, ansCol)
else:
    print(0)
'''
#2 시작하는 좌표가 오름차순의 앞순서이기를 보장하는 델타를 사용하자, 6목 주의
moveList = [(0,1),(1,1),(1,0),(1,-1)]
goMatrix = [ list(map(int, input().split())) for _ in range(19) ]

goFlag = False
for row in range(19):
    for col in range(19):
        if goMatrix[row][col] != 0:
            for dx, dy in moveList:
                # 앞에 하나 -> 조건 만족하지 않으면 건너뛰기
                preCol, preRow = col - dx, row - dy
                if 0<=preCol<19 and 0<=preRow<19 and goMatrix[preRow][preCol] == goMatrix[row][col]:
                    continue

                # 오목
                stoneCnt = 1
                for dist in range(1, 5):
                    nxtCol, nxtRow = col + dx * dist, row + dy * dist
                    if 0<=nxtCol<19 and 0<=nxtRow<19 and goMatrix[nxtRow][nxtCol] == goMatrix[row][col]:
                        stoneCnt += 1
                    else: # 하나라도 조건이 안맞으면 다음 탐색하러
                        break

                # 뒤에 하나 -> 오목인데 육목일지도 모르니까
                if stoneCnt == 5:
                    aftCol, aftRow = col + dx*5, row + dy*5
                    if not (0<=aftCol<19 and 0<=aftRow<19 and goMatrix[aftRow][aftCol] == goMatrix[row][col]):
                        goFlag = True
                        ansColor, ansRow, ansCol = goMatrix[row][col], row+1, col+1

        if goFlag:
            break
    if goFlag:
        break

if goFlag:
    print(ansColor)
    print(ansRow, ansCol)
else:
    print(0)