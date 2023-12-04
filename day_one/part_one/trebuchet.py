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
