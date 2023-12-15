# Advent of Code 2023

## `--- Day 1: Trebuchet?! ---`

Question: [Day 1, Part 2](QUESTION.md)

### `--- Part Two ---`
Whoops! It looks like the calculation is wrong, it looks like some of the digits are actually **spelled out with letters**, one to nine!

This is going to be a pain, haha!


```python
# Trebuchet: Sums the first and last digit of each line.
# Advent of Code 2023 - Day 1 - Part 2

alphabetical_number = [
    "one", "two", "three",
    "four", "five", "six",
    "seven", "eight", "nine",
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
```

<details>

  <summary>🚧 Spoiler</summary>

  The answer is `53312`, that's because we check the left & right (`trebuchet_check_side`) result of the data, then we sum the result of the left & right (`trebuchet_combine`).

  We multiply the left by 10 to form a two digit number, then we sum up the result from the right to get the final result (of the... you get what I mean I forgot the word *Hey, I'm not native speaker ok? :/*).
  > left * 10 + right = result
  > 6 * 10 + 9 = 69

</details>
