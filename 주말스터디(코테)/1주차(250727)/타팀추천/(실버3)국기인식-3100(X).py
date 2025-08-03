# (1) 색상마다 구역에서 바꿔야 하는 횟수를 저장
# (2) 그다음 색상을 조합하고 총 횟수를 확인

import string
matrix = [ list(input()) for _ in range(6) ]

# 색상 찾기
colorList = []
for row in range(6):
    for col in range(9):
        colorList.append(matrix[row][col])
colorSet = set(colorList)

# 헝가리 (가로)
hungaryCost = { color: [0, 0, 0] for color in colorSet }
for idx, (startRow, endRow) in enumerate([(0,2), (2,4), (4,6)]):
    for color in colorSet:
        tempCnt = 0
        for tempRow in range(startRow, endRow):
            for tempCol in range(9):
                if matrix[tempRow][tempCol] != color:
                    tempCnt += 1
        hungaryCost[color][idx] = tempCnt

# 프랑스 (세로)
franceCost = { color: [0, 0, 0] for color in colorSet }
for idx, (startCol, endCol) in enumerate([(0,3), (3,6), (6,9)]):
    for color in colorSet:
        tempCnt = 0
        for tempCol in range(startCol, endCol):
            for tempRow in range(6):
                if matrix[tempRow][tempCol] != color:
                    tempCnt += 1
        franceCost[color][idx] = tempCnt

# 없는 색(A–Z)도 채워두기 (각 구역 전체가 전부 바뀌어야 하므로 18)
ALL_COLORS = list(string.ascii_uppercase)
for color in ALL_COLORS:
    if color not in hungaryCost:
        hungaryCost[color] = [18,18,18]
        franceCost[color] = [18,18,18]

# (color1, color2, color3) & 12 23 안겹치는 조합
minCnt = float('inf')
for color1 in colorSet:
    for color2 in ALL_COLORS:
        if color2 == color1:
            continue
        for color3 in colorSet:
            if color2 == color3:
                continue

            # 헝가리 (가로)
            tempCnt = hungaryCost[color1][0] + hungaryCost[color2][1] + hungaryCost[color3][2]
            minCnt = min(minCnt, tempCnt)

            # 프랑스 (세로)
            tempCnt = franceCost[color1][0] + franceCost[color2][1] + franceCost[color3][2]
            minCnt = min(minCnt, tempCnt)

print(minCnt)