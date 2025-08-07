# 퀵정렬 -> O(NlogN)
# 분할: index 0을 기준으로 작으면 lowList에, 크면 highList에 넣기
# 정복: lowList + pivot + highList
# 재귀: lowList or highList가 길이가 하나로 갈때까지의 깊이로 들어감

def quickSort(nums):
    # 종료조건
    if len(nums) <= 1:
        return nums # nums의 길이가 최대한 작아진 상태
    low, high = [], []
    pivot = nums[0]
    for n in nums[1:]:
        if n < pivot:
            low.append(n)
        elif n >= pivot:
            high.append(n)
    # print(f'{low=} {pivot=} {high=}')
    return quickSort(low) + [pivot] + quickSort(high)

N = int(input())
nums = list( int(input()) for _ in range(N) )

print(*quickSort(nums), sep='\n')