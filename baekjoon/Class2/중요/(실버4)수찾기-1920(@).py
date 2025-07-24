# for문 2번 돌리면 2^10이라 뻑날거 같음 -> 1초 2^8
# 이분탐색 -> 오름차순, 반복적으로 반으로 나눠서(mid) (target)검색 O(logN)

def binary_search(target, data):
    start = 0
    end = len(data)-1

    while start <= end: #
        mid = (start+end)//2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid+1
        else:
            end = mid-1

    return

n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

nList.sort() # 이분 탐색마다 sort하는 것은 시간낭비
for m in mList: # nList 중 m이 있나?
    if binary_search(m, nList) is not None: # 어떤 정수가 반환될지 몰라 None으로 함. flag 세우는 방법도 있을듯
        print(1)
    elif binary_search(m, nList) is None:
        print(0)