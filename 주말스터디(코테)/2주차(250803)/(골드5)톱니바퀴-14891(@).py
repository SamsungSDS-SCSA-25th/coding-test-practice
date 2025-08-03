# (1) 왼쪽/오른쪽 전파 -> (2) 일괄 회전

from collections import deque

wheelList = [deque(list((map(int, list(input()))))) for _ in range(4)]
k = int(input())
rotateList = [tuple(map(int, input().split())) for _ in range(k)]
# print(wheelList)
# print(rotateList)

for wheelIdx, rotateHow in rotateList:
    wheelIdx -= 1
    directions = [0, 0, 0, 0]
    directions[wheelIdx] = rotateHow

    # 왼쪽으로 전파
    for tempWheelIdx in range(wheelIdx, 0, -1): # 0은 포함 x
        if wheelList[tempWheelIdx][6] != wheelList[tempWheelIdx-1][2]:
            directions[tempWheelIdx-1] = -directions[tempWheelIdx] # 현재 톱니바퀴와 반대방향
        else: # 같으면 중단
            break

    # 오른쪽으로 전파
    for tempWheelIdx in range(wheelIdx, 3):
        if wheelList[tempWheelIdx][2] != wheelList[tempWheelIdx+1][6]:
            directions[tempWheelIdx+1] = -directions[tempWheelIdx]  # 현재 톱니바퀴와 반대방향
        else:
            break

    # 전파된 것들 일괄 회전
    for tempWheelIdx, dir in enumerate(directions):
        if dir: # 전파 안된 부분은 0으로 남아있음
            wheelList[tempWheelIdx].rotate(dir)

ansList = [1,2,4,8]
score = 0
for idx in range(4):
    score += wheelList[idx][0] * ansList[idx]

# print(*wheelList)
print(score)