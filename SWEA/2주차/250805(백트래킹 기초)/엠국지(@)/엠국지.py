def dfs(n, startIdx, curSum):
    global powerList, powerSum, countryCnt
    #1 종료조건
    if n == selectN: # -> m국이 되었을때 종료
        if curSum == powerSum: # -> 국력의합이 같은지 확인
            # print(f'{curSum=}')
            countryCnt += 1
        return

    #2 하부재귀
    for startIdx in range(startIdx, countryN): # (D) 회귀 돌때마다 idx+1씩 올라가서 start도 증가함
        dfs(n + 1, startIdx + 1, curSum + powerList[startIdx])

    return countryCnt


tc = int(input())
for i in range(1, tc+1):
    countryN, selectN, powerSum = map(int, input().split())
    powerList = list(map(int, input().split()))
    countryCnt = 0

    print(f'#{i}', end=' ')
    dfs(0, 0, 0)
    print(countryCnt)