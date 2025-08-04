# 빙고의 경우 행렬과 전치행렬, 그리고 두 대각선만 살펴보면된다.

# 열 확인
def matrixCheck(matrix):
    global tempCnt
    for row in range(5):
        if matrix[row] == [0, 0, 0, 0, 0]:
            tempCnt += 1

# 행 확인
def matrixTCheck(matrixT):
    global tempCnt
    for col in range(5):
        if matrixT[col] == [0, 0, 0, 0, 0]:
            tempCnt += 1

# 대각선 확인
def diagnoalCheck(matrix):
    global tempCnt
    tempList = []
    for size in range(5):
        if matrix[0+size][0+size] == 0:
            tempList.append(0)
    if tempList == [0, 0, 0, 0, 0]:
        tempCnt += 1

    tempList = []
    for size in range(5):
        if matrix[4-size][0+size] == 0:
            tempList.append(0)
    if tempList == [0, 0, 0, 0, 0]:
        tempCnt += 1


matrix = [ list(map(int, input().split())) for _ in range(5) ]

callList = []
for _ in range(5):
    x1, x2, x3, x4, x5 = map(int, input().split())
    callList.extend([x1, x2, x3, x4, x5])

for idx, call in enumerate(callList):
    tempCnt = 0
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == call:
                matrix[row][col] = 0

    matrixCheck(matrix)
    matrixTCheck(matrixT=list(map(list, zip(*matrix))))
    diagnoalCheck(matrix)

    if tempCnt >= 3:
        answer = idx + 1
        break

print(answer)