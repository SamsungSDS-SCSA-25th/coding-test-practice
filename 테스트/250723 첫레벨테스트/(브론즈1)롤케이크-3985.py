'''
cakeLength = int(input())
people = int(input())
sizeList = [ list(map(int, input().split())) for _ in range(people) ]

cakeStatusList = [0] * cakeLength
thinkEatCakeList = []
realEatCakeList = [0] * people

for personIdx, personSize in enumerate(sizeList): # 원소가 리스트 형태로 나오더라도 enumerate 사용가능
    start, end = personSize[0], personSize[1]
    thinkEatCakeList.append(end - start)
    #print(thinkEatCakeList)
    for cakeIdx in range(start, end+1):
        if cakeStatusList[cakeIdx - 1] == 0:
            realEatCakeList[personIdx] += 1
            cakeStatusList[cakeIdx - 1] += 1


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
'''

# 변수명 길이를 줄여라 -> 예영 프로님 조언

cakeLength = int(input())
people = int(input())
sizeList = [ list(map(int, input().split())) for _ in range(people) ]

cakeList = [0] * cakeLength
thinkList = []
realList = [0] * people

for personIdx, personSize in enumerate(sizeList): # 원소가 리스트 형태로 나오더라도 enumerate 사용가능

    start, end = personSize[0], personSize[1]

    thinkList.append(end - start)

    for cakeIdx in range(start, end+1):
        if cakeList[cakeIdx - 1] == 0:
            realList[personIdx] += 1
            cakeList[cakeIdx - 1] += 1

# .index() 는 동일한 것이 있을 경우 맨 앞에 것을 출력
maxThink = max(thinkList)
maxReal = max(realList)
print(thinkList.index(maxThink) + 1) # ok
print(realList.index(maxReal) + 1) # ok