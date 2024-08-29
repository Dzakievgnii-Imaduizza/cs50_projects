greeting = input("Greeting: ").strip().lower()
prize = 0
if not greeting.startswith("hello") and not greeting.startswith("h"):
    prize = 100
elif greeting.startswith("h") and not greeting.startswith("hello"):
    prize = 20
print(f"${prize}")
