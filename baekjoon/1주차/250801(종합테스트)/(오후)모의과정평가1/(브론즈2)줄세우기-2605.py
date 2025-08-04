n = int(input())
numList = list(map(int, input().split()))

answer = [1]
for student in range(2, n+1):
    cardNum = numList[student-1]
    if cardNum == 0:
        answer.append(student)
        continue
    answer.insert(-(cardNum), student)

print(*answer)