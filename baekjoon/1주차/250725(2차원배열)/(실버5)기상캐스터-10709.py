# flag를 이용하여 -1인지 양수인지를 구분하고 시작

h, w = map(int, input().split())
cloudMatrix = [ list(input()) for _ in range(h) ]
numberMatrix = [ [0] * w for _ in range(h) ]

for row in range(h):
    flag = False
    cloudCnt = 0
    for col in range(w):
        if flag == False:
            numberMatrix[row][col] = -1

        if cloudMatrix[row][col] == 'c':
            flag = True
            numberMatrix[row][col] = 0
            cloudCnt = 0
        elif flag == True: # c는 아니지만 flag가 True인 경우
            cloudCnt += 1
            numberMatrix[row][col] = cloudCnt

for row in range(h):
    for col in range(w):
        print(numberMatrix[row][col], end=' ')
    print()