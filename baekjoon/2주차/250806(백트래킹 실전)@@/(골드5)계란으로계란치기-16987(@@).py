# 계란에 대해 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제
# 가장왼쪽 -> 아무계란이나 치기 -> 오른쪽 이동 | 손에 든 계란의 내구도 확인
# 순열이 아님 칠 계란은 랜덤하게 선택할 수 있기 때문

def backTracking(curIdx, curCnt):
    global maxCnt
    # 가지치기 x
    # 종료조건
    if curIdx == N:
        maxCnt = max(maxCnt, curCnt) # 깨진 계란 최대값 업데이트
        return
    # 재귀
    if eggs[curIdx][0] <= 0: # 현재 선택한 계란의 내구도가 0보다 작으면
        backTracking(curIdx + 1, curCnt) # 다음 계란을 선택하러 감

    else: # 선택한 계란 내구도 0초과
        canBreak = False # (D) 선택한 계란에 대한 깰 계란 있는지 확인 flag
        for eggIdx in range(N):
            if curIdx == eggIdx : # 선택한 계란과 동일한 차례면 pass
                continue

            if eggs[eggIdx][0] > 0: # 당한 계란의 내구도 0초과
                canBreak = True # 깰수 있는 계란이 있는 것
                eggs[eggIdx][0] -= eggs[curIdx][1] # 당한 계란: 친 계란 무게만큼 내구도 감소
                eggs[curIdx][0] -= eggs[eggIdx][1] # 친 계란: 당한 계란 무게만큼 내구도감소
                cnt = 0
                if eggs[eggIdx][0] <= 0:
                    cnt += 1
                if eggs[curIdx][0] <= 0:
                    cnt += 1
                backTracking(curIdx + 1, curCnt + cnt)
                eggs[eggIdx][0] += eggs[curIdx][1] # 위 내용 원상복구
                eggs[curIdx][0] += eggs[eggIdx][1] # 동

        # (D) 위에서 모든 계란에 대해 탐색했는데 깰 수 있는 계란이 없음 -> 이번 선택한 계란에
        # 칠 계란이 없어도 앞으로 나아가서 확인해봐야함
        if not canBreak:
            backTracking(curIdx + 1, curCnt)

N = int(input())
# (내구도, 무게)
eggs = [ list(map(int, input().split())) for _ in range(N) ]

maxCnt = 0
backTracking(0, 0)
print(maxCnt)