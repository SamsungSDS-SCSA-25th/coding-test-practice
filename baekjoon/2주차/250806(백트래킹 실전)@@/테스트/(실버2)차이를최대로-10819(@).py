# 순열(최댓값) -> 백트래킹

def dfs(curDepth, lst):
    global numList, visited, N, maxSum
    # 최댓값이라 가지치기 불가능
    if curDepth == N:
        # print(lst)
        tempSum = 0
        for idx in range(N-1):
            tempSum += abs(lst[idx] - lst[idx+1])
        if tempSum > maxSum:
            maxSum = tempSum
        return

    for idx in range(N):
        if not visited[idx]:
            visited[idx] = True
            dfs(curDepth + 1, lst+[numList[idx]])
            visited[idx] = False


N = int(input())
numList = list(map(int, input().split()))

maxSum = 0
visited = [False] * N
dfs(0, [])
print(maxSum)