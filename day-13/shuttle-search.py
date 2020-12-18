import pathlib
import unittest

PUZZLE_INPUT = "input.txt"
TEST_INPUT = "test-input.txt"

def shuttle_search_1(notes: list[int, list[int]]) -> int:
    earliest_timestamp = notes[0]
    bus_ids = notes[1]
    bus_times = bus_ids.copy()
    for index,value in enumerate(bus_times):
        while bus_times[index] < earliest_timestamp:
            bus_times[index] += value
    i = bus_times.index(min(bus_times))
    return bus_ids[i] * (min(bus_times) - earliest_timestamp)

def process_input_1(file_name: str) -> list[int]:
    with (pathlib.Path(__file__).parent / file_name).open() as input_file:
        output = [line.strip() for line in input_file]
        output[0] = int(output[0])
        output[1] = [int(i) for i in output[1].split(',') if i != 'x']
    return output

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(295, shuttle_search_1(process_input_1(TEST_INPUT)))

if __name__ == "__main__":
    unittest.main(exit=False)

    pro_input = process_input_1(PUZZLE_INPUT)
    print(f"Part 1 Answer: {shuttle_search_1(pro_input)}")
