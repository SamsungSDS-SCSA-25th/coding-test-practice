# 일반적인 정렬문제

r, c = map(int, input().split())
imageMatrix = [ list(map(int, input().split())) for _ in range(r) ]
t = int(input())

filteredMatrix = []
for row in range(r-2): # 좌표하나잡기
    tempColList = []
    for col in range(c-2):
        tempMedianList = []
        for tempRow in range(row,row+3): # 9개 순환하기
            for tempCol in range(col,col+3):
                tempMedianList.append(imageMatrix[tempRow][tempCol])
        # 9개 중 5번째 숫자가 중앙값
        tempMedianList.sort() # (D) 오름차순으로 정렬 후 중앙값 고르기
        tempColList.append(tempMedianList[4])
    # print(tempColList)
    filteredMatrix.append(tempColList)

cnt = 0
for row in range(r-2):
    for col in range(c-2):
        if filteredMatrix[row][col] >= t:
            cnt += 1
print(cnt)