# TODO
from cs50 import get_string

def main():
    text = get_string("Text: ")
    grade = count_grade(text)
    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print("Grade " + str(grade))

def count_grade(text):
    letters = 0
    words = 1
    sentences = 0
    for i in text:
        if i.isalpha():
            letters += 1
        elif i == " ":
            words += 1
        elif i == "?" or i == "!" or i == ".":
            sentences += 1
    x = 100/words
    l = letters * x
    s = sentences * x
    index = 0.0588 * l - 0.296 * s - 15.8
    result = int(round(index))
    return result




main()