# 두문제 이상 부분집합
## 부분 집합은 visited가 필요하지 않다. -> 순열만 visited 필요 (순서)

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