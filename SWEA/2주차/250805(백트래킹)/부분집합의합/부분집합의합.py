# 부분집합을 구하는 것으로 구현...
# answerList --> cnt로 변환하면 더 간단해질 것

def dfs(curDepth, answer, curSum, startIdx):
    global N, setSum, A, answerList
    # print(f'{answer=}')
    # 종료조건
    if curDepth == N: # 원소 꽉찬 경우
        # print(f'{answer=}')
        if curSum == setSum: # 합조건 만족하는 경우 (음수가 없어서 return 바로)
            answerList.append(answer)
        return

    # 재귀
    for idx in range(startIdx, len(A)): # (D) A의 길이만큼 =..-
        dfs(curDepth + 1, answer + [A[idx]], curSum + A[idx], idx + 1)

tc = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in range(1, tc+1):
    N, setSum = map(int, input().split())
    answerList = []

    print(f'#{i}', end=' ')
    dfs(0, [], 0, 0)
    print(len(answerList))