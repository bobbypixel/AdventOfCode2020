import io
import pathlib

PUZZLE_INPUT = "input.txt"

def get_seat_ids(boarding_passes: list[str]) -> list[int]:
    seat_IDs  = []
    for boarding_pass in boarding_passes:
        rows, row_range = 128, [i for i in range(128)]
        columns, column_range = 8, [i for i in range(8)]
        for c in range(len(boarding_pass)):
            # rows
            if c < 7:
                rows = rows // 2
                if boarding_pass[c] == 'F':
                    for i in range(rows):
                        row_range.pop()
                elif boarding_pass[c] == 'B':
                    for i in range(rows):
                        row_range.pop(0)
            # columns
            else:
                columns = columns // 2
                if boarding_pass[c] == 'L':
                    for i in range(columns):
                        column_range.pop()
                if boarding_pass[c] == 'R':
                    for i in range(columns):
                        column_range.pop(0)
        seat_ID = row_range[0] * 8 + column_range[0]
        seat_IDs.append(seat_ID)
    return sorted(seat_IDs)

def binary_boarding_1(boarding_passes: list[str]) -> int:
    return max(get_seat_ids(boarding_passes))

def binary_boarding_2(boarding_passes: list[str]) -> int:
    seat_IDs = get_seat_ids(boarding_passes)
    current = seat_IDs[0]
    for i in range(len(seat_IDs)):
        if current != seat_IDs[i]:
            return current
        current += 1
    return None

def process_input_file(input_file: io.TextIOWrapper) -> list[str]:
    return [line.strip() for line in input_file if line.strip()]

if __name__ == "__main__":
    input_file_path = (pathlib.Path(__file__).parent / PUZZLE_INPUT)
    with input_file_path.open() as input_file:
        input = process_input_file(input_file)

    print(f"Part 1 Answer: {binary_boarding_1(input)}")
    print(f"Part 2 Answer: {binary_boarding_2(input)}")
