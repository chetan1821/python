# | Symbol | Meaning                  |
# | ------ | ------------------------ |
# | `.`    | Any character            |
# | `^`    | Start of string          |
# | `$`    | End of string            |
# | `*`    | 0 or more times          |
# | `+`    | 1 or more times          |
# | `?`    | 0 or 1 time              |
# | `{}`   | Specific number of times |
# | `[]`   | Set of characters        |
# | `\`    | Escape character         |

import re
# . Any charcter
# text = "chetan ohello  hoe"
# r = re.findall(".he",text)
# print(r)


# ^ caret => Matches pattern only at beginning

# Dollar ($) → End of String
# 👉 Matches pattern only at end

# txt = "Python is best"
# r= re.findall("^Python",txt)
# r1=re.findall("best$",txt)
# print(r1)


# 4. Star (*) → 0 or More Times
# 👉 Matches zero or more occurrences

text = "ie  ie am gowo gow goooo to "
print(re.findall("ie*", text))

# Plus (+) → 1 or More Times
# 👉 Matches at least one




