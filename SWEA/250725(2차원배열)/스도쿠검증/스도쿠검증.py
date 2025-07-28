# 3가지 검증을 하고 나면 스도쿠 해결완료
# 전치행렬
### set을 사용하여 중복을 제거하는 방식도 있음

t = int(input())

for index in range(t):
    puzzleMatrix = [ list(map(int, input().split())) for _ in range(9) ]
    puzzleMatrixT = list(map(list, zip(*puzzleMatrix)))

    #print(puzzleMatrix)
    #print(puzzleMatrixT)

    flag = True

    # 열에 겹치는 숫자가 있는지?
    if flag:
        for colList in puzzleMatrix:
            if flag == False:
                break
            for i in range(1, 10):
                if colList.count(i) != 1:
                    flag = False
                    break

    #print(flag)

    # 행에 겹치는 숫자가 있는지?
    if flag:
        for rowList in puzzleMatrixT:
            if flag == False:
                break
            for i in range(1, 10):
                if rowList.count(i) != 1:
                    flag = False
                    break

    #print(flag)

    # 3x3행렬에 겹치는 숫자가 있는지?
    if flag:
        for rowStart in range(0, 9, 3):
            for colStart in range(0, 9, 3):
                tempList = [i for i in range(1, 10)]
                for row in range(rowStart, rowStart + 3):
                    for col in range(colStart, colStart + 3):

                        if puzzleMatrix[row][col] in tempList:
                            tempList.remove(puzzleMatrix[row][col])
                        #print(tempList)

                if len(tempList) != 0:
                    flag = False
                    break

    if flag:
        print(f'#{index + 1} {1}')
    elif not flag:
        print(f'#{index + 1} {0}')