paperNum, overlapPaper = map(int, input().split())
xyxyMatrix = [ list(map(int, input().split())) for i in range(paperNum) ]

matrixOrigin = [ [0] * 100 for _ in range(100) ]
for xyxyList in xyxyMatrix:
    x1, y1 = int(xyxyList[0]), int(xyxyList[1])
    x2, y2 = int(xyxyList[2]), int(xyxyList[3])
    for row in range(y1, y2+1):
        for col in range(x1, x2+1):
            matrixOrigin[row][col] += 1

#print(matrixOrigin)
#print(m)

cnt = 0
for i in range(100):
    for j in range(100):
        if matrixOrigin[i][j] > overlapPaper:
            cnt += 1

if paperNum == 0:
    print(0)
else:
    print(cnt)