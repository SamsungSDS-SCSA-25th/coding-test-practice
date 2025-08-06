# k가 미정, k개의 순열 -> 순열중에 겹치는 것? -> set에 넣고 돌리는 방법
# 백트래킹
## 순열의 visited는 항상 idx순으로 넣기

def dfs(curDepth, answer):
    global n, k, cards, visited, cnt, repeatSet
    # 가지치기 불가
    # 종료조건
    if curDepth == k:
        tempNum = int("".join(list(map(str, answer))))
        if tempNum not in repeatSet:
            # print(tempNum)
            repeatSet.add(tempNum)
            cnt += 1
        return
    # 하부재귀
    for idx in range(n):
        if not visited[idx]:
            visited[idx] = True
            dfs(curDepth + 1, answer + [cards[idx]])
            visited[idx] = False


n = int(input())
k = int(input())
cards = [ int(input()) for _ in range(n) ]

# (D) idx 순으로 검사하면, 중복되는 숫자 괜찮다
visited = [False] * n

repeatSet = set()
cnt = 0
dfs(0, [])
print(cnt)