t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    matrix = [ list(map(int, input().split())) for _ in range(n) ]
    matrixT = list(map(list, zip(*matrix)))

    colMultiList = []
    for idx, rowList in enumerate(matrixT):
        tempMulti = 1
        for row in rowList:
            tempMulti *= row
        colMultiList.append((idx, tempMulti))

    colMultiList.sort(key=lambda x: (-x[1], -x[0]))
    print(colMultiList[0][0]+1)