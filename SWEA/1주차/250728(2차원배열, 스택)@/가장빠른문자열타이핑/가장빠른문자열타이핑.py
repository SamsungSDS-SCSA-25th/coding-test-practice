## 뒤에서 접근할 필요도 없고, 그냥 앞에서 출발해서 같은 문자열이면
### 리스트 슬라이싱은 범위초과 전까지 그냥 출력해줌!!!

t = int(input())

for index in range(t):
    info = input().split()
    infoList, targetList = list(info[0]), list(info[1])
    # print(f'{infoList=} {targetList=}')

    idx, cnt = 0, 0
    while idx < len(infoList):
        if infoList[idx:idx+len(targetList)] == targetList:
            cnt += 1
            idx += len(targetList)
        else:
            cnt += 1
            idx += 1

    print(f'#{index+1} {cnt}')