def dfs(n, ans):
    global N, rollSum
    #1 종료조건
    if n == N: # 무조건 종료하는 상황
        # print(f'{ans=} {rollSum=}')
        if sum(ans) == rollSum: # 그중에서 출력해야하는 상황
            print(*ans)
        return

    for rollIdx in range(1, 7):
        dfs(n+1, ans+[rollIdx])

##########################

tc = int(input())
for i in range(1, tc+1):
    N, rollSum = map(int, input().split())

    print(f'#{i}')
    dfs(0, [])