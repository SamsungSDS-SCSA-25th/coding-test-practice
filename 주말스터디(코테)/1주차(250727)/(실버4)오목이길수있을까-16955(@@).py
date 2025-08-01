## XX

# .을 탐색하고 -> X를 놓았을 때 -> 8가지 방향으로 X가 5개 연속하는지 확인
# 실패
## X인 곳에서 출발해서 5개 연속인지 봐야함 -> 10x10이므로 완전탐색
## -> X는 하나 사용할 수 있다고 구현하기
## 시작점이 .인 경우 놓치고 있었음...
### 뒤로 다시 돌아가는 방향은 검색할 필요 x

'''
directionList = [(-1, 1), (0, 1), (1, 1),
                 (-1, 0)        , (1, 0),
                 (-1, -1), (0, -1), (1, -1)]
'''
''' #1
directionList = [(1, 0), (1, 1), (0, 1), (-1, 1)]

matrix = [ list(input().rstrip()) for _ in range(10) ]

flag = False
for row in range(10):
    if flag:
        break
    for col in range(10):
        if flag:
            break
        if matrix[row][col] == 'X' or matrix[row][col] == '.':
            for dir in directionList:
                if matrix[row][col] == 'X': # xChance를 통해 X를 하나 둘 수 있도록 함
                    xChance = 1
                elif matrix[row][col] == '.':
                    xChance = 0
                tempCnt = 1
                for dist in range(1, 5):
                    tempRow = row + dir[1] * dist
                    tempCol = col + dir[0] * dist
                    if 0 <= tempRow < 10 and 0 <= tempCol < 10:
                        #print(f'{dir=} {dist=} {tempRow=}, {tempCol=}')
                        if matrix[tempRow][tempCol] == 'X':
                            tempCnt += 1
                            #print('X')
                        elif matrix[tempRow][tempCol] == '.':
                            #print('.')
                            xChance -= 1
                            if xChance < 0:  # xChance를 하나 더 써야한다면 다른 길 찾기
                                break
                            tempCnt += 1
                        elif matrix[tempRow][tempCol] == 'O': # 더이상 앞으로 못나감
                            #print('O')
                            break

                if tempCnt == 5:
                    flag = True
                    break

print(1 if flag else 0)
'''
'''
#2 완전탐색으로 델타검색
### 아이디어는 떠오름 하지만 분기에서 실수가 있었음...

# 모든 방향 8방향
moveList = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

goMatrix = [ list(input().rstrip()) for _ in range(10) ]
# print(goMatrix)

flag = False
for row in range(10):
    for col in range(10):
        for dx, dy in moveList: # 모든 점에 놓아보자
            if goMatrix[row][col] == 'X': # 대신 .에는 X를 하나 놓을 기회가 있음
                xChance = 1
            elif goMatrix[row][col] == '.':
                xChance = 0
            else:
                break

            tempCnt = 1 # tempCnt가 5면 가능
            for dist in range(1, 5):
                tempRow = row + dy * dist
                tempCol = col + dx * dist
                if 0 <= tempRow < 10 and 0 <= tempCol < 10 and xChance >= 0:
                    if goMatrix[tempRow][tempCol] == 'X':
                        tempCnt += 1
                    elif goMatrix[tempRow][tempCol] == '.':
                        tempCnt += 1
                        xChance -= 1
                        if xChance < 0:
                            break

                if tempCnt == 5:
                    flag = True
                    break
        if flag:
            break
    if flag:
        break

print(1 if flag else 0)
'''
#3 타인들 코드리뷰 -> 내방식대로해도 괜찮을 것 같음
moveList = [(0,1),(1,1),(1,0),(1,-1)] # 완전탐색이라 4방향 확인
goMatrix = [ list(input()) for _ in range(10) ]

goFlag = False
for row in range(10):
    for col in range(10):
        if goMatrix[row][col] == 'X':
            for dx, dy in moveList:
                xChance = 1 # (D) 변수 위치 유의
                stoneCnt = 1
                for dist in range(1, 5):
                    nxtCol, nxtRow = col + dx*dist, row + dy*dist
                    if 0 <= nxtCol < 10 and 0 <= nxtRow < 10:
                        if goMatrix[nxtRow][nxtCol] == '.':
                            xChance -= 1
                            stoneCnt += 1
                        elif goMatrix[nxtRow][nxtCol] == 'X':
                            stoneCnt += 1
                    else: # 범위 벗어나면 끝
                        break

                # print(stoneCnt, xChance)
                if stoneCnt == 5 and xChance >= 0:
                    # print('x')
                    goFlag = True
                    break

        elif goMatrix[row][col] == '.':
            for dx, dy in moveList:
                xChance = 1
                stoneCnt = 1 # x를 두고 시작한다
                for dist in range(1, 5):
                    nxtCol, nxtRow = col + dx * dist, row + dy * dist
                    if 0 <= nxtCol < 10 and 0 <= nxtRow < 10:
                        if goMatrix[nxtRow][nxtCol] == '.':
                            break # .이 나오면 그냥 끝
                        elif goMatrix[nxtRow][nxtCol] == 'X':
                            stoneCnt += 1
                    else: # 범위 벗어나면 끝
                        break

                if stoneCnt == 5:
                    goFlag = True
                    break

        if goFlag:
            break
    if goFlag:
        break

if goFlag:
    print(1)
else:
    print(0)