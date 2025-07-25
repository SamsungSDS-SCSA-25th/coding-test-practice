## 이중 for문 불가인지 완전탐색 해보기 -> 중간에 break하는 조건 있으면 가능할지도?
## 슬라이딩 윈도우
# - 고정된 길이 또는 조건에 따라 움직이는 연속된 구간을 탐색
# - 앞에서 하나 빼고, 뒤에 하나 더하는 방식으로 창을 미끄러지듯 이동
## 수학적 규칙찾기
# // 하고 범위만큼 합하기
# // 하고 0이 등장하면 for문 break -> cnt 출력
# 짝수와 홀수를 나누어서, center와 offset 규칙을 발견하고 문제풀이

'''
n = int(input())

cnt = 0
for num in range(1, n+1):
    center = n // num

    if num % 2 != 0:
        tempSum = 0
        offset = (num - 1) // 2
        if center - offset <= 0:
            break
        for temp in range(center - offset, center + offset + 1):
            tempSum += temp
            if tempSum == n:
                cnt += 1
                #print(num)

    elif num % 2 == 0:
        tempSum = 0
        offset = num // 2
        if center - offset + 1 <= 0:
            break
        for temp in range(center - offset + 1, center + offset + 1):
            tempSum += temp
            if tempSum == n:
                cnt += 1
                #print(num)

print(cnt)
'''

# 슬라이딩 윈도우 -> 원리) github slidingWindow.md 참고
n = int(input())

start, end = 1, 1
currentSum = 1
cnt = 0

while start <= n: # 1부터 시작
    if currentSum == n: # 순서 유의
        cnt += 1
        currentSum -= start
        start += 1
    elif currentSum < n: # 순서 유의
        end += 1
        currentSum += end
    else: # 순서 유의
        currentSum -= start
        start += 1

print(cnt)