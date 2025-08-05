# 시간초과 유의

n = int(input())
checkpointList = [ tuple(map(int, input().split())) for _ in range(n) ]

totalSum = 0
for idx in range(n-1):
    totalSum += abs(checkpointList[idx][0]-checkpointList[idx+1][0]) + abs(checkpointList[idx][1]-checkpointList[idx+1][1])

minTotalSum = float('inf')
for noIdx in range(1, n-1): # 01234 (n=5)
    temptotalSum = totalSum

    temptotalSum -= ( abs(checkpointList[noIdx-1][0] - checkpointList[noIdx][0]) + abs(checkpointList[noIdx-1][1] - checkpointList[noIdx][1]) )
    temptotalSum -= ( abs(checkpointList[noIdx][0] - checkpointList[noIdx+1][0]) + abs(checkpointList[noIdx][1] - checkpointList[noIdx+1][1]) )
    temptotalSum += ( abs(checkpointList[noIdx-1][0] - checkpointList[noIdx+1][0]) + abs(checkpointList[noIdx-1][1] - checkpointList[noIdx+1][1]) )

    minTotalSum = min(minTotalSum, temptotalSum)

print(minTotalSum)