# L개의 길이다 -> 조합(사전순) -> 백트래킹

def backTracking(curDepth, startIdx, totalList, aCnt):
    global answer
    # 가지치기 x
    # 종료조건
    if curDepth == L:
        if aCnt >= 1 and len(totalList) - aCnt >= 2:
            answer.append(totalList)
        return
    # 재귀
    for idx in range(startIdx, C):
        if password[idx] in 'aeiou':
            cnt = 1
        else:
            cnt = 0
        backTracking(curDepth + 1, idx + 1, totalList+[password[idx]], aCnt+cnt)

L, C = map(int, input().split())
password = input().split()
password.sort() # 알파벳 사전식 정렬
# print(password)

answer = []
backTracking(0, 0, [], 0)
for ans in answer:
    print(*ans, sep='')