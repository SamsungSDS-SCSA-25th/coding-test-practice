''' # 정렬로 중복 줄이기
def dfs(n, ans):
    global lst
    #1 종료조건
    if n == targetN:
        # sort를 사용하면 안됨.. sorted 써서 순간적으로만 정렬
        if sorted(ans) not in lst:
            lst.append(ans)
            print(*ans)
        return

    #2 하부함수 호출(재귀)
    for rollIdx in range(1, 7): # 주사위 1~6까지 굴리기
        # print(f'#{rollIdx}')
        dfs(n+1, ans + [rollIdx])
'''
# 아이디어로 풀이
def dfs(n, ans):
    global lst
    #1 종료조건
    if n == targetN:
        print(*ans)
        return

    #2 하부함수 호출(재귀)
    if n == 0: # 처음
        for rollIdx in range(1, 7):
            # print(f'#{rollIdx}')
            dfs(n+1, ans + [rollIdx])
    else: # 그 이후
        for rollIdx in range(ans[-1], 7): # 전 노드의 숫자부터 주사위 굴리기 시작하면 됨
            # print(f'#{rollIdx}')
            dfs(n+1, ans + [rollIdx])

#############################

tc = int(input())
for i in range(1, tc+1):
    targetN = int(input())

    print(f'#{i}')
    lst =[]
    dfs(0, [])