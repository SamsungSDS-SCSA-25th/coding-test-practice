subjectNum = int(input())
scoreList = list(map(int, input().split()))

standard = max(scoreList)
newScoreList = [ score / standard * 100 for score in scoreList ]
avg = sum(newScoreList) / subjectNum
print(avg)