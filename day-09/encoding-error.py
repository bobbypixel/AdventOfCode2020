from itertools import combinations
import pathlib
import unittest

PUZZLE_INPUT = "input.txt"
TEST_INPUT = "test-input.txt"

def encoding_error_1(xmas_data: list[int], preamble_len: int) -> int:
    for num in range(preamble_len, len(xmas_data)):
        prev_nums = [xmas_data[n] for n in range(num - preamble_len, num)]
        if not check_sum(prev_nums, xmas_data[num]):
            return xmas_data[num]

def check_sum(nums: list[int], k: int) -> bool:
    return any(sum(pair) == k for pair in combinations(nums, 2))

def encoding_error_2(xmas_data: list[int], preamble_len: int) -> int:
    invalid_num = encoding_error_1(xmas_data, preamble_len)
    con_set = find_contiguous_set(xmas_data, invalid_num)
    return min(con_set) + max(con_set)

def find_contiguous_set(xmas_data: list[int], invalid_num: int) -> list[int]:
    curr_set = []
    for i in range(len(xmas_data)):
        curr_set.append(xmas_data[i])
        curr_sum = sum(curr_set)
        if curr_sum == invalid_num:
            return curr_set
        while curr_sum > invalid_num:
            curr_set.pop(0)
            curr_sum = sum(curr_set)
            if curr_sum == invalid_num:
                return curr_set

def process_input(file_name: str) -> list[int]:
    with (pathlib.Path(__file__).parent / file_name).open() as input_file:
        output = list(map(int, input_file.readlines()))
    # Output: [0, 1, 2, 3,...]
    return output

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(127, encoding_error_1(process_input(TEST_INPUT), 5))
    def test_2(self):
        self.assertEqual(62, encoding_error_2(process_input(TEST_INPUT), 5))

if __name__ == "__main__":
    unittest.main(exit=False)

    pro_input = process_input(PUZZLE_INPUT)
    print(f"Part 1 Answer: {encoding_error_1(pro_input, 25)}")
    print(f"Part 2 Answer: {encoding_error_2(pro_input, 25)}")
