# 민기가 좋아하는 햄버거의 최적의 조합
# 칼로리 상한 아래에서, 가장 점수가 높은 햄버거 찾기
# 조합 -> 백트래킹
### 조합 말고,,, 부분집합으로 풀자...

def dfs(curCalSum, curScoreSum, curIdx):
    global scoreCalList, N, minCal, maxScore
    # 가지치기
    if curCalSum >= minCal:
        return

    # 종료조건
    if curIdx == N: # idx가 5(범위초과)를 도달하면 끝!
        maxScore = max(maxScore, curScoreSum)
        # print(f'{maxScore=}')
        return

    # 하부재귀 -> 부분집합 알고리즘 (암기!)
    dfs(curCalSum, curScoreSum, curIdx + 1) # curIdx에서 갱신없음 (안고름)
    dfs(curCalSum + scoreCalList[curIdx][1], curScoreSum + scoreCalList[curIdx][0], curIdx + 1) # curIdx에서 갱신 (고름)


tc = int(input())
for i in range(1, tc+1):
    N, minCal = map(int, input().split())
    scoreCalList = [ tuple(map(int, input().split())) for _ in range(N) ]

    maxScore = 0
    dfs(0, 0, 0)

    print(f'#{i} {maxScore}')