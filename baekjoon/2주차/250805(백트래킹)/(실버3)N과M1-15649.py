# 1~n까지 숫자 사용가능
# 길이는 m -> m번 뽑는다 -> 백트래킹!

def dfs(curN, ans):
    global n, m
    if curN == m:
        if len(set(ans)) == m: # set으로 중복숫자 있는지 검증
            print(*ans)
        return

    for num in range(1, n+1):
        dfs(curN + 1, ans + [num])

n, m = map(int, input().split())
dfs(0, [])