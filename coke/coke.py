def main():
    due = 50
    while True:
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            due = due - coin
            if due <= 0:
                print(f"Change Owed: {due*-1}")
                break
        print(coin)
        print(due)

main()
