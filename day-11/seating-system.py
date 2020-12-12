import pathlib
import unittest

PUZZLE_INPUT = "input.txt"
TEST_INPUT = "test-input.txt"

def seating_system_1(layout: list[str]) -> int:
    old_layout = layout
    new_layout = occupy_seats(old_layout)
    while new_layout != old_layout:
        old_layout = new_layout 
        new_layout = occupy_seats(leave_seats(old_layout))
    return sum(seat == '#' for row in new_layout for seat in row)

def occupy_seats(layout: list[str]) -> list[str]:
    new_layout = layout.copy()
    for i,row in enumerate(new_layout):
        for j,seat in enumerate(row):
            all_adjacents = find_adjacent_seats(layout, i, j)
            if seat == 'L' and '#' not in (all_adjacents):
                new_layout[i] = new_layout[i][:j] + '#' + new_layout[i][j+1:]
    return new_layout

def leave_seats(layout: list[str]) -> list[str]:
    new_layout = layout.copy()
    for i,row in enumerate(new_layout):
        for j,seat in enumerate(row):
            all_adjacents = find_adjacent_seats(layout, i, j)
            if seat == '#' and all_adjacents.count('#') > 3:
                new_layout[i] = new_layout[i][:j] + 'L' + new_layout[i][j+1:]
    return new_layout

def find_adjacent_seats(layout: list[str], row: int, col: int) -> list[str]:
    top_adjacents = ['.', '.', '.']
    side_adjacents = ['.', '.']
    bot_adjacents = ['.', '.', '.']
    
    # Get top adjacent seat
    if row > 0:
        top_adjacents[1] = layout[row-1][col]

    # Get bottom adjacent seat
    if row < len(layout)-1:
        bot_adjacents[1] = layout[row+1][col]
    
    if col > 0:
        # Get left adjacent seat
        side_adjacents[0] = layout[row][col-1]
        if row > 0:
            # Get top left adjacent seat
            top_adjacents[0] = layout[row-1][col-1]
        if row < len(layout)-1:
            # Get bottom left adjacent seat
            bot_adjacents[0] = layout[row+1][col-1]

    if col < len(layout[row])-1:
        # Get right adjacent seat
        side_adjacents[1] = layout[row][col+1]
        if row > 0:
            # Get top right adjacent seat
            top_adjacents[2] = layout[row-1][col+1]
        if row < len(layout)-1:
            # Get bottom right adjacent seat
            bot_adjacents[2] = layout[row+1][col+1]
 
    return top_adjacents + side_adjacents + bot_adjacents

def seating_system_2(layout: list[str]) -> int:
    old_layout = layout
    new_layout = occupy_seats_2(old_layout)
    while new_layout != old_layout:
        old_layout = new_layout 
        new_layout = occupy_seats_2(leave_seats_2(old_layout))
    return sum(seat == '#' for row in new_layout for seat in row)

def occupy_seats_2(layout: list[str]) -> list[str]:
    new_layout = layout.copy()
    for i,row in enumerate(new_layout):
        for j,seat in enumerate(row):
            all_adjacents = find_adjacent_seats_2(layout, i, j)
            if seat == 'L' and '#' not in (all_adjacents):
                new_layout[i] = new_layout[i][:j] + '#' + new_layout[i][j+1:]
    return new_layout

def leave_seats_2(layout: list[str]) -> list[str]:
    new_layout = layout.copy()
    for i,row in enumerate(new_layout):
        for j,seat in enumerate(row):
            all_adjacents = find_adjacent_seats_2(layout, i, j)
            if seat == '#' and all_adjacents.count('#') > 4:
                new_layout[i] = new_layout[i][:j] + 'L' + new_layout[i][j+1:]
    return new_layout

def find_adjacent_seats_2(layout: list[str], row: int, col: int) -> list[str]:
    top_adjacents = ['.', '.', '.']
    side_adjacents = ['.', '.']
    bot_adjacents = ['.', '.', '.']
    
    # Get adjacent seat to the top
    if row > 0:
        i = row
        while top_adjacents[1] == '.' and i > 0:
            i -= 1
            top_adjacents[1] = layout[i][col]

    # Get adjacent seat to the bottom
    if row < len(layout)-1:
        i = row
        while bot_adjacents[1] == '.' and i < len(layout)-1:
            i += 1
            bot_adjacents[1] = layout[i][col]
        
    if col > 0:
        # Get adjacent seat to the left
        i = col
        while side_adjacents[0] == '.' and i > 0:
            i -= 1
            side_adjacents[0] = layout[row][i]

        # Get adjacent seat to the diagonal top left
        if row > 0:
            i = row
            j = col
            while top_adjacents[0] == '.' and i > 0 and j > 0:
                i -= 1
                j -= 1
                top_adjacents[0] = layout[i][j]

        # Get adjacent seat to the diagonal bottom left
        if row < len(layout)-1:
            i = row
            j = col
            while bot_adjacents[0] == '.' and i < len(layout)-1 and j > 0:
                i += 1
                j -= 1
                bot_adjacents[0] = layout[i][j]

    if col < len(layout[row])-1:
        # Get adjacent seat to the right
        i = col
        while side_adjacents[1] == '.' and i < len(layout[row])-1:
            i += 1
            side_adjacents[1] = layout[row][i]

        # Get adjacent seat to the diagonal top right
        if row > 0:
            i = row
            j = col
            while top_adjacents[2] == '.' and i > 0 and j < len(layout[i])-1:
                i -= 1
                j += 1
                top_adjacents[2] = layout[i][j]

        # Get adjacent seat to the diagonal bottom right
        if row < len(layout)-1:
            i = row
            j = col
            while bot_adjacents[2] == '.' and i < len(layout)-1 and j < len(layout[i])-1:
                i += 1
                j += 1
                bot_adjacents[2] = layout[i][j]
 
    return top_adjacents + side_adjacents + bot_adjacents

def process_input(file_name: str) -> list[int]:
    with (pathlib.Path(__file__).parent / file_name).open() as input_file:
        output = [line.strip() for line in input_file]
    return output

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(37, seating_system_1(process_input(TEST_INPUT)))
    def test_2(self):
        self.assertEqual(26, seating_system_2(process_input(TEST_INPUT)))

if __name__ == "__main__":
    unittest.main(exit=False)

    pro_input = process_input(PUZZLE_INPUT)
    print(f"Part 1 Answer: {seating_system_1(pro_input)}")
    print(f"Part 1 Answer: {seating_system_2(pro_input)}")
