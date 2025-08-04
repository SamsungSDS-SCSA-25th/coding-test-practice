n, m = map(int, input().split())
aMatrix =  [ list(map(int, input().split())) for _ in range(n) ]
m, k = map(int, input().split())
bMatrix = [ list(map(int, input().split())) for _ in range(m) ]
bMatrixT = list(map(list, zip(*bMatrix)))
ansMatrix = [ [0]*k for _ in range(n) ]

for row in range(n):

    for tempRow in range(k):
        for tempCol in range(m):
            ansMatrix[row][tempRow] += aMatrix[row][tempCol] * bMatrixT[tempRow][tempCol]

        # print(ansMatrix[row][col])

for row in range(n):
    for col in range(k):
        print(ansMatrix[row][col], end=' ')
    print()