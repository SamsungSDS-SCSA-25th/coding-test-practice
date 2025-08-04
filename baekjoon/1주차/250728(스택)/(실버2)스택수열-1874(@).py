# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# stack에서 pop하는 것 나열한 것이 입력값이 target이어야 함
## 디버거로 어디서 반복과 분기가 틀어지는지 확인하면서 손코딩 리팩터링

n = int(input())
targetList = [int(input()) for _ in range(n)]
stack = []
pushPopList = []
current = 1
flag = True
for target in targetList:
    while current <= target: #1 target까지 도달할 때까지 append (append 할때는 무조건 1씩 오름차순)
        stack.append(current)
        pushPopList.append('+')
        current += 1

    if stack and stack[-1] == target: #2 stack의 마지막 값과 target이 같으면
        stack.pop()
        pushPopList.append('-')
    else: #3 실패
        flag = False
        break

if flag:
    print('\n'.join(pushPopList))
else:
    print('NO')