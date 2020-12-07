import pathlib
import re
import unittest

PUZZLE_INPUT = "input.txt"
TEST_INPUT = "test-input.txt"

def handy_haversacks_1(rules: list[list[str, list[str, int]]]) -> int:
    count = 0
    main_bags = []
    for bag_group in rules:
        main_bags.append(bag_group[0])
    for bag_group in rules:
        count += min(1, check_bag(0, "shiny gold", bag_group, rules, main_bags))
    return count

def check_bag(count: int, special_bag: str, bag_group: list[str, list[str, int]], rules: list[str, list[str, int]], main_bags: list[str]) -> int:
    if len(bag_group) == 1:
        return count
    for bag in bag_group[1:]:
        if special_bag in bag[0]:
            return 1
        elif bag[0] in main_bags:
            inner_bag_group = rules[main_bags.index(bag[0])]
            count += check_bag(count, special_bag, inner_bag_group, rules, main_bags)
    return count

def handy_haversacks_2(rules: list[list[str, list[str]]]):
    main_bags = []
    for bag_group in rules:
        main_bags.append(bag_group[0])
    bag_group = rules[main_bags.index("shiny gold")]
    check_bag_2(bag_group, rules, main_bags)

def check_bag_2(bag_group: list[str, list[str, int]], rules: list[str, list[str, int]], main_bags: list[str]):
    global count_2
    for bag in bag_group[1:]:
        count_2 += bag[1]
        for i in range(bag[1]):
            inner_bag_group = rules[main_bags.index(bag[0])]
            check_bag_2(inner_bag_group, rules, main_bags)
    
def process_input_file(file_name: str) -> list[list[str, list[str]]]:
    with (pathlib.Path(__file__).parent / file_name).open() as input_file:
        rules = []
        for line in (l.strip() for l in input_file):
            bag_group = []
            bag_list = line.split("contain")
            bag_group.append(bag_list[0].strip().rsplit(' ', 1)[0])
            if "no other bags" not in bag_list[1]:
                for bag in (b.strip() for b in bag_list[1].split(", ")):
                    sec_bag_list = []
                    color = re.search(r"(\w+) (\w+) (bag)|s", bag)[0].rsplit(' ', 1)[0]
                    amount = int(re.match(r"\d", bag)[0])
                    sec_bag_list.append(color)
                    sec_bag_list.append(amount)
                    bag_group.append(sec_bag_list)
            rules.append(bag_group)
    # rules look like this:
    # [ 
    #   [main_bag, [secondary_bag_1, amount], [secondary_bag_2, amount]],
    #   [main_bag_2, [secondary_bag_1, amount], [secondary_bag_2, amount]],
    #   ...
    # ]
    return rules

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, handy_haversacks_1(process_input_file(TEST_INPUT)))
        
    def test_2(self):
        handy_haversacks_2(process_input_file(TEST_INPUT))
        self.assertEqual(32, count_2)

if __name__ == "__main__":
    count_2 = 0
    unittest.main(exit=False)
    
    pro_input = process_input_file(PUZZLE_INPUT)
    
    print(f"Part 1 Answer: {handy_haversacks_1(pro_input)}")
    
    count_2 = 0
    handy_haversacks_2(pro_input)
    print(f"Part 2 Answer: {count_2}")
    
