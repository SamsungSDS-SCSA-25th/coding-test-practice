# 가장 낮은 탑이니 가지치기해야함
def dfs(curDepth, startIdx, curSum):
    global heightList, minSum
    # 가지치기
    if minSum < curSum:
        return

    # 종료조건
    if curSum >= topH:
        minSum = min(minSum, curSum)
        return

    for idx in range(startIdx, N):
        dfs(curDepth+1, idx+1, curSum+heightList[idx])

tc = int(input())
for i in range(1, tc+1):
    N, topH = map(int, input().split())
    heightList = list(map(int, input().split()))
    minSum = float('inf')

    print(f'#{i}', end=' ')
    dfs(0, 0, 0)
    print(minSum-topH)