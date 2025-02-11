texts= "apple banana apple orange banana apple"

words = texts.split()
wordCount = {}

for word in words:
    if word in wordCount:
        wordCount[word] +=1
    else:
        wordCount[word] = 1

print("Word counts: ")
for word,count in wordCount.items():
    print(word,count)
