def main():
    raw = input("Input: ")
    twttr = ""
    for i in range(len(raw)):
        if raw[i] != "A" and raw[i] != "a" and raw[i] != "I" and raw[i] != "i" and raw[i] != "U" and raw[i] != "u" and raw[i] != "E" and raw[i] != "e" and raw[i] != "O" and raw[i] != "o":
            twttr += raw[i]
    print(twttr)

main()
