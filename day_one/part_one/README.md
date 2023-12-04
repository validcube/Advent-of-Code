# Advent of Code 2023

## `--- Day 1: Trebuchet?! ---`

### `--- Part One ---`
The solution is very easy, since we know that a wild elf has modified the input file to show her creativity skills;
*I gonna impressed, that for sure took a long time to do!*; what we need to do is 
we just need to read the file, filter anything that isn't an digit out, then we sum the first and the last digit of every line in the input.

Voila! We have the answer; try it out for yourself by running the code on your machine!


```python
# Trebuchet: Sums the first and last digit of each line.
# Advent of Code 2023 - Day 1 - Part 1


trebuchet_array = []


def trebuchet(file):
  with open(file, "r") as file:
    for line in file:
      data = "".join(filter(lambda x: x.isdigit(), line))
      trebuchet_array.append(trebuchet_combine(data))


def trebuchet_combine(data):
  data1 = data[0]
  data2 = data[-1]
  data = str(data1) + str(data2)
  return int(data)


trebuchet("data.txt")
print(f"🥞 The result is {sum(trebuchet_array)}")
```

<details>
  <summary>🚧 Spoiler</summary>

  The answer is `53386`, that's because we appended the result of the data that have been stripped of anything that isn't a digit (`trebuchet()` and `trebuchet_combine(data)`), then we summed the first and the last digit of each line (`sum(trebuchet_array)`).

  ```python
  def trebuchet(file):
    # We open the file, read it, and go through
    # each line to filter out anything that isn't a digit.

    # We send the data that have been filtered to `trebuchet_combine` function

    # We append the result of the data that have been combined to `trebuchet_array`
    # so we can sum it later.

    with open(file, "r") as file:
      for line in file:
        data = "".join(filter(lambda x: x.isdigit(), line))
        trebuchet_array.append(trebuchet_combine(data))


  def trebuchet_combine(data):
    data1 = data[0]
    data2 = data[-1]
    data = str(data1) + str(data2)
    return int(data)


  trebuchet("data.txt")
  print(f"🥞 The result is {sum(trebuchet_array)}") # Sum the first and the last digit of each line.
  ```
</details>

