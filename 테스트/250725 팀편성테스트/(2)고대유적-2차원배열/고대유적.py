# OO
# 이 문제는 무난하게 잘풀었다
# 전치행렬 구하는 방법 외워두기 -> 리스트맵리스트집별!
## 0에서 1을 센 것 2보다 큰 지
## 맨 마지막 인덱스에서 1이 등장한 경우 예외처리

### 첫번째는 행렬+전치행렬 / 두번째는 dxdy 이용

'''
t = int(input())

for index in range(t):
    n, m = map(int, input().split())
    matrix = [ list(map(int, input().split())) for _ in range(n) ]
    matrixT = list(map(list, zip(*matrix)))

    maxLength = 0
    # 열
    for colList in matrix:
        tempCnt = 0
        for idx, col in enumerate(colList):
            if col == 0:
                if tempCnt >= 2:
                    maxLength = max(maxLength, tempCnt)
                tempCnt = 0

            elif col == 1:
                tempCnt += 1
                if idx == len(colList)-1 and tempCnt >= 2:
                    maxLength = max(maxLength, tempCnt)

    #print(f'{maxLength=}')

    # 행
    for rowList in matrixT:
        tempCnt = 0
        for idx, row in enumerate(rowList):
            if row == 0:
                if tempCnt >= 2:
                    maxLength = max(maxLength, tempCnt)
                tempCnt = 0

            elif row == 1:
                tempCnt += 1
                if idx == len(rowList) - 1 and tempCnt >= 2:
                    maxLength = max(maxLength, tempCnt)

    print(f'#{index+1} {maxLength}')
'''

t = int(input())

directionList = [(1,0), (0,1)] # 완전탐색이라, 후방만 체크하면됨

for index in range(t):
    n, m = map(int, input().split())
    matrix = [ list(map(int, input().split())) for _ in range(n) ]

    maxCnt = float('-inf')
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 1:
                for direction in directionList:
                    tempCnt = 1 # tempCnt가 2부터 유적지로 봄
                    tempRow, tempCol = row, col
                    flag = True
                    while flag:
                        tempRow += direction[1]
                        tempCol += direction[0]
                        if 0<= tempRow <n and 0<= tempCol <m:
                            if matrix[tempRow][tempCol] == 1:
                                tempCnt += 1
                            elif matrix[tempRow][tempCol] == 0:
                                flag = False
                        else: # 좌표가 범위 밖으로 벗어나면
                            flag = False

                    maxCnt = max(maxCnt, tempCnt)

    print(f'#{index+1} {maxCnt}')