def main():
    dollars = input("How much was the meal? ")
    dollars = dollars_to_float(dollars.replace('$',''))
    percent = input("What percentage would you like to tip? ")
    percent = percent_to_float(percent.replace('%',''))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    return float(d)



def percent_to_float(p):
    # TODO
    per = float(p) / 100
    return per


main()