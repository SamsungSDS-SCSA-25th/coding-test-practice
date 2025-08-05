def dfs(curDepth, startIdx, curSum):
    global N, S, cnt, numList
    if curDepth > 0 and curSum == S: # 처음은 제외 (D) validate시점 유의
        cnt += 1

    # 위에서 마지막수까지 더한 curSum을 확인하고 밑에서 validate
    if startIdx == N: # (D) curDepth는 의미가 없음 -> 인덱스가 numList 범위내 인지체크
        return

    # print(f'{startIdx},{curDepth},{curSum}')
    for idx in range(startIdx, N):
        dfs(curDepth + 1, idx + 1, curSum + numList[idx])


N, S = map(int, input().split())
numList = list(map(int, input().split()))

cnt = 0
dfs(0,0, 0)
print(cnt)