# TODO
from cs50 import get_int

def main():
    while True:
        height = get_int("Height: ")
        if height > 0:
            if height < 9:
                break
    draw(height)

def draw(height):
    spaces = 2
    initial_spaces = height - 1
    hashes = 1
    for i in range(height):
        print(" " * initial_spaces + "#" * hashes + " " * spaces + "#" * hashes)
        hashes += 1
        initial_spaces -= 1

main()