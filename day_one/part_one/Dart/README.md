# Advent of Code 2023

## `--- Day 1: Trebuchet?! ---`

Question: [Day 1, Part 1](QUESTION.md)

### Navigator

* [Python](/day_one/part_one/README.md)
* Dart

### `--- Part One ---`
The solution is very easy, since we know that a wild elf has modified the input file to show her creativity skills;
*I gonna impressed, that for sure took a long time to do!*; what we need to do is 
we just need to read the file, filter anything that isn't an digit out, then we sum the first and the last digit of every line in the input.

Voila! We have the answer; try it out for yourself by running the code on your machine!

> ![TIP]
> This explaination is written for Python, but you can visit other languages like Dart.

```Dart
// Trebuchet: Sums the first and last digit of each line.
// Advent of Code 2023 - Day 1 - Part 1

import 'dart:convert';
import 'dart:io';

int trebuchetCombine(String data) {
  final data1 = data[0];
  final data2 = data[data.length - 1];
  final result = data1 + data2;

  return int.parse(result);
}

void main() {
  final data = File('data.txt');
  num sum;
  List list = [];

  Stream<String> lines = data.openRead().transform(utf8.decoder).transform(
        LineSplitter(),
      );

  lines.forEach((line) {
    final result = trebuchetCombine(
      line.replaceAll(RegExp(r'[^0-9]'), ''),
    );
    list.add(result);
  }).then(
    (value) => {
      sum = list.reduce((a, b) => a + b),
      print('🥞 The result is $sum'),
    },
  );
}

```

<details>

  <summary>🚧 Spoiler</summary>

  The answer is `53386`

  We first read the puzzle input, and we read it line by line, then we remove anything that isn't a digit using regex, then we sum the first and last digit of each line.

</details>

