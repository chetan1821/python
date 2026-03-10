import re

text = "Python is very easy to learn"
word = "Python"
result = re.match(word, text)
if result:
    print("Word matched at beginning")
else:
    print("Word not matched")