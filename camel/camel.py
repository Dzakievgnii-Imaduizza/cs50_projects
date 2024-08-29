def main():
    snake = ""
    camel = input("camelCase: ")
    for i in range(len(camel)):
        if camel[i].isupper():
            snake += "_"+camel[i].lower()
        else:
            snake += camel[i]
    print(f"snake_case: {snake}")

main()
