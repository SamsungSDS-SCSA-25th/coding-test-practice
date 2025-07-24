# max와 min의 차이 이용

for index in range(10):

    dumpNum = int(input())
    boxList = list(map(int, input().split()))

    for dump in range(dumpNum):

        minVal, maxVal = min(boxList), max(boxList)

        if (maxVal - minVal) <= 1:
            break

        boxList[boxList.index(minVal)] += 1
        boxList[boxList.index(maxVal)] -= 1

    # break문이 없으면 minVal, maxVal이 최신 값이 아니라는 점 주의
    print(f'#{index+1} {max(boxList) - min(boxList)}')