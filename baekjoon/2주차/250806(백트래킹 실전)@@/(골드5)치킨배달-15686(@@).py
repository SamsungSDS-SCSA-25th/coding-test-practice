# 백트래킹으로 어떻게 구현하지? -> 치킨집 중에 M개를 고르면 됨 조합

# 치킨집 조합을 찾았으니, 이제 거리재기
def check(chickenList):
    global homes
    # 치킨거리 최소값
    city = []
    # print(homes)
    # print(chickenList)
    for col1, row1 in homes:
        temp = []
        for col2, row2 in chickenList:
            temp.append(abs(col1-col2) + abs(row1-row2))
        # print(temp)
        city.append(min(temp))
    # 도시의 치킨거리 최소값
    # print(city)
    minCity = sum(city)
    return minCity

# 조합을 백트래킹으로 찾았으나, itertools 사용하면 더 편함
def backTracking(startIdx, curDepth, chickenList):
    global chickenCnt, answer
    # 가지치기 x
    # 종료조건
    if curDepth == M:
        # print(f'{chickenList=}')
        answer = min(answer, check(chickenList))
        return
    # 재귀
    for idx in range(startIdx, chickenCnt):
        backTracking(idx + 1, curDepth + 1, chickenList + [chickens[idx]])


N, M = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(N) ]

homes, chickens = [], []
homeCnt, chickenCnt = 0, 0
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 1:
            homes.append((col, row))
            homeCnt += 1
        elif matrix[row][col] == 2:
            chickens.append((col, row))
            chickenCnt += 1

# print(M, chickenCnt)
answer = 10**8
backTracking(0, 0, [])
print(answer)