def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validity = True
    lastNum = False
    firstNum = False
    if not (2 <= len(s) <= 6):
        validity = False
    if not (s[0].isalpha() and s[1].isalpha()):
        validity = False
    if s[len(s)-1].isnumeric():
        lastNum = True
    for i in range(len(s)-2,-1,-1):
        if s[i].isnumeric() and not lastNum:
            validity = False
        if not s[i].isnumeric():
            lastNum = False
    punc = ["|", "/", "\\", ":", "*", "?", '"', "<", ">"," ",".",","]
    for i in range(len(s)):
        for j in range(len(punc)):
            if s[i] == punc[j]:
                validity = False
    for i in range(len(s)):

        if s[i].isnumeric() and not firstNum:
            firstNum = True
            if s[i] == "0":
                validity = False
                break
            else:
                break
    # for i in range(5,-1,-1):
        # print(i)

    return validity

main()
