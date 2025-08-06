# 두문제 이상 부분집합
## 부분 집합은 visited가 필요하지 않다. -> 순열만 visited 필요 (순서)
''' #1
def dfs(curIdx, curSum, ans):
    global N, L, R, X, cnt
    if curIdx == N: # (D) 무조건 종료해야 하는 경우
        if L <= curSum <= R and len(ans) >= 2:
            tempList = []
            for idx in ans:
                tempList.append(problemList[idx])
            if max(tempList) - min(tempList) >= X:
                # print(tempList)
                cnt += 1
        return

    # (D) 부분집합 공식 -> visited가 필요하지 않다 -> 순서가 중요하지 않기 때문 -> 나중에 return으로 재귀
    dfs(curIdx + 1, curSum, ans)
    dfs(curIdx + 1, curSum + problemList[curIdx], ans+[curIdx])

N, L, R, X = map(int, input().split())
problemList = list(map(int, input().split()))

cnt = 0
dfs(0, 0, [])
print(cnt)
'''
#2 -> 캠프 문제수에 제한이 없으므로 부분집합 백트래킹
def backTracking(curDepth, lst):
    global probCnt
    # 종료조건
    if curDepth == N: # 무조건 종료해야 하는 조건
        # print(lst)
        if (len(lst) >= 2 and L <= sum(lst) <= R and max(lst) - min(lst) >= X): # 조건부 조건
            # print(lst)
            probCnt += 1
        return
    # 재귀 -> 부분집합
    backTracking(curDepth+1, lst)
    backTracking(curDepth+1, lst+[hardList[curDepth]])


N, L, R, X = map(int, input().split())
hardList = list(map(int, input().split()))

probCnt = 0
backTracking(0, [])
print(probCnt)