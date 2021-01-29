word = input("Enter word: ")
index = 0
for i in word:
    if i in ['a', 'e', 'i', 'o', 'u']: break
    else: index = index + 1
print(word[index:len(word)] + word[0:index] + 'ay')
