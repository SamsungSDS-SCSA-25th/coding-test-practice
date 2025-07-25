# index의 범위 주의하자...
# maxSquare와 length 같은 초기화하는 문장 위치 주의...
# 어디서 틀렸는지 모르겠으면 종이에 반복문 돌려보기

n, m = map(int, input().split())
numMatrix = [ list(map(int, list(input()))) for _ in range(n) ]

maxSquare = 0
for row in range(n): # 좌표하나 선택
    for col in range(m):
        length = 0 # 초기화
        while True: # 정사각형 확장
            if row + length == n or col + length == m: # 범위 탈출 시 중단
                break
            if numMatrix[row][col] == numMatrix[row][col+length] == numMatrix[row+length][col] == numMatrix[row+length][col+length]:
                #print(f'{length=}, {maxSquare=}')
                maxSquare = max(maxSquare, ((length+1) * (length+1)))
            length += 1

print(maxSquare)