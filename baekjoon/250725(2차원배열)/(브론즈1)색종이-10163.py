# 2차원 배열에 색종이 번호를 원소값으로 대체하는 알고리즘

n = int(input())
infoList = [ list(map(int, input().split())) for _ in range(n) ]

emptyMatrix = [[0] * 1001 for _ in range(1001)]
for idx, info in enumerate(infoList):
    x, y, xLength, yLength = info[0], info[1], info[2], info[3]

    for row in range(y, y+yLength):
        for col in range(x, x+xLength):
            emptyMatrix[row][col] = idx + 1

#print(emptyMatrix)

for idx in range(n):
    tempColorCnt = 0
    for row in range(1001):
        for col in range(1001):
            if emptyMatrix[row][col] == idx+1:
                tempColorCnt += 1

    print(tempColorCnt)