# 돌이 있는 경우의 분기처리
# 알파벳을 인덱스 형태로 접근하기
''' #1
colList = ['A','B','C','D','E','F','G','H']
DIRECTIONS = {
    'R': (1,0), 'L': (-1,0), 'T':(0,1), 'B':(0,-1),
    'RT': (1,1), 'LB': (-1,-1), 'RB': (1,-1), 'LT': (-1,1)
} # move가 key로 사용

king, stone, n = input().split()
n = int(n)
moveList = [ input() for _ in range(n) ]

kingInfo = list(king)
kingCol, kingRow = colList.index(kingInfo[0]), int(kingInfo[1])-1
stoneInfo = list(stone)
stoneCol, stoneRow = colList.index(stoneInfo[0]), int(stoneInfo[1])-1
# print(kingCol, stoneCol)

for move in moveList:
    dx, dy = DIRECTIONS[move][0], DIRECTIONS[move][1]

    if not (0<=kingCol + dx<8 and 0<=kingRow + dy<8):
        continue

    if kingCol + dx == stoneCol and kingRow + dy == stoneRow:
        if 0<= stoneCol + dx <8 and 0<= stoneRow + dy <8: # 돌과 만나도 이동가능
            stoneCol += dx
            stoneRow += dy
        else: # 이동 자체를 안한다
            continue

    kingCol += dx
    kingRow += dy

    # print(f'{kingCol=} {kingRow=} {stoneCol=} {stoneRow=}')

print(colList[kingCol]+str(kingRow+1))
print(colList[stoneCol]+str(stoneRow+1))
'''
#2
king, stone, n = input().split()
moveList = [ input() for _ in range(int(n)) ]

directions = {
    'R': (1,0),
    'L': (-1,0),
    'B': (0,-1),
    'T': (0,1),
    'RT': (1,1),
    'LT': (-1,1),
    'RB': (1,-1),
    'LB': (-1,-1)
}
colList = list('ABCDEFGH')

kingCol, kingRow =  colList.index(list(str(king))[0]), int(list(str(king))[1])-1
stoneCol, stoneRow = colList.index(list(str(stone))[0]), int(list(str(stone))[1])-1

for move in moveList:
    dx, dy = directions[move][0], directions[move][1]

    if not (0<=kingCol + dx<8 and 0<=kingRow + dy<8): # king 범위초과
        continue

    if kingCol + dx == stoneCol and kingRow + dy == stoneRow:
        if 0<=stoneCol + dx<8 and 0<=stoneRow + dy<8:
            stoneCol += dx
            stoneRow += dy
        else:
            continue

    kingCol += dx
    kingRow += dy

print(colList[kingCol]+str(kingRow+1))
print(colList[stoneCol]+str(stoneRow+1))