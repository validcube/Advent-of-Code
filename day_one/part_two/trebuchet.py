# Trebuchet: Sums the first and last digit of each line.
# Advent of Code 2023 - Day 1 - Part 2

alphabetical_number = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def trebuchet_check_side(chars, index, left):
    start = max(0, index - 4) if left else index
    end = index + 1 if left else min(index + 5, len(chars))
    word = "".join(chars[start:end])

    for index2, number in enumerate(alphabetical_number, start=1):
        if (left and word.endswith(number)) or (not left and word.startswith(number)):
            return index2
        
    return 0


def trebuchet_combine(left, right):
    return left * 10 + right


def trebuchet(file):
    trebuchet_array = []

    with open(file, "r") as file:
        for line in file:
            chars = [
                int(chars2)
                if chars2.isdigit()
                else trebuchet_check_side(line, index, left=True)
                or trebuchet_check_side(line, index, left=False)
                for index, chars2 in enumerate(line)
            ]
            
            left = next((number for number in chars if number != 0), 0)
            right = next((number for number in reversed(chars) if number != 0), left)
            trebuchet_array.append(trebuchet_combine(left, right))

    return trebuchet_array


result = sum(trebuchet("data.txt"))
print(f"🥞 The result is {result}")
