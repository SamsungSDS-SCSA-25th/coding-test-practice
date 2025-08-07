# 병합정렬 -> O(NlogN)
# 분할: 두개의 리스트로 나눈다 (길이 같거나, 1 차이남)
# 정복: 두개의 리스트 각각 정렬한다
# 재귀: 두개의 리스트를 계속 나누고, 1이 되면 멈춘다.

def merge(lst1, lst2):
    result = []
    idx1 = idx2 = 0
    while idx1 < len(lst1) and idx2 < len(lst2): # 두 리스트에 요소가 남아있는 동안 반복
        if lst1[idx1] <= lst2[idx2]: # lst1에서 꺼낸 것이 더 작음
            result.append(lst1[idx1]) # 먼저 append
            idx1 += 1 # lst1 다음 인덱스로
        else:
            result.append(lst2[idx2]) # lst2에서 꺼낸 것이 더 작음
            idx2 += 1 # lst2 다음 인덱스로

    if idx1 == len(lst1):
        result += lst2[idx2:]
    else:
        result += lst1[idx1:]
    return result

# 계속 파고, 파고 들어감 -> 리스트의 원소가 1일때 돌아온다
def mergeSort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return merge(left, right) # left, right가 재귀되어 돌아올 때 병합


N = int(input())
nums = list( int(input()) for _ in range(N) )

print(*mergeSort(nums), sep='\n')