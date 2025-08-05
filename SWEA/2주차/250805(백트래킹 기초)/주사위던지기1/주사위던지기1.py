def dfs(n, ans):
    # [1] 종료조건
    if n == targetN:
        print(*ans) # 정답처리는 무조건 종료시점에!!!
        return # 무조건 끝나야함

    # [2] 하부함수호출(재귀), 필요한 파라미터 추가
    for rollIdx in range(1, 7): # 주사위
        dfs(n+1, ans+[rollIdx])


#################################################################
# 범위 밖이면 이것을 해라 정도 -> bfs에서 많이 사용
def oob(i, j):
    return not 0<=i<N and 0<=j<N
#################################################################

tc = int(input())
for i in range(1, tc+1):
    targetN = int(input())

    print(f'#{i}')
    dfs(0, []) # n, ans
    print()