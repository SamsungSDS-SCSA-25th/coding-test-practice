n = int(input())
wordList = [ input() for _ in range(n) ]
wordList = sorted(list(set(wordList)), key=lambda x: (len(x), x)) # 튜플을 사용하여 다중정렬 (길이, 사전)

for word in wordList:
    print(word)
