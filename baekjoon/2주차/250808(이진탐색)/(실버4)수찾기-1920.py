# n * m -> 10^10 시간초과
# 이진탐색

def binarySearch(numList, target):
    global ansList
    start = 0
    end = len(numList) - 1

    while start <= end: # = 조건 기억하기
        mid = (start + end) // 2 # mid는 while 문안에서 start와 end기준으로 갱신

        if numList[mid] == target: # 찾음
            ansList.append(1)
            return

        elif numList[mid] < target: # 타겟보다 작으면 시작점 mid+1
            start = mid + 1
        elif numList[mid] > target: # 타겟보다 크면 끝점 mid-1
            end = mid - 1

    ansList.append(0)
    return # 없음


N = int(input())
numList = list(map(int, input().split()))
M = int(input())
targetList = list(map(int, input().split()))

numList.sort() # 이진탐색 전에는 무조건 오름차순 sort
ansList = []
for target in targetList:
    binarySearch(numList, target)

print(*ansList, sep='\n')