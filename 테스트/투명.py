n, m = map(int, input().split())
xyxyList = [ list(map(int, input().split())) for i in range(n) ]

matrixOrigin = [ [0] * 100 for i in range(100) ]
for xyxyArr in xyxyList:
    x1, y1 = int(xyxyArr[0]), int(xyxyArr[1])
    x2, y2 = int(xyxyArr[2]), int(xyxyArr[3])
    #distanceRow = int(xyxyArr[3]) - int(xyxyArr[1])
    #distanceCol = int(xyxyArr[2]) - int(xyxyArr[0])
    for row in range(y1, y2+1):
        for col in range(x1, x2+1):
            matrixOrigin[row][col] += 1

#print(matrixOrigin)
#print(m)


cnt = 0
for i in range(100):
    for j in range(100):
        if matrixOrigin[i][j] > m:
            cnt += 1
if n == 0:
    print(0)
else:
    print(cnt)