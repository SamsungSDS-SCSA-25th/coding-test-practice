# 윈도우 슬라이딩 하면 될 것 같음
# 긴 리스트, 짧은 리스트를 나누고 Index도 나누어줌
### 어디서 꼬인지 모르겠으면, 우선 오타부터 찾아보고, 그 다음에 하나씩 출력해보자

t = int(input())

for index in range(t):
    n, m = map(int, input().split())
    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))

    longList, shortList = [], []
    if len(aList) >= len(bList):
        longList, shortList = aList, bList
    elif len(aList) < len(bList):
        longList, shortList = bList, aList

    maxSum = 0
    for idx in range(len(longList)-len(shortList)+1): # 총 횟수
        tempSum = 0
        shortIdx = 0
        for i in range(idx, idx+len(shortList)): # 하나의 누적합 반복문
            tempSum += longList[i] * shortList[shortIdx]
            shortIdx += 1

        maxSum = max(tempSum, maxSum)
        #print(f'{tempSum=}')

    print(f'#{index+1} {maxSum}')