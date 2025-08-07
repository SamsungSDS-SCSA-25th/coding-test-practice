# 49개 중에 k개의 수를 골라서 입력값에 주어짐
# 위 조합에서 또 6개를 고르는 조합 -> 백트래킹
# S의 원소는 오름차순으로 주어짐

def backTracking(curDepth, startIdx, lst):
    global answer
    # 가지치기 x
    # 종료조건
    if curDepth == 6:
        answer.append(lst)
        return
    # 재귀
    for idx in range(startIdx, K):
        backTracking(curDepth + 1, idx + 1, lst + [nums[idx]])

while True:
    info = list(map(int, input().split()))
    if info[0] == 0:
        break

    answer = []
    K, nums = info[0], info[1:]
    backTracking(0, 0, [])
    for ans in answer:
        print(*ans)
    print()