# 같은 숫자는 중복되지 않는다.

def dfs(curDepth, answer):
    global n
    if curDepth == n:
        if len(set(answer)) == n: # 중복방지 set
            print(*answer)
        return

    for num in range(1, n+1):
        dfs(curDepth + 1, answer + [num])

n = int(input())
dfs(0, [])