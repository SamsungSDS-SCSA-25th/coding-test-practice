''' 중요포인트
1. 다섯알의 전, 후도 탐색해서 딱 다섯알만 있는지 확인해야함
2. 오른쪽으로 돌이 놓아진다는 보장이 없어, 첫번째 돌이 가장 왼쪽에 있다는 보장이 없어 정렬해야함
3. 완전탐색은 델타를 8개에서 4개로 줄여도 됨
4. 범위 조건은 앞에 나와야 함...
'''

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