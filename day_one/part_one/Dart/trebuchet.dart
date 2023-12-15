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
