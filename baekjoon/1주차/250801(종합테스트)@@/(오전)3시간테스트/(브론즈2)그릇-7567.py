dishList = list(input())

h = 0
for idx, dish in enumerate(dishList):
    if idx == 0:
        h += 10
        continue

    if dishList[idx-1] == '(':
        if dishList[idx] == ')':
            h += 10
        elif dishList[idx] == '(':
            h += 5

    elif dishList[idx-1] == ')':
        if dishList[idx] == '(':
            h += 10
        elif dishList[idx] == ')':
            h += 5

print(h)