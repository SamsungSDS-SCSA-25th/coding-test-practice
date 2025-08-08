# 이진탐색으로 풀이
# N * M -> 분명 시간초과
## end -> 최대 나무의 높이 / 높이를 더할 때 음수는 0으로 치환

def binarySearch(trees):
    global N, M, maxH
    start = 1
    end = max(trees)

    while start <= end:
        # print(f'{start=} {end=}')
        midH = (start+end) // 2
        # print(f'{midH=}')
        if sum([max(tree - midH, 0) for tree in trees]) >= M: # 나무 만족하므로 높이를 더 늘려봄 -> 0이하는 안됨
            maxH = max(maxH, midH)
            start = midH + 1

        elif sum([max(tree - midH, 0) for tree in trees]) < M: # 나무를 더 잘라야하므로 높이 줄임 -> 0 이하는 안됨
            end = midH - 1


N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
maxH = 0
binarySearch(trees)
print(maxH)