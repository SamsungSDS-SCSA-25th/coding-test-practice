# 둘레의 길이 구하는 아이디어?
## dxdy 기법으로 1의 값을 가지고 있으면서, 4방향 중 하나라도 0이거나 외곽이면 카운트

moveList = [(1,0),(0,1),(-1,0),(0,-1)]

n = int(input())
paperMatrix = [ [0]*100 for _ in range(100) ]
for _ in range(n):
    x, y = map(int, input().split())
    for row in range(y,y+10):
        for col in range(x,x+10):
            paperMatrix[row][col] += 1

cnt = 0
for row in range(100):
    for col in range(100):
        if paperMatrix[row][col] >= 1: # (D) 2개 이상 겹친 부분도 둘레가 될 수 있었음
            for dx, dy in moveList:
                nxtCol, nxtRow = col + dx, row + dy
                if nxtCol < 0 or nxtCol >= 100 or nxtRow < 0 or nxtRow >= 100 or paperMatrix[nxtRow][nxtCol] == 0: # 테두리 확인
                    cnt += 1

print(cnt)