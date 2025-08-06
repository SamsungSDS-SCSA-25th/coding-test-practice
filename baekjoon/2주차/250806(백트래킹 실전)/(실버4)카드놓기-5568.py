# k가 미정, k개의 순열 -> 순열중에 겹치는 것? -> set에 넣고 돌리는 방법
# 백트래킹
## visited 구현 다르게 하는 방법 알아두기 (아래)

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
    for card in cards:
        if visited[card] != 0:
            visited[card] -= 1
            dfs(curDepth + 1, answer + [card])
            visited[card] += 1


n = int(input())
k = int(input())
cards = [ int(input()) for _ in range(n) ]

repeatSet = set()
# card 번호가 겹칠 수 있음 -> visited 다르게 구현
visited = [0] * (99+1)
for card in cards:
    visited[card] += 1

cnt = 0
dfs(0, [])
print(cnt)