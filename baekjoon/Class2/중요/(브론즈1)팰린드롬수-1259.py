while True:
    n = int(input())

    if n == 0:
        break

    if list(str(n))[::-1] == list(str(n)):
        print('yes')
    else:
        print('no')




