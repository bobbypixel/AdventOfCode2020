import pathlib
import unittest
import copy

PUZZLE_INPUT = "input.txt"
TEST_INPUT = "test-input.txt"

def handheld_halting_1(instructions: list[list[str, int]]) -> int:
    curr_line = 0 # current index of instruction running
    old_instructions = [] # indexes of old instructions
    accumulator = 0 # program will add to this as it runs
    
    # Run until the program tries to run any line a second time
    while curr_line not in old_instructions:
        old_instructions.append(curr_line)
        operation = instructions[curr_line][0]
        argument = instructions[curr_line][1]
        if operation == "acc":
            accumulator += argument
            curr_line += 1
        elif operation == "jmp":
            curr_line += argument
        elif operation == "nop":
            curr_line += 1

    return accumulator

def handheld_halting_2(instructions: list[list[str, int]]) -> int:
    # Make a list of nop and jmp found in the instructions
    nop_jmp = []
    for i,j in enumerate(instructions):
        if j[0] in ("nop", "jmp"):
            nop_jmp.append(i)
            
    # Make new instructions by changing jmp and nop
    new_instructions = []
    for i in nop_jmp:
        new = copy.deepcopy(instructions)
        new[i][0] = ("jmp" if new[i][0] == "nop" else "nop")
        new_instructions.append(new)

    # Run until a new instruction terminates correctly
    curr_line = 0 # current index of instruction running
    old_lines = [] # list of indexes of old lines that were run
    for i in range(len(new_instructions)):   
        accumulator = 0 # program will add to this as it runs
        while curr_line < len(new_instructions[i]):
            operation = new_instructions[i][curr_line][0]
            argument = new_instructions[i][curr_line][1]
            if operation == "acc":
                accumulator += argument
                curr_line += 1
            elif operation == "jmp":
                curr_line += argument
            elif operation == "nop":
                curr_line += 1
            
            # If infinite loop, break and try the next new instruction.
            if curr_line in old_lines:
                curr_line = 0
                old_lines = []
                accumulator = 0
                break
            
            old_lines.append(curr_line)
        
        # Program correctly terminated
        if curr_line >= len(new_instructions[i]):
            return accumulator

def process_input(file_name: str) -> list[list[str, int]]:
    with (pathlib.Path(__file__).parent / file_name).open() as input_file:
        lines = input_file.read().splitlines()
        output = []
        for l in (i.split() for i in lines):
            output.append([l[0], int(l[1])])
    # Output:
    # [
    #   [operation_1, argument_1],
    #   [operation_2, argument_2],
    #   ...
    # ]
    return output

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(5, handheld_halting_1(process_input(TEST_INPUT)))
    def test_2(self):
        self.assertEqual(8, handheld_halting_2(process_input(TEST_INPUT)))

if __name__ == "__main__":
    unittest.main(exit=False)

    pro_input = process_input(PUZZLE_INPUT)
    print(f"Part 1 Answer: {handheld_halting_1(pro_input)}")
    print(f"Part 2 Answer: {handheld_halting_2(pro_input)}")
