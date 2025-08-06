# 500이상 유지조건
# N개의 운동키트 N일 동안 -> 어떤순서로 사용할지? -> 순열
# 운동 기간동안 항상 중량이 500 이상이 되도록 하는 경우의 수
# 이 때 몇몇 운동 키트들의 중량 증가량이 같을 수 있으나, 서로 다른 운동 키트로 간주한다.

def dfs(curDay, curWeight):
    # print(f'{curDay=}, {curWeight=}')
    global visited, kitList, N, cnt, K
    # 가지치기
    if curWeight < 500:
        return
    # 종료조건
    if curDay == N and curWeight >= 500:
        # print(curWeight)
        cnt += 1
        return
    # 하부재귀
    for idx in range(N): # idx기준으로 방문행렬 방문위함
        # print(f'{weight=}, {curDay=}, {curWeight=}')
        if not visited[idx]:
            visited[idx] = True
            dfs(curDay + 1, curWeight - K +  kitList[idx]) # (D) K 로 변경
            visited[idx] = False


N, K = map(int, input().split())
kitList = list(map(int, input().split())) # N개
# print(kitList)

# (D) 중복되는 숫자라고 하더라도, idx기준으로 관리하면 됨
visited = [False] * N

cnt = 0
dfs(0, 500)
print(cnt)