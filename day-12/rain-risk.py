import pathlib
import parse
import unittest

PUZZLE_INPUT = "input.txt"
TEST_INPUT = "test-input.txt"

def rain_risk_1(nav_instructions: list[list[str, int]]) -> int:
    ship_location = [0, 0, 0, 0] # [W, N, E, S]
    ship_direction = 180 # Ship starts facing east
    for action,value in nav_instructions:
        if action == 'N':
            ship_location[1] += value
        elif action == 'E':
            ship_location[2] += value
        elif action == 'S':
            ship_location[3] += value
        elif action == 'W':
            ship_location[0] += value
        elif action == 'L':
            ship_direction += -value
        elif action == 'R':
            ship_direction += value
        elif action == 'F':
            direction = (ship_direction % 360) // 90
            ship_location[direction] += value
    return abs(ship_location[0] - ship_location[2]) + abs(ship_location[1] - ship_location[3])

def rain_risk_2(nav_instructions: list[list[str, int]]) -> int:
    ship_location = [0, 0, 0, 0] # [W, N, E, S]
    waypoint_location = [0, 1, 10, 0] # [W, N, E, S]
    for action,value in nav_instructions:
        if action == 'N':
            waypoint_location[1] += value
        elif action == 'E':
            waypoint_location[2] += value
        elif action == 'S':
            waypoint_location[3] += value
        elif action == 'W':
            waypoint_location[0] += value
        elif action == 'L':
            waypoint_location = rotate_waypoint(waypoint_location, value, action)
        elif action == 'R':
            waypoint_location = rotate_waypoint(waypoint_location, value, action)
        elif action == 'F':
            for i,j in enumerate(waypoint_location):
                ship_location[i] += j * value
    return abs(ship_location[0] - ship_location[2]) + abs(ship_location[1] - ship_location[3])

def rotate_waypoint(waypoint_location: list[int], value: int, action: chr) -> list[int]:
    new_waypoint_location = [0, 0, 0, 0]
    direction = (value % 360) // 90 * {'L': -1, 'R': 1}[action]
    for i in range(len(waypoint_location)):
        new_waypoint_location[(i+direction) % 4] = waypoint_location[i]
    return new_waypoint_location

def process_input(file_name: str) -> list[int]:
    with (pathlib.Path(__file__).parent / file_name).open() as input_file:
        pattern = parse.compile("{}{:d}")
        output = [pattern.parse(line).fixed for line in input_file if line.strip()]
    return output

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(25, rain_risk_1(process_input(TEST_INPUT)))
    def test_2(self):    
        self.assertEqual(286, rain_risk_2(process_input(TEST_INPUT)))

if __name__ == "__main__":
    unittest.main(exit=False)

    pro_input = process_input(PUZZLE_INPUT)
    print(f"Part 1 Answer: {rain_risk_1(pro_input)}")
    print(f"Part 2 Answer: {rain_risk_2(pro_input)}")
