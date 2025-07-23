cakeLength = int(input())
people = int(input())
sizeList = [ list(map(int, input().split())) for _ in range(people) ]

cakeSituList = [0] * cakeLength
thinkEatCakeList = []
realEatCakeList = [0] * people

for personIdx, personSize in enumerate(sizeList):
    start, end = personSize[0], personSize[1]
    thinkEatCakeList.append(end - start)
    #print(thinkEatCakeList)
    for cakeIdx in range(start, end+1):
        if cakeSituList[cakeIdx - 1] == 0:
            realEatCakeList[personIdx] += 1
            cakeSituList[cakeIdx - 1] += 1


#print(cakeSituList) # ok
#print(thinkEatCakeList) # ok
#print(realEatCakeList) # ok

maxThinkEatCake = max(thinkEatCakeList)
maxRealEatCake = max(realEatCakeList)
if thinkEatCakeList.count(maxThinkEatCake) > 1:
    #print(thinkEatCakeList.pop(thinkEatCakeList.index(maxThinkEatCake)) + 1)
    for idx, eatCake in enumerate(thinkEatCakeList):
        if eatCake == maxThinkEatCake:
            print(idx + 1)
            break
else:
    print(thinkEatCakeList.index(maxThinkEatCake) + 1) # ok
if realEatCakeList.count(maxRealEatCake) > 1:
    #print(realEatCakeList.pop(realEatCakeList.index(maxRealEatCake)) + 1)
    for idx, eatCake in enumerate(realEatCakeList):
        if eatCake == maxRealEatCake:
            print(idx + 1)
            break
else:
    print(realEatCakeList.index(maxRealEatCake) + 1) # ok
