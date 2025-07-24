P = int(input())

for _ in range(P):
    testList = list(map(int, input().split()))
    index = testList[0]
    heightList = testList[1:]

    lineList = []
    moveCnt = 0

    for height in heightList:
        inserted = False
        for idx in range(len(lineList)): # 처음은 반복문이 안돈다!!!
            if height < lineList[idx]: # 앞으로 이동해야하는 상황
                lineList.insert(idx, height) # 앞으로 한칸 이동
                moveCnt += len(lineList) - idx - 1  # 밀린 횟수 계산 -> 가장 앞에서 작은 수 앞으로 들어가면 돼서 idx는 for문 탈출!!!
                inserted = True
                break
        if not inserted:
            lineList.append(height)  # 제일 큰 경우 그냥 맨 뒤에

    print(index, moveCnt)
