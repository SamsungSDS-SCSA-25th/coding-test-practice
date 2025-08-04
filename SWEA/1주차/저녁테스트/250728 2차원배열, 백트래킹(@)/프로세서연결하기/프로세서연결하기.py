# 뭔가 최단거리를 구하는 알고리즘이 있을 것으로 생각함
# bfs? -> 백트래킹 잘모름

t = int(input())

# 북,동,남,서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
'''
for index in range(t):
    n = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(n) ]
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 1:
                if row == 0 or row == n-1 or col == 0 or col == n-1:
                    continue # break 아님 유의

                while True:
                    for
'''
