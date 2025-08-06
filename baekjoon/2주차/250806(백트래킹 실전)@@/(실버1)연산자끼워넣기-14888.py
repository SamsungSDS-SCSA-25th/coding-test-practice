# 순열 -> 백트래킹 / 연산자를 일단 순열형태로 펼쳐놓는다 ->(종료조건) 연산 후 결과를 확인 후, 최대 최소를 구분한다.
# visited 필요함

def newDivide(a, b):
    return int(a / b)

def dfs(curDepth, lst):
    global numList, N, visited, minCal, maxCal
    # 가지치기 x
    # 종료조건
    if curDepth == N-1:
        # print(f'{lst=}')
        tempCal = 0
        for numIdx in range(N-1):
            if numIdx == 0:
                if lst[numIdx] == 0: # +
                    tempCal = numList[numIdx] + numList[numIdx+1]
                elif lst[numIdx] == 1: # -
                    tempCal += numList[numIdx] - numList[numIdx+1]
                elif lst[numIdx] == 2: # *
                    tempCal += numList[numIdx] * numList[numIdx+1]
                elif lst[numIdx] == 3: # /
                    tempCal += newDivide(numList[numIdx], numList[numIdx+1])
                continue

            if lst[numIdx] == 0:  # +
                tempCal += numList[numIdx + 1]
            elif lst[numIdx] == 1:  # -
                tempCal -= numList[numIdx + 1]
            elif lst[numIdx] == 2:  # *
                tempCal *= numList[numIdx + 1]
            elif lst[numIdx] == 3:  # /
                tempCal = newDivide(tempCal, numList[numIdx + 1])

        # print(f'{numIdx=} {tempCal=}')
        minCal = min(tempCal, minCal)
        maxCal = max(tempCal, maxCal)
        return

    # 하부재귀
    for idx in range(N-1):
        if not visited[idx]:
            visited[idx] = True
            dfs(curDepth + 1, lst + [opList[idx]])
            visited[idx] = False


N = int(input())
numList = list(map(int, input().split()))
ops = list(map(int, input().split()))
# ops 펼치기 -> 0: + | 1: - | 2: * | 3: /
opList = []
for idx, op in enumerate(ops):
    for _ in range(op):
        opList.append(idx)
# print(opList)

minCal, maxCal = float('inf'), float('-inf')
visited = [False] * (N)

dfs(0, [])

print(maxCal)
print(minCal)
# print(newDivide(-1, 3))