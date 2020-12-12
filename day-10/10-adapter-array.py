import pathlib
import unittest

PUZZLE_INPUT = "input.txt"
TEST_INPUT = "test-input.txt"

def adapter_array_1(adapters: list[int]) -> int:
    jolt_diff = [0, 0, 0]
    for i in range(len(adapters)-1):
        diff = adapters[i+1] - adapters[i]
        jolt_diff[diff-1] += 1
    return jolt_diff[0] * jolt_diff[2]

# Solution by @Brotherluii
# https://twitter.com/Brotherluii/status/1337026275354038274
def adapter_array_2(adapters: list[int]) -> int:
    jolt_diffs = []
    for i in range(len(adapters)-1):
        jolt_diffs.append(adapters[i+1] - adapters[i])
    row = 0
    jolt_rows = [0, 0, 0]
    for i in range(len(jolt_diffs)):
        if jolt_diffs[i] == 1:
            row += 1
        else:
            if row > 1:
                jolt_rows[row-2] += 1
            row = 0
    return 2**jolt_rows[0] * 4**jolt_rows[1] * 7**jolt_rows[2]

def process_input(file_name: str) -> list[int]:
    with (pathlib.Path(__file__).parent / file_name).open() as input_file:
        output = sorted(list(map(int, input_file.readlines())))
        output = [0] + output + [output[-1] + 3] # Add outlet and built-in adapter
    # Output: [0 (outlet), 1, 2, 3,...highest+3 (built-in adapter)]
    return output

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(35, adapter_array_1(process_input(TEST_INPUT)))
    def test_2(self):
        self.assertEqual(8, adapter_array_2(process_input(TEST_INPUT)))

if __name__ == "__main__":
    unittest.main(exit=False)

    pro_input = process_input(PUZZLE_INPUT)
    print(f"Part 1 Answer: {adapter_array_1(pro_input)}")
    print(f"Part 2 Answer: {adapter_array_2(pro_input)}")
