def main():
    nowTime = input("What time is it? ")
    timeInDecimal = convert(nowTime)
    if 7 <= timeInDecimal <= 8:
        print("breakfast time")
    if 12 <= timeInDecimal <= 13:
        print("lunch time")

    if 18 <= timeInDecimal <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    final = hour + minute/60
    return final


if __name__ == "__main__":
    main()
