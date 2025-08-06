# 경우의수가 많으므로 백트래킹 -> 순열도 조합도 부분집합도 아님
# visited를 써서 백트래킹의 기록을 남기고 이동한다. ???
### 아이디어 기억하기!!!

def dfs(curDay, curProfit):
    global dayPriceList, N, maxSum, visited
    # 가지치기 x
    # 종료조건 -> 2가지
    if curDay >= N:
        if curProfit > maxSum:
            maxSum = curProfit
        return

    ### 아이디어 꼭 기억하기 -> 백트래킹의 특징을 최대한 이용 (컴퓨터입장에서 백트래킹 생각해보기)
    # 일을 안한다고 분기
    dfs(curDay+1, curProfit)

    # 일을 한다고 분기
    period, profit = dayPriceList[curDay]
    if not visited[curDay] and curDay + period <= N: # (D) N과 같은 경우는 N에서 1일짜리 할때
        visited[curDay] = True
        dfs(curDay + period, curProfit + profit)
        visited[curDay] = False


N = int(input())
dayPriceList = []
for curDay in range(N): # 0~N-1 (D) 이상한 조건 넣지말고 정석으로 가자
    day, price = map(int, input().split())
    dayPriceList.append((day, price))
# print(dayPriceList)

visited = [False] * N

maxSum = 0
dfs(0, 0)
print(maxSum)