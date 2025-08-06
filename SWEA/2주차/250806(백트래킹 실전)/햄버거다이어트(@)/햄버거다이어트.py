# 민기가 좋아하는 햄버거의 최적의 조합
# 칼로리 상한 아래에서, 가장 점수가 높은 햄버거 찾기
# 조합 -> 백트래킹

def dfs(curCalSum, curScoreSum, startIdx):
    global scoreCalList, N, minCal, maxScore
    # 가지치기
    if curCalSum >= minCal:
        return

    maxScore = max(maxScore, curScoreSum)  # N개가 꼭 아니어도 되므로, 계속 maxScore 갱신

    # 종료조건
    if startIdx == N: # 조합은 idx가 5(범위초과)를 도달하면 끝!
        # print(f'{maxScore=}')
        return

    # 하부재귀
    for idx in range(startIdx, N): # 조합에 대한 알고리즘
        dfs(curCalSum + scoreCalList[idx][1], curScoreSum + scoreCalList[idx][0], idx + 1)


tc = int(input())
for i in range(1, tc+1):
    N, minCal = map(int, input().split())
    scoreCalList = [ tuple(map(int, input().split())) for _ in range(N) ]

    maxScore = 0
    dfs(0, 0, 0)

    print(f'#{i} {maxScore}')