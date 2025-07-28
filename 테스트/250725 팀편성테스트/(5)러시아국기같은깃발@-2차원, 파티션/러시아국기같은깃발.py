# O
# 행을 기준으로 경계선을 이용 -> 조합이 아님
# 각 행리스트에서 바꿔야 할 숫자 카운트 -> 최소 구하기

'''
t = int(input())

for index in range(t):
    n, m = map(int, input().split())
    infoMatrix = [ list(input()) for _ in range(n) ]
    # print(infoMatrix)

    minCnt = float('inf')
    for wbBorder in range(0, n-2):
        for brBorder in range(wbBorder+1, n-1):
            tempCnt = 0
            # white 검색
            for whiteRowIdx in range(0, wbBorder+1):
                for info in infoMatrix[whiteRowIdx]:
                    if info != 'W':
                        tempCnt += 1
            # blue 검색
            for blueRowIdx in range(wbBorder+1, brBorder+1):
                for info in infoMatrix[blueRowIdx]:
                    if info != 'B':
                        tempCnt += 1
            # red 검색
            for redRowIdx in range(brBorder+1, n):
                for info in infoMatrix[redRowIdx]:
                    if info != 'R':
                        tempCnt += 1

            minCnt = min(minCnt, tempCnt)

    print(f'#{index+1} {minCnt}')
'''

# 파티션을 활용해서 W,B,R 구역정하기 for문 2번

t = int(input())

for index in range(t):
    n, m = map(int, input().split())
    infoMatrix = [ list(input()) for _ in range(n) ]
    print(infoMatrix)