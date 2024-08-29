from cs50 import get_string

text = get_string("text: ")
count = 0
for c in text:
    if c == " ":
        count += 1
print(count)