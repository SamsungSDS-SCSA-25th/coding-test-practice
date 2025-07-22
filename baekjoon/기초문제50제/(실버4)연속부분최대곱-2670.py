n = int(input())
num_list = [ float(input()) for _ in range(n) ]

maxProduct = num_list[0]
for start in range(n):
    tempProduct = 1
    for end in range(start, n):
        tempProduct *= num_list[end]
        if maxProduct < tempProduct:
            maxProduct = tempProduct

print(f'{maxProduct:.3f}')
