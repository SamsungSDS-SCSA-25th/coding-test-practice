## XO
# 슬라이딩 윈도우
# 문제의 핵심은 과일이 두 종류를 초과 안됨
# 오른쪽 포인터를 이동하면서 과일을 추가하고,
# 만약 두 종류를 넘어가면 왼쪽 포인터를 이동시켜서 과일을 제거하는 방식으로 구간을 조절

''' -> 완전탐색 O(N^3) 시간초과
n = int(input())
fruitList = list(map(int, input().split()))

answerList = []
for windowSize in range(1, len(fruitList) + 1):  # 1~탕후루길이

    for startIdx in range(len(fruitList) - windowSize + 1):  # 윈도우가 시작하는 지점
        tempFruitList = []
        for curIdx in range(startIdx, startIdx + windowSize):  # 그 안에서 어디까지 가야하나
            tempFruitList.append(fruitList[curIdx])
        # print(f'{tempFruitList=}')
        if len(set(tempFruitList)) <= 2:
            answerList.append(tempFruitList)

# 맨 마지막이 가장 긴 리스트임
print(len(answerList[-1]))
'''
from os import remove

'''
# 투포인터를 활용하여 시간복잡도 O(N log N)
n = int(input())
fruitList = list(map(int, input().split()))

left = 0
fruitCntDict = {} # key: 과일종류 / value: 과일의 개수
maxLen = 0

#(1) 과일수가 2이하면, right += 1 하며 아래 논리 실행
for right in range(n):

    curFruit = fruitList[right]
    if curFruit in fruitCntDict: # 사전에 존재시 과일추가
        fruitCntDict[curFruit] += 1
    else: # 사전에 과일이 없으면
        fruitCntDict[curFruit] = 1

    #(2) 과일수가 2를 초과하여, 2를 초과하지 않을 때까지 left += 1
    while len(fruitCntDict) > 2: # 과일의 수가 2개 이상인 경우만 반복문 작동
        fruitRemove = fruitList[left]
        fruitCntDict[fruitRemove] -= 1

        if fruitCntDict[fruitRemove] == 0:
            del fruitCntDict[fruitRemove]

        left += 1

    maxLen = max(maxLen, right - left + 1)

print(maxLen)
'''
#2 -> 슬라이딩윈도우
n = int(input())
fruitList = list(map(int, input().split()))
fruitDict = {}

left = 0
maxLen = 0

for right in range(n):
    # 계속 오른쪽으로 확장하는 경우
    curFruit = fruitList[right]
    fruitDict[curFruit] = fruitDict.get(curFruit, 0) + 1

    # 과일 개수가 2개를 초과하면 왼쪽 축소
    while len(fruitDict) > 2:
        removeFruit = fruitList[left]
        fruitDict[removeFruit] -= 1
        if fruitDict[removeFruit] == 0:
            del fruitDict[removeFruit]
        left += 1

    maxLen = max(maxLen, right - left + 1)
    # 2개 이상이면 다시 오른쪽으로 확장하러

print(maxLen)