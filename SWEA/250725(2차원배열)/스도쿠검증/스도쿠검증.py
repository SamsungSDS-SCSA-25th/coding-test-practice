# 3가지 검증을 하고 나면 스도쿠 해결완료
# 전치행렬

t = int(input())

for index in range(t):
    puzzleMatrix = [ list(map(int, input().split())) for _ in range(9) ][::-1]
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
        for yStart in range(0, 9, 3):
            for xStart in range(0, 9, 3):
                tempList = [i for i in range(1, 10)]
                for row in range(yStart, yStart + 3):
                    for col in range(xStart, xStart + 3):

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