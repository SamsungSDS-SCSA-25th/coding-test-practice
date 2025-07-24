paperNum, overlapPaper = map(int, input().split())
xyxyMatrix = [ list(map(int, input().split())) for i in range(paperNum) ]

matrixOrigin = [ [0] * 100 for _ in range(100) ]
for xyxyList in xyxyMatrix:
    # 모든 좌표는 100보다 작거나 같은 자연수이다...
    x1, y1 = int(xyxyList[0]), int(xyxyList[1])
    x2, y2 = int(xyxyList[2]), int(xyxyList[3])
    for row in range(y1-1, y2): # 좌표계에서 일관적으로 1을 내려줘야 함 -> 3x3 그림 그려서 색을 점으로 저장한다고 생각해봐!
        for col in range(x1-1, x2): # 위 동
            matrixOrigin[row][col] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if matrixOrigin[i][j] > overlapPaper:
            cnt += 1

if paperNum == 0:
    print(0)
else:
    print(cnt)