# 상한액이 있다.
# 상한액을 이진탐색하며, 최댓값을 업데이트

def binarySearch(bugets, total):
    global answer
    start = 0
    end = max(bugets)

    while start <= end:
        # print(f'{start=} {end=}')
        midFrontier = (start+end) // 2
        # print(f'{midFrontier=}')
        if sum([min(midFrontier, budget) for budget in bugets]) == total:
            # print(f'{0}{sum([min(midFrontier, budget) for budget in bugets])=}')
            return midFrontier # 총예산과 같은 순간이면 그냥 return

        elif sum([min(midFrontier, budget) for budget in bugets]) <= total: # 예산여유, 상한액을 좀 더 높여볼까
            answer = midFrontier # 최종적으로 예산이 최대가 되는 경계선 (매번 갱신하다가 마지막의 answer 찍힌 것이 답)
            start = midFrontier + 1

        elif sum([min(midFrontier, budget) for budget in bugets]) > total: # 예산초과, 상한액을 낮춰야 함
            # print(f'{2}{sum([min(midFrontier, budget) for budget in bugets])=}')
            end = midFrontier - 1

    return answer


N = int(input())
budgets = list(map(int, input().split()))
total = int(input())

answer = binarySearch(budgets, total)
print(answer)