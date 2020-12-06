import pathlib

PUZZLE_INPUT = "input.txt"

def custom_customs_1(customs: list[list[str]]) -> int:
    counts = 0
    for group in customs:
        group_set = set("".join(group))
        counts += len(group_set)
    return counts

def custom_customs_2(customs: list[list[str]]) -> int:
    counts = 0
    for group in customs:
        group_set = set("".join(group))
        for letter in group_set:
            if all(letter in person for person in group):
                counts += 1
    return counts

def process_input_file(file_name: str) -> list[list[str]]:
    with (pathlib.Path(__file__).parent / file_name).open() as input_file:
        groups = []
        current = []
        for line in (l.strip() for l in input_file):
            if line:
                current.append(line)
            else:
                groups.append(current)
                current = []
        groups.append(current)
    return groups

if __name__ == "__main__":
    pro_input = process_input_file(PUZZLE_INPUT)
    print(f"Part 1 Answer: {custom_customs_1(pro_input)}")
    print(f"Part 2 Answer: {custom_customs_2(pro_input)}")
