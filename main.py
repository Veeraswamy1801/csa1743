import itertools

def solve_cryptarithmetic():
    # Define the words involved
    word1 = "SEND"
    word2 = "MORE"
    result = "MONEY"

    # Extract unique characters
    unique_chars = set(word1 + word2 + result)
    if len(unique_chars) > 10:
        print("Too many unique letters (more than 10), cannot assign unique digits.")
        return

    # Convert to list for indexing
    unique_chars = list(unique_chars)

    # Generate all possible digit assignments (permutations of 0-9)
    for perm in itertools.permutations(range(10), len(unique_chars)):
        char_digit = dict(zip(unique_chars, perm))

        # Skip if any word starts with 0
        if char_digit[word1[0]] == 0 or char_digit[word2[0]] == 0 or char_digit[result[0]] == 0:
            continue

        # Convert words to numbers
        num1 = int("".join(str(char_digit[c]) for c in word1))
        num2 = int("".join(str(char_digit[c]) for c in word2))
        res = int("".join(str(char_digit[c]) for c in result))

        if num1 + num2 == res:
            print(f"Solution Found:")
            print(f"{word1} = {num1}")
            print(f"{word2} = {num2}")
            print(f"{result} = {res}")
            print(f"Mapping: {char_digit}")
            return
n
    print("No solution found.")

# Run the function
solve_cryptarithmetic()
