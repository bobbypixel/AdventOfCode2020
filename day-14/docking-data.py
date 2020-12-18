import pathlib
import unittest
import re
import itertools

PUZZLE_INPUT = "input.txt"
TEST_INPUT_1 = "test-input-1.txt"
TEST_INPUT_2 = "test-input-2.txt"

def docking_data_1(init_program: list[str, dict]) -> int:
    results = {}
    for program in init_program:
        mask = program[0]
        mems = program[1]
        for mem in mems:
            mem_value = "{0:036b}".format(mems[mem])
            new_mem_value = ""
            for index,value in enumerate(mask):
                if value != 'X':
                    new_mem_value += value
                else:
                    new_mem_value += mem_value[index]
            results[mem] = (int(new_mem_value, 2))
    return sum(results.values())

def docking_data_2(init_program: list[str, dict]) -> int:
    results = {}
    for program in init_program:
        mask = program[0]
        mems = program[1]

        for mem in mems:
            address = "{0:036b}".format(mem)
            result = ""
            for index,value in enumerate(mask):
                if value != '0':
                    result += value
                else:
                    result += address[index]
            program_addresses = []

            # Get all combinations of floating bits and their indexes
            n = result.count('X')
            floating_bits = list(map(list, itertools.product([0, 1], repeat=n)))
            floating_bits_index = list(filter(lambda x: result[x] == 'X', range(len(result))))

            for i in floating_bits:
                new_address = list(result)
                for j in range(len(i)):
                    new_address[floating_bits_index[j]] = i[j]
                new_address = "".join(map(str, new_address))
                program_addresses.append("".join(new_address))
                results[new_address] = mems[mem]

    return sum(results.values())

def process_input(file_name: str) -> list[str, dict]:
    with (pathlib.Path(__file__).parent / file_name).open() as input_file:
        output = []
        group = []
        mems = {}
        for line in input_file:
            line = line.strip()
            if line[:4] == "mask":
                if group != []:
                    group.append(mems)
                    output.append(group)
                group = []
                mems = {}
                group.append(line[7:])
            else:
                mem = "".join(line.split()).split("=")
                mem_address = mem[0]
                pattern = re.compile(r"\[[0-9]+\]")
                mem_address = re.search(pattern, mem_address)[0]
                value = int(mem[1])
                mems[int(mem_address[1:-1])] = value
        group.append(mems)
        output.append(group)
    return output

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(165, docking_data_1(process_input(TEST_INPUT_1)))
    def test_2(self):
        self.assertEqual(208, docking_data_2(process_input(TEST_INPUT_2)))

if __name__ == "__main__":
    unittest.main(exit=False)

    pro_input = process_input(PUZZLE_INPUT)
    print(f"Part 1 Answer: {docking_data_1(pro_input)}")
    print(f"Part 2 Answer: {docking_data_2(pro_input)}")
