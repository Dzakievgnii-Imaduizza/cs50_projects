import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py DATABASEFILE SEQUENCEFILE")

    # TODO: Read database file into a variable
    database = []
    with open(sys.argv[1], "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            database.append(row)

    with open(sys.argv[1], "r") as f:
        reader = csv.reader(f)
        temp = []
        for row in reader:
            temp.append(row)

    short_tandems = temp[0]

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as f:
        sequence = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    dict = {}
    for i in range(1, len(short_tandems)):
        key = short_tandems[i]
        dict[key] = longest_match(sequence, short_tandems[i])

    # print(short_tandems)
    # TODO: Check database for matching profiles
    i = 0
    while i < len(database):
        j = len(short_tandems)-1
        similar = 0
        while j > 0:
            index = short_tandems[j]
            if int(database[i][index]) == dict[index]:
                similar += 1
            j -= 1

        if similar == len(short_tandems)-1:
            print(database[i]["name"])
            return
        i += 1

    print("No Match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
