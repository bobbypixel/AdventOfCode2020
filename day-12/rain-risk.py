import pathlib
import parse
import unittest

PUZZLE_INPUT = "input.txt"
TEST_INPUT = "test-input.txt"

def rain_risk_1(nav_instructions: list[list[str, int]]) -> int:
    ship_location = [0, 0, 0, 0] # [W, N, E, S]
    ship_direction = 180
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
            ship_direction -= value
        elif action == 'R':
            ship_direction += value
        elif action == 'F':
            direction = (ship_direction % 360) // 90
            ship_location[direction] += value
    east_west_pos = ship_location[0] - ship_location[2]
    north_south_pos = ship_location[1] - ship_location[3]
    return abs(east_west_pos) + abs(north_south_pos)

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
            waypoint_location = calculate_waypoint_location(waypoint_location)
            new_waypoint_location = [0, 0, 0, 0]
            direction = (value % 360) // 90
            for i in range(len(waypoint_location)):
                if waypoint_location[i] > 0:
                    new_waypoint_location[(i-direction) % 4] = waypoint_location[i]
            waypoint_location = new_waypoint_location
        elif action == 'R':
            waypoint_location = calculate_waypoint_location(waypoint_location)
            new_waypoint_location = [0, 0, 0, 0]
            direction = (value % 360) // 90
            for i in range(len(waypoint_location)):
                if waypoint_location[i] > 0:
                    new_waypoint_location[(i+direction) % 4] = waypoint_location[i]
            waypoint_location = new_waypoint_location
        elif action == 'F':
            for i,j in enumerate(waypoint_location):
                ship_location[i] += j * value
    east_west_pos = ship_location[0] - ship_location[2]
    north_south_pos = ship_location[1] - ship_location[3]
    return abs(east_west_pos) + abs(north_south_pos)

def calculate_waypoint_location(waypoint_location: list[int]) -> list[int]:
    if waypoint_location[0] > waypoint_location[2]:
        waypoint_location[0] = waypoint_location[0] - waypoint_location[2]
        waypoint_location[2] = 0
    elif waypoint_location[2] > waypoint_location[0]:
        waypoint_location[2] = waypoint_location[2] - waypoint_location[0]
        waypoint_location[0] = 0
    else:
        waypoint_location[2] = 0
        waypoint_location[0] = 0

    if waypoint_location[1] > waypoint_location[3]:
        waypoint_location[1] = waypoint_location[1] - waypoint_location[3]
        waypoint_location[3] = 0
    elif waypoint_location[3] > waypoint_location[1]:
        waypoint_location[3] = waypoint_location[3] - waypoint_location[1]
        waypoint_location[1] = 0
    else:
        waypoint_location[3] = 0
        waypoint_location[1] = 0

    return waypoint_location

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
