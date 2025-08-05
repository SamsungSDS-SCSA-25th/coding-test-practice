def dfs(curDepth, answer):
    global n, m
    if curDepth == m:
        if len(set(answer)) == m:
            print(*answer)
        return

    for num in range(1, n + 1):
        if answer and num > answer[-1]: # 앞 숫자보다 클때만 dfs도는 validate
            dfs(curDepth + 1, answer + [num])
        elif not answer: # 첫 출발
            dfs(curDepth + 1, answer + [num])

n, m = map(int, input().split())
dfs(0, [])
