from io import TextIOBase
import pathlib
import re

PUZZLE_INPUT = "input.txt"
REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def passport_processing_1(passports: list[str]) -> int:
    valid_passports = 0

    for person in passports:
        field_counter = 0
        for field in person:
            for r in REQUIRED_FIELDS:
                if r in field:
                    field_counter += 1
        if field_counter == len(REQUIRED_FIELDS):
            valid_passports += 1

    return valid_passports

def passport_processing_2(passports: list[str]) -> int:
    valid_passports = 0
    
    for person in passports:
        field_counter = 0
        for field in person:
            for i in range(len(REQUIRED_FIELDS)):
                if REQUIRED_FIELDS[i] in field:
                    n = field.split(":")[1]
                    if i == 0:
                        if 1920 <= int(n) <= 2002:
                            field_counter += 1
                    elif i == 1:
                        if 2010 <= int(n) <= 2020:
                            field_counter += 1
                    elif i == 2:
                        if 2020 <= int(n) <= 2030:
                            field_counter += 1
                    elif i == 3:
                        if (
                            (n[-2:] == "cm" and 150 <= int(n[:-2]) <= 193) or
                            (n[-2:] == "in" and 59 <= int(n[:-2]) <= 76)
                        ):
                            field_counter += 1
                    elif i == 4:
                        if n[0] == "#" and re.match(r"^[a-f0-9]{6}$", n[1:]):
                            field_counter += 1
                    elif i == 5:
                        for color in EYE_COLORS:
                            if n == color:
                                field_counter += 1
                    elif i == 6:
                        if re.match(r"^[0-9]{9}$", n):
                            field_counter += 1
        if field_counter == len(REQUIRED_FIELDS):
            valid_passports += 1
            
    return valid_passports

def process_input_file(input_file: TextIOBase):
    passport_list = []
    person = []
    lines = input_file.readlines()

    for line in lines:
        for field in line.strip().split():
            person.append(field)
        if line == "\n" or line is lines[-1]:
            passport_list.append(person)
            person = []

    return passport_list

if __name__ == "__main__":
    with (pathlib.Path(__file__).parent / PUZZLE_INPUT).open() as input_file:
        input = process_input_file(input_file)
        print(f"Part 1 Answer: {passport_processing_1(input)}")
        print(f"Part 2 Answer: {passport_processing_2(input)}")
