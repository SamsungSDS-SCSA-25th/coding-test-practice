# 임의의 두 공 사이 간격은 짝수
# 인덱스가 같아지는 것이 있으면 충돌횟수 기록하기
### (D) 충돌하더라도 그냥 공의 방향은 나둬도 됨 (예영프로님 아이디어)
# 범위를 넘어서도 RL 바꾸기 -> 0~L

L, N, T = map(int, input().split())
ballInfoList = [ tuple(input().split()) for _ in range(N) ]
leftList, rightList = [], []
for ballInfo in ballInfoList:
    if ballInfo[1] == 'L':
        leftList.append(int(ballInfo[0]))
    elif ballInfo[1] == 'R':
        rightList.append(int(ballInfo[0]))

# 첫 데이터 전처리
leftList.sort() # 오름차순으로 정렬 1 3 4 5
rightList.sort(key=lambda x: -x) # 내림차순으로 정렬 5 4 3 1

# print(leftList)
# print(rightList)

boomCnt = 0
for _ in range(T): # 시간동안
    nxtLeftList, nxtRightList = [], [] # pop을 하지 않기 위해 사용 -> pop하면 index가 꼬임

    for left in leftList:
        nxtLeft = left - 1
        if nxtLeft == 0:
            nxtRightList.append(nxtLeft)
        else:
            nxtLeftList.append(nxtLeft)

    for right in rightList:
        nxtRight = right + 1
        if nxtRight == L:
            nxtLeftList.append(nxtRight)
        else:
            nxtRightList.append(nxtRight)

    # 충돌 판단
    tempSet = set(nxtLeftList) & set(nxtRightList)
    boomCnt += len(tempSet)

    # 갱신
    leftList, rightList = nxtLeftList, nxtRightList

print(boomCnt)