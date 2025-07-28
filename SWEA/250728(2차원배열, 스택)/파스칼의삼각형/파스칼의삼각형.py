# 맨 앞, 맨 뒤 idx -> 무조건 1
# 그 외 idx -> 위 행의 idx-1 + idx

t = int(input())

for index in range(t):
    n = int(input())
    matrix = [ [0] * n for _ in range(n) ]


    for row in range(n):
        for col in range(n):

            for idx in range(row+1): # 행의 idx + 1 만큼 파스칼 삼각형 순열 존재
                if idx == 0 or idx == row:
                    matrix[row][idx] = 1
                else:
                    matrix[row][idx] = matrix[row-1][idx-1] + matrix[row-1][idx]

    # print(matrix)
    print(f'#{index+1}')
    for colList in matrix:
        for val in colList:
            if val == 0:
                break
            print(val, end=' ')
        print()