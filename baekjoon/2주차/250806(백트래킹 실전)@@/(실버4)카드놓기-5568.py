# k가 미정, k개의 순열 -> 순열중에 겹치는 것? -> set에 넣고 돌리는 방법 -> (D) 중복제거를 최대한 활용하기
# 백트래킹
## 순열의 visited는 항상 idx순으로 넣기

def dfs(curDepth, answer):
    global n, k, cards, visited, cnt, answerSet
    # 가지치기 불가
    # 종료조건
    if curDepth == k:
        # tempNum = int("".join(list(map(str, answer))))
        # if tempNum not in repeatSet:
            # print(tempNum)
        answerSet.add("".join(list(map(str, answer)))) # (D) set은 중복되는 것 없앰. 따로 중복체크할 필요 없음
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

# (D) idx 순으로 방문행렬 검사하면, 중복되는 숫자 괜찮다
visited = [False] * n

answerSet = set()
dfs(0, [])
# print(answerSet)
cnt = len(answerSet)
print(cnt)