n, m = map(int, input().split())
matrixOrigin = [ list(input()) for _ in range(n) ]

#print(matrixOrigin)
minCnt = float('inf')
for row in range(n-7):
    for col in range(m-7):
        blackColor = 0
        whiteColor = 0
        for tempRow in range(row, row+8):
            for tempCol in range(col, col+8):
                tempRowColSum = tempRow + tempCol
                #print(f'{tempRowColSum=} {tempRow=} {tempCol=}')

                if ( tempRowColSum % 2 == 1 and matrixOrigin[tempRow][tempCol] == 'B' ) or (
                        tempRowColSum % 2 == 0 and matrixOrigin[tempRow][tempCol] == 'W' ):
                    blackColor += 1
                    #print(f'{blackColor=}')

                elif (tempRowColSum % 2 == 1 and matrixOrigin[tempRow][tempCol] == 'W') or (
                        tempRowColSum % 2 == 0 and matrixOrigin[tempRow][tempCol] == 'B'):
                    whiteColor += 1
                    #print(f'{whiteColor=}')

        minCnt = min(minCnt, blackColor, whiteColor)

print(minCnt)