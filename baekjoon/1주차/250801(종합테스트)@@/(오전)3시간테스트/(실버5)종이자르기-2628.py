# 구역저장하기 -> 각 행열을 오름차순으로 넘어가면서 간격이 가장큰 값 업데이트
# 가장 간격이 큰 값의 곱이 답이다

m, n = map(int, input().split())
k = int(input())
infoList = [ tuple(map(int, input().split())) for _ in range(k) ]

rowList = []
colList = []
for info in infoList:
    if info[0] == 0:
        rowList.append(info[1])
    elif info[0] == 1:
        colList.append(info[1])

rowList.sort()
colList.sort()
rowList.append(n)
colList.append(m)
maxRowLen = 0
for idx, row in enumerate(rowList):
    if idx == 0:
        maxRowLen = row
        continue

    rowLen = rowList[idx] - rowList[idx-1]
    maxRowLen = max(maxRowLen, rowLen)

maxColLen = 0
for idx, col in enumerate(colList):
    if idx == 0 and not idx == len(colList)-1:
        maxColLen = col
        continue

    colLen = colList[idx] - colList[idx - 1]
    maxColLen = max(maxColLen, colLen)

print(maxRowLen * maxColLen)