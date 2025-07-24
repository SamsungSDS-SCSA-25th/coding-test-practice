'''
mushroomsScoreList = [ int(input()) for _ in range(10) ]

tempSum = 0
for idx, mushroomsScore in enumerate(mushroomsScoreList):
    tempSum += mushroomsScore
    if tempSum == 100:
        print(tempSum)
        break
    if tempSum > 100:
        if abs(tempSum - 100) > abs(tempSum - mushroomsScore - 100):
            print(tempSum - mushroomsScore)
            break
        elif abs(tempSum - 100) <= abs(tempSum - mushroomsScore - 100):
            print(tempSum)
            break

if tempSum < 100:
    print(tempSum)
'''

mushroomsScoreList = [ int(input()) for _ in range(10) ]

tempSum = 0
for mushroomScore in mushroomsScoreList:

    tempSum += mushroomScore

    if tempSum == 100:
        print(tempSum)
        break

    if tempSum > 100: # 반복문 수행중, 100이 넘어가면 앞 뒤 체크 (절댓값 이용)
        if abs(tempSum - 100) > abs(tempSum - mushroomScore - 100):
            print(tempSum - mushroomScore)
            break
        elif abs(tempSum - 100) <= abs(tempSum - mushroomScore - 100):
            print(tempSum)
            break

if tempSum < 100: # 반복문 수행이후 100이 안남는 경우 리스트총합이 100과 가장 가까움
    print(tempSum)