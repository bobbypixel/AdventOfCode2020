import pathlib
import unittest

PUZZLE_INPUT = "input.txt"
TEST_INPUT = "test-input.txt"

def rambunctious_recitation(starting_numbers: list[int], last_turn: int) -> int:
    nums = starting_numbers.copy()
    for turn in range(len(starting_numbers), last_turn):
        last_num = nums[turn-1]
        if last_num not in nums[:-1]:
            nums.append(0)
        else:
            nums.append((turn-1) - max(i for i,j in enumerate(nums[:-1]) if j == last_num))
    return nums[-1]

def process_input(file_name: str):
    with (pathlib.Path(__file__).parent / file_name).open() as input_file:
        output = list(map(int, input_file.readline().strip().split(',')))
    return output

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(436, rambunctious_recitation(process_input(TEST_INPUT), 2020))
    def test_2(self):
        self.assertEqual(175594, rambunctious_recitation(process_input(TEST_INPUT), 30000000))

if __name__ == "__main__":
    unittest.main(exit=False)

    pro_input = process_input(PUZZLE_INPUT)
    print(f"Part 1 Answer: {rambunctious_recitation(pro_input, 2020)}")
    print(f"Part 2 Answer: {rambunctious_recitation(pro_input, 30000000)}")
    
