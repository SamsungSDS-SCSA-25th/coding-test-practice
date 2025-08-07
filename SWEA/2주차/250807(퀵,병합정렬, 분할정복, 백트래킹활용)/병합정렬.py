# 병합정렬 -> O(NlogN)
# 분할: 두개의 리스트로 나눈다 (길이 같거나, 1 차이남)
# 정복: 두개의 리스트 각각 정렬한다
# 재귀: 두개의 리스트를 계속 나누고, 1이 되면 멈춘다.

def merge(lst1, lst2):
    global cnt
    # 병합 직전 카운트
    if lst1 and lst2 and lst1[-1] > lst2[-1]:
        cnt += 1

    result = []
    idx1 = idx2 = 0
    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1] <= lst2[idx2]:
            result.append(lst1[idx1])
            idx1 += 1
        else:
            result.append(lst2[idx2])
            idx2 += 1

    if idx1 == len(lst1):
        result += lst2[idx2:]
    else:
        result += lst1[idx1:]
    return result

def mergeSort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return merge(left, right)

tc = int(input())
for i in range(1, tc+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0

    sorted = mergeSort(nums)
    # 가운데 원소와 카운트 출력
    print(f"#{i} {sorted[N//2]} {cnt}")