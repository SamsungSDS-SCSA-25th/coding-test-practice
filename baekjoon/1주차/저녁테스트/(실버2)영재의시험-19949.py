# 3개의 연속된 문제의 답은 같지 않게 한다는 자신의 비법 ㅋㅋ
# 5지 선다형
# 3칸씩 슬라이딩 하면서 -> 백트래킹
# 3개 연속된 답인 것은 pruning
### 5점 이상인 것을 먼저 가지치기 하면 안됩니다
# -> 뒤에 더 많은 원소들이 와서 더 많은 답안리스트로 파생될 수 있어 (언더카운트)
# -> 뒤에 3개 연속되는 숫자들이 등장가능 (오버카운트)
# -> 언더카운트되는 경우의수가 압도적으로 많음

def backTracking(curIdx, curScore, anslst):
    global res
    # 가지치기1 -> 3개 연속 같은 답
    if 3<=curIdx<=10 and anslst[curIdx - 3] == anslst[curIdx - 2] == anslst[curIdx - 1]:
        # print(anslst)
        return
    # (D) 가지치기2 -> 남은 문제 수로 최대 얻을 수 있는 점수조차 5 미만이면 포기
    if curScore + (10 - curIdx) < 5:
        return

    # 종료조건
    if curIdx == 10:
        if curScore >= 5:
            res += 1
        return
    # 재귀 -> 5가지 답에 대한 하부호출
    for ans in range(1, 6):
        if ans == answerList[curIdx]:
            score = 1
        else:
            score = 0
        backTracking(curIdx + 1, curScore + score, anslst + [ans])


answerList = list(map(int, input().split()))

res = 0
backTracking(0, 0, [])
print(res)