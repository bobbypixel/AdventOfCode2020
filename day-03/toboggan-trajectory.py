from __future__ import annotations
import unittest

def toboggan_trajectory_1(input_map: list[chr], slope: list[int]) -> int:
    x, y = 0, 0 # starting point
    trees = 0 # tree counter
    
    while y < len(input_map) - 1:
        # move right
        x += slope[0]

        # loopback the repeating line
        if x > len(input_map[y]) - 1:
            x = x - len(input_map[y])

        # move down
        y += slope[1]

        # check tree
        if input_map[y][x] == "#":
            trees += 1
    return trees

def toboggan_trajectory_2(input_map: list[chr], *slopes: list[int]) -> int:
    multiply = 1
    for slope in slopes:
        multiply *= toboggan_trajectory_1(input_map, slope)
    return multiply

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, toboggan_trajectory_1([ \
            "..##.........##.........##.........##.........##.........##.......", \
            "#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..", \
            ".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.", \
            "..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#", \
            ".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.", \
            "..#.##.......#.##.......#.##.......#.##.......#.##.......#.##....."], \
            [3, 1]))
        
if __name__ == "__main__":
    # Optional tests
    # unittest.main()

    import pathlib
    with (pathlib.Path(__file__).parent / "puzzle-input.txt").open() as input_file:
        input_map = [line.strip() for line in input_file if line.strip()]
        print(f"Part 1 Answer: {toboggan_trajectory_1(input_map, [3,1])}")
        print(f"Part 2 Answer: {toboggan_trajectory_2(input_map, [1,1], [3,1], [5,1], [7,1], [1,2])}")
