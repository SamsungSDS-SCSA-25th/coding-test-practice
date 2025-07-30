# 소요시간 : 30분
# 시간복잡도 : 125ms
# 공간복잡도 : 61,824 kb

# 위에서부터 n//2 양옆 1씩 더하면서 내려오다가
# n//2 행이 되면 최대화
# 그 이후에 양옆 1씩 지우면서 내려오기 -> tempIdxList 이용

### 타 프로님들 코드를 보니 맨해튼 거리? 절댓값을 이용하여 시작하는 열을 정한 것 같음 '권수현'님 코드가 젤 좋았음

t = int(input())

for index in range(t):
    n = int(input())
    harvestMatrix = [ list(map(int, list(input()))) for _ in range(n) ]

    # print(harvestMatrix)

    harvestSum = 0
    tempIdxList = []
    for idx, colList in enumerate(harvestMatrix):
        if idx <  n//2: # ok
            tempIdxList.append(idx)
            for col in colList[n//2-idx:n//2+idx+1]:
                harvestSum += col
        elif idx == n//2: # ok
            harvestSum += sum(colList)
        elif idx > n//2: # ok
            tempIdx = tempIdxList[-1] # (D) idx에 앞에서 증가한 것을 반대로 내려가면 됨
            tempIdxList.pop()
            for col in colList[n//2-tempIdx:n//2+tempIdx+1]:
                harvestSum += col

    print(f'#{index+1} {harvestSum}')