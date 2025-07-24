# 이중 for문 불가
# // 하고 범위만큼 합하기
# // 하고 0이 등장하면 for문 break -> cnt 출력
# 짝수와 홀수를 나누어서, center와 offset 규칙을 발견하고 문제풀이

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