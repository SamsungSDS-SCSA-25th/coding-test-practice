''''
infoMatrix = [ list(input().split()) for _ in range(9) ]
print(infoMatrix)

middleGoalList = []
detailGoalList = []
for row in range(9): # 하나씩 선정
    for col in range(9):
        if row == 4 and col == 4: # 최종목표는 생략 -> validate 맨 처음
            continue # (D) break가 아님 유의
        tempCnt = 0
        for tempRow in range(9): # 행렬 순회
            for tempCol in range(9):
                if infoMatrix[row][col] == infoMatrix[tempRow][tempCol]:
                    tempCnt += 1

        #if infoMatrix[][col] == 'm4':
         #   print('M4')

        if tempCnt == 2: # 2번 나왔으면
            middleGoalList.append(infoMatrix[row][col])
        elif tempCnt == 1: # 1번 나왔으면
            detailGoalList.append(infoMatrix[row][col])

middleGoalList = sorted(list(set(middleGoalList))) # 중간목표 중복제거 + 사전순 정렬
### (D) 대소, 숫자 우선순위는 이후 디버깅 !!!
print(f'{middleGoalList=}')

detailGoalList = sorted(detailGoalList)
print(f'{detailGoalList=}')

###################
for middleGoalIdx, middleGoal in enumerate(middleGoalList):
    print(f'#{middleGoalIdx + 1}. {middleGoal}')
    tempIdx = 0
    for detailGoalIdx in range(middleGoalIdx*8, (middleGoalIdx*8) + 8):
        detailGoal = detailGoalList[detailGoalIdx]
        print(f'#{middleGoalIdx + 1}-{tempIdx + 1}. {detailGoal}')
        tempIdx += 1
'''

### 세부목표를 전부 가지고 사전식으로 정렬하는줄 알고 착각...
### 다시 코드 짜다가 중도 실패
# 사전형으로 짜기

infoMatrix = [ list(input().split()) for _ in range(9) ]

middleDetailDict = {}
for row in range(0, 9, 3):
    for col in range(0, 9, 3):
        if row == 3 and col == 3: # 최종목표 있는 행렬 생략
            continue
        tempDetailList = []
        for tempRow in range(3):
            for tempCol in range(3):
                if tempRow == 1 and tempCol == 1: # 가운데 것은 중간목표
                    key = infoMatrix[row+tempRow][col+tempCol]
                else:
                    tempDetailList.append(infoMatrix[row+tempRow][col+tempCol])

        tempDetailList.sort()
        middleDetailDict[key] = tempDetailList

#print(f'{middleDetailDict=}')
sortedMiddleDetailDict = {}
for key in sorted(middleDetailDict): # 사전형을 sorted하면 오름차순 keyList 반환
    sortedMiddleDetailDict[key] = middleDetailDict[key]
#print(f'{sortedMiddleDetailDict=}')

for keyIdx, key in enumerate(sortedMiddleDetailDict.keys()):
    print(f'#{keyIdx+1}. {key}')
    for valueIdx, value in enumerate(sortedMiddleDetailDict[key]):
        print(f'#{keyIdx+1}-{valueIdx+1}. {value}')