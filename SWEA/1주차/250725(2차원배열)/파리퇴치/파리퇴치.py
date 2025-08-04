# 시작점을 반복문으로 만들고
# 그 시작점에서 시작하는 파리채 내의 원소를 반복문으로 찾고 더해주면 됨

t = int(input())

for index in range(t):
    n, m = map(int, input().split())
    matrixOrigin= [ list(map(int, input().split())) for _ in range(n) ]
    #print(matrixOrigin)
    maxSum = 0
    for y in range(n-m+1): # 시작점 y좌표
        for x in range(n-m+1): # 시작점 x좌표
            tempSum = 0
            for ry in range(y, y+m):
                for rx in range(x, x+m):
                    tempSum += matrixOrigin[ry][rx]
                    maxSum = max(maxSum, tempSum)

    print(f'#{index+1} {maxSum}')