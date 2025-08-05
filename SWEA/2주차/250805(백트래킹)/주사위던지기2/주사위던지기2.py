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

#############################

tc = int(input())
for i in range(1, tc+1):
    targetN = int(input())

    print(f'#{i}')
    lst =[]
    dfs(0, [])
    print()