n, k = map(int, input().split())

def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def combination(n, k):
    result = factorial(n) // (factorial(n - k) * factorial(k))
    return result

print(combination(n, k))