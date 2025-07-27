# 가장 많은 카운트된 층을 구한다 -> 알고리즘이 안 떠오름...
# 땅이 256층, 500*500=250000 -> 시간복잡도 크지 않으므로 층을 완전탐색 -> min값으로 출발해서 max값까지
## 시간초과가 난다...

''' 최종 인벤토리가 음수인지만 보면 되는데, 너무 시뮬레이션스럽게 생각했다...
N, M, B = map(int, input().split()) # N 세로 / M 가로 / B 인벤토리 블록
landMatrix = [ list(map(int, input().split())) for _ in range(N) ]

# 출력 기댓값 (시간, 평평한 높이)
# print(f'{min(min(landMatrix))=} {max(max(landMatrix))=}')

minFloor, maxFloor = min(min(landMatrix)), max(max(landMatrix))
minSec, ansFloor = float('inf'), 0
for targetFloor in range(minFloor, maxFloor+1):
    flag = True # min 계산할 flag 초기화
    tempB = B # 인벤토리 매번 초기화해야 함
    tempSec = 0
    # 흙을 우선 파낸다 -> 인벤토리의 흙을 확보하기 위함
    for row in range(N):
        for col in range(M):
            if landMatrix[row][col] > targetFloor: # 흙을 파야하는 상황 2초
                tempSec += (landMatrix[row][col] - targetFloor) * 2
                tempB += (landMatrix[row][col] - targetFloor)

    # 흙을 마지막으로 채운다 -> 인벤토리의 흙이 최대화된 상황에서 시작하기 위함
    for row in range(N):
        for col in range(M):
            if landMatrix[row][col] < targetFloor: # 흙을 채우는 상황 1초
                tempB -= (targetFloor - landMatrix[row][col])
                if tempB < 0: # 흙이 다 떨어짐 -> 완전히 불가는한 목표층수 -> 완전 탈출
                    flag = False
                    break
                tempSec += (targetFloor - landMatrix[row][col]) * 1

        if not flag:
            break

    # print(f'{tempB=} {targetFloor=} {tempSec=} {minSec=}')
    if flag:
        if minSec > tempSec or (minSec == tempSec and targetFloor > ansFloor): # 시간이 같으면 높은층 선택
            minSec = tempSec
            ansFloor = targetFloor
    # print(f'{targetFloor=} {tempSec=} {minSec=}')

print(f'{minSec} {ansFloor}')
'''

N, M, B = map(int, input().split()) # N 세로 / M 가로 / B 인벤토리 블록
landMatrix = [ list(map(int, input().split())) for _ in range(N) ]

# 출력 기댓값 (시간, 평평한 높이)
# print(f'{min(min(landMatrix))=} {max(max(landMatrix))=}')

minFloor, maxFloor = min(min(landMatrix)), max(max(landMatrix))
minSec, ansFloor = float('inf'), 0
for targetFloor in range(minFloor, maxFloor+1):
    flag = True # min 계산할 flag 초기화
    tempB = B # 인벤토리 매번 초기화해야 함
    tempSec = 0
    # 흙을 우선 파낸다 -> 인벤토리의 흙을 확보하기 위함
    for row in range(N):
        for col in range(M):
            if landMatrix[row][col] > targetFloor: # 흙을 파야하는 상황 2초
                tempSec += (landMatrix[row][col] - targetFloor) * 2
                tempB += (landMatrix[row][col] - targetFloor)

            elif landMatrix[row][col] < targetFloor: # 흙을 채우는 상황 1초
                tempB -= (targetFloor - landMatrix[row][col])
                tempSec += (targetFloor - landMatrix[row][col]) * 1

    if tempB < 0:  # 흙이 다 떨어짐 -> 완전히 불가는한 목표층수 -> 완전 탈출
        flag = False
        continue # break 아님 유의

    # print(f'{tempB=} {targetFloor=} {tempSec=} {minSec=}')
    if flag:
        if minSec > tempSec or (minSec == tempSec and targetFloor > ansFloor): # 시간이 같으면 높은층 선택
            minSec = tempSec
            ansFloor = targetFloor
    # print(f'{targetFloor=} {tempSec=} {minSec=}')

print(f'{minSec} {ansFloor}')