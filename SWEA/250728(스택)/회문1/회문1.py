# dxdy 기법을 활용 대각선 고려 x -> 완탐으로 풀 것이라 후방만 고려
# 짝수, 홀수 구분 -> 회문의 길이가 주어짐

# 10개의 테스트케이스

directionList = [(1,0), (0,1)]

for index in range(8):
    n = int(input()) # 회문의 길이
    matrix = [ list(input()) for _ in range(8) ]

    palindromeCnt = 0
    if n == 1:
        print(f'#{index + 1} {8*8}')
    else:
        for row in range(8):
            for col in range(8):

                for direction in directionList: # (1,0) (0,1)
                    tempList = []
                    for length in range(n):  # 회문의 길이만큼
                        tempRow = row + direction[1] * length
                        tempCol = col + direction[0] * length
                        if 0<= tempRow < 8 and 0<= tempCol < 8:
                            tempList.append(matrix[tempRow][tempCol])
                        else:
                            break

                    # print(f'{tempList=}')
                    # 회문인지 판단하는 알고리즘 (1 제외)
                    if len(tempList) == n: # (D) 회문의 길이가 n을 만족해야 함
                        if n % 2 == 0: # 회문길이가 짝수인 경우
                            if tempList[:n//2] == tempList[n//2:][::-1]: # (D) 역정렬한 것과 동일해야 함
                                palindromeCnt += 1
                        elif n % 2 != 0: # 홀수
                            if tempList[:n//2] == tempList[n//2+1:][::-1]:
                                palindromeCnt += 1

        print(f'#{index+1} {palindromeCnt}')