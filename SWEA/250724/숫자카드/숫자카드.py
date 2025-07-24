n = int(input())

for index in range(n):
    testNum = int(input())
    testList = list(map(int, list(input())))
    testCountList = [0] * 10
    for test in testList:
        testCountList[test] += 1

    maxCount = max(testCountList)
    #print(maxCount)
    #print(testCountList
    indexList = []
    for num, count in enumerate(testCountList):
        #print(count)
        if count == maxCount:
            indexList.append(num)

    maxNum = indexList[-1]

    print(f'#{index+1} {maxNum} {maxCount}')