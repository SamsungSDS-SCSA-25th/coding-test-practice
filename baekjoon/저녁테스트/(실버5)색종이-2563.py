
n = int(input())
paperMatrix = [ [0] * 100 for _ in range(100) ]
for _ in range(n):
    x, y = map(int, input().split())
    for row in range(y,y+10):
        for col in range(x,x+10):
            paperMatrix[row][col] = 1

cnt = 0
for row in range(100):
    for col in range(100):
        if paperMatrix[row][col] == 1:
            cnt += 1

print(cnt)