N, targetL = map(int, input().split())
signInfo = [ list(map(int, input().split())) for _ in range(N) ] # D R G

signDict = {}
for sign in signInfo:
    tempList = []
    for _ in range(sign[1]):
        tempList.append('R')
    for _ in range(sign[2]):
        tempList.append('G')
    signDict[sign[0]] = tempList
# print(signDict)

sec, move = 0, 0
while True:
    if move == targetL:
        break

    if move in list(signDict.keys()): # 신호등과 만날때
        if signDict[move][sec % len(list(signDict[move]))] == 'R': # 기다려야 하는 경우
            sec += 1
        elif signDict[move][sec % len(list(signDict[move]))] == 'G': # 신호등 통과
            sec += 1
            move += 1
    else: # 신호등 안만나면
        sec += 1
        move += 1

print(sec)