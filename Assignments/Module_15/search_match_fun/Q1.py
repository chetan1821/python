import re

text = "Python is very easy to learn"

word = "easy"

result = re.search(word, text)

if result:
    print("Word found in string")
else:
    print("Word not found")