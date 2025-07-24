testNum = int(input())

for index in range(testNum):
    N, M = map(int, input().split())
    testList = list(map(int, input().split()))

    minVal = float('inf')
    maxVal = float('-inf')

    for i in range(N-(M-1)):
        tempSum = 0
        for idx in range(i, i+M):
            tempSum += testList[idx]

        minVal = min(minVal, tempSum)
        maxVal = max(maxVal, tempSum)

    print(f'#{index+1} {maxVal-minVal}')