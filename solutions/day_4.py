import re


def count(pattern: str, text: str) -> int:
    return len(re.findall(pattern + r"(?:\s\S|\S)*?\s){7}", text, re.MULTILINE))


def solve_part_1(input_text: str) -> int:
    return count(r"(([bie]yr|hgt|pid|[he]cl):", input_text)


def solve_part_2(input_text: str) -> int:
    return count(
        r"((iyr:20(?:1[0-9]|20)|"  # 2010-2020
        r"byr:(?:19[2-9][0-9]|200[0-2])|"  # 1920-2002
        r"eyr:20(?:2[0-9]|30)|"  # 2020-2030
        r"hgt:(?:1(?:[5-8][0-9]|9[0-3])cm|(?:59|6[0-9]|7[0-6])in)|"  # 150-193cm / 59-76in
        r"hcl:#[0-9a-f]{6}|"  # Hex color
        r"ecl:(?:amb|blu|brn|gry|grn|hzl|oth)|"  # One of
        r"pid:\d{9}(?!\d))",  # 0-999999999
        input_text
    )
