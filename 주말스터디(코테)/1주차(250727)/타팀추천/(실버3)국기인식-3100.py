# 파티션을 나누고 -> 모든 경우의 수를 대입하고 카운트
# 행렬 + 전치행렬 고려

matrix = [ list(input()) for _ in range(6) ]
matrixT = list(map(list, zip(*matrix)))

# 색상 찾기
colorList = []
for row in range(6):
    for col in range(9):
        colorList.append(matrix[row][col])
colorSet = sorted(set(colorList))
# print(colorSet)

minCnt = float('inf')
# 일반행렬 - ABA 패턴
for centerColor in colorSet:
    for aroundColor in colorSet:

        if aroundColor == centerColor:
            continue

        tempCnt = 0
        for row in range(2, 4):
            for col in range(9):
                if matrix[row][col] != centerColor:
                    tempCnt += 1

        for row in range(0, 2):
            for col in range(9):
                if matrix[row][col] != aroundColor:
                    tempCnt += 1

        for row in range(4, 6):
            for col in range(9):
                if matrix[row][col] != aroundColor:
                    tempCnt += 1

        minCnt = min(minCnt, tempCnt)

# 일반행렬 - ABC 패턴
for centerColor in colorSet:
    aroundColorSet = { color for color in colorSet if color != centerColor }
    for aroundColor1 in aroundColorSet:
        for aroundColor2 in aroundColorSet:

            if aroundColor1 == aroundColor2:
                continue

            tempCnt = 0
            for row in range(2, 4):
                for col in range(9):
                    if matrix[row][col] != centerColor:
                        tempCnt += 1

            for row in range(0, 2):
                for col in range(9):
                    if matrix[row][col] != aroundColor1:
                        tempCnt += 1

            for row in range(4, 6):
                for col in range(9):
                    if matrix[row][col] != aroundColor2:
                        tempCnt += 1

            minCnt = min(minCnt, tempCnt)

# 전치행렬 - ABA 패턴
for aroundColor in colorSet:
    for centerColor in colorSet:

        if aroundColor == centerColor:
            continue

        tempCnt = 0
        for row in range(3, 6):
            for col in range(6):
                if matrixT[row][col] != centerColor:
                    tempCnt += 1

        for row in range(0, 3):
            for col in range(6):
                if matrixT[row][col] != aroundColor:
                    tempCnt += 1

        for row in range(6, 9):
            for col in range(6):
                if matrixT[row][col] != aroundColor:
                    tempCnt += 1

        minCnt = min(minCnt, tempCnt)

# 전치행렬 - ABC 패턴
for centerColor in colorSet:
    aroundColorSet = { color for color in colorSet if color != centerColor }
    for aroundColor1 in aroundColorSet:
        for aroundColor2 in aroundColorSet:

            if aroundColor1 == aroundColor2:
                continue

            tempCnt = 0
            for row in range(3, 6):
                for col in range(6):
                    if matrixT[row][col] != centerColor:
                        tempCnt += 1

            for row in range(0, 3):
                for col in range(6):
                    if matrixT[row][col] != aroundColor1:
                        tempCnt += 1

            for row in range(6, 9):
                for col in range(6):
                    if matrixT[row][col] != aroundColor2:
                        tempCnt += 1

            minCnt = min(minCnt, tempCnt)

print(minCnt)