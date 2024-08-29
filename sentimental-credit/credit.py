# TODO
from cs50 import get_int

def main():
    validity = str()
    while True:
        card_number = get_int("Number: ")
        if card_number > 1:
            break
    string_card = str(card_number)
    if calculate(string_card):
        if len(string_card) == 15:
            if string_card[0:2] == "34" or string_card[0:2] == "37":
                print("AMEX")
            else:
                print("INVALID")
        if len(string_card) == 16:
            if string_card[0:2] == "51" or string_card[0:2] == "52" or string_card[0:2] == "53" or string_card[0:2] == "54" or string_card[0:2] == "55":
                print("MASTERCARD")
            elif string_card[0] == "4":
                print("VISA")
            else:
                print("INVALID")
        if len(string_card) == 13:
            if string_card[0] == "4":
                print("VISA")
            else:
                print("INVALID")
        else:
            print("INVALID")
    else:
        print("INVALID")

def calculate(card):
    total = 0
    index = len(card) - 1
    while index >= 0:
        total += int(card[index])
        index -= 2
    index = len(card) - 2
    while index >= 0:
        if int(card[index]) * 2 > 9:
            temp = int(card[index]) * 2
            tempstring = str(temp)
            total += int(tempstring[0])
            total += int(tempstring[1])
        else:
            total += int(card[index]) * 2
        index -= 2
    if total % 10 == 0:
        return True
    else:
        return False
main()