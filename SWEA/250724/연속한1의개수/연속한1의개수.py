T = int(input())

for index in range(T):

    N = int(input())
    testList = list(map(int, list(input())))

    maxCnt, cnt = 0, 0
    for idx, test in enumerate(testList):
        if test == 0:
            maxCnt = max(maxCnt, cnt)
            cnt = 0
        elif test == 1:
            cnt += 1

        if idx == len(testList) - 1:
            maxCnt = max(maxCnt, cnt)

    print(f'#{index+1} {maxCnt}')