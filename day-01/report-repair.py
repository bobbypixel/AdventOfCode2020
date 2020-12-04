from __future__ import annotations
import os
import unittest

def report_repair_1(report: list[int]) -> int:
    for i in range(len(report)):
        for j in range(i, len(report)):
            if report[i] + report[j] == 2020:
                return report[i] * report[j]

def report_repair_2(report: list[int]) -> int:
    for i in range(len(report)):
        for j in range(i, len(report)):
            for k in range(j, len(report)):
                if report[i] + report[j] + report[k] == 2020:
                    return report[i] * report[j] * report[k]

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(514579, report_repair_1([1721, 979, 366, 299, 675, 1456]))
    def test_2(self):
        self.assertEqual(241861950, report_repair_2([1721, 979, 366, 299, 675, 1456]))

if __name__ == "__main__":
    # Optional tests
    # unittest.main()
    
    dirname = os.path.dirname(__file__)
    puzzle_input = os.path.join(dirname, "input.txt")

    with open(puzzle_input) as f:
        lineList = f.readlines()
        lineList = [int(line.strip()) for line in lineList]
        print(f"Part 1 Answer: {report_repair_1(lineList)}")
        print(f"Part 2 Answer: {report_repair_2(lineList)}")
