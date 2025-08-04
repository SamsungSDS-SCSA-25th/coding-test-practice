# 색이 겹치지 않는다고 명시 -> 값이 2면 count

t = int(input())

for index in range(t):
    n = int(input())
    colorList = [ list(map(int, input().split())) for _ in range(n) ]
    emptyMatrix = [ [0] * 10 for _ in range(10) ]

    for info in colorList:
        colorType = info[-1]
        x1, y1, x2, y2 = info[0], info[1], info[2], info[3]

        for row in range(y1, y2+1):
            for col in range(x1, x2+1):
                emptyMatrix[row][col] += 1
    purpleCnt = 0
    for row in range(10):
        for col in range(10):
            if emptyMatrix[row][col] == 2:
                purpleCnt += 1

    print(f'#{index+1} {purpleCnt}')