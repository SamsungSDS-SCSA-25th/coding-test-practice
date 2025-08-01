# 임의의 두 공 사이 간격은 짝수
# 인덱스가 같아지는 것이 있으면 충돌횟수 기록하기
### (D) 충돌하더라도 그냥 공의 방향은 나둬도 됨 (예영프로님 아이디어)
# 범위를 넘어서도 RL 바꾸기 -> 0~L
from collections import deque

L, N, T = map(int, input().split())
ballInfoList = [ tuple(input().split()) for _ in range(N) ]
leftList, rightList = [], []
for ballInfo in ballInfoList:
    if ballInfo[1] == 'L':
        leftList.append(int(ballInfo[0]))
    elif ballInfo[1] == 'R':
        rightList.append(int(ballInfo[0]))

# 첫 데이터 전처리
leftList.sort() # 오름차순으로 정렬
rightList.sort(key=lambda x: -x) # 내림차순으로 정렬

# print(leftList)
# print(rightList)

boomCnt = 0
for time in range(T): # 시간동안
    for idx, left in enumerate(leftList):
        leftList[idx] -= 1
        if leftList[idx] == 0: # (D) 1이 아니라 0
            rightList.append(leftList[idx])
            leftList.pop(0)
    for idx, right in enumerate(rightList):
        rightList[idx] += 1
        if rightList[idx] == L:
            leftList.append(rightList[idx])
            rightList.pop(0)

    tempSet = set(leftList) & set(rightList)
    boomCnt += len(tempSet)

print(boomCnt)