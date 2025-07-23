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