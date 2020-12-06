import string

def solve(data, part_two=False):
    valid_passports = 0
    total_passports = 1
    passport = dict()
    i = 0
    for l in data:
        if len(l) == 0:
            if not part_two and check_passport_part1(passport):
                valid_passports += 1
            elif part_two and check_passport_part2(passport):
                valid_passports += 1
            passport = dict()
            total_passports += 1


        for p in l.split(" "):
            if len(p) == 0:
                continue
            (key, value) = p.split(":")
            passport[key] = value
        i += 1

    if not part_two and check_passport_part1(passport):
        valid_passports += 1
    elif part_two and check_passport_part2(passport):
        valid_passports += 1

    return valid_passports


def check_passport_part1(passport):
    return all((prop in passport) for prop in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def check_passport_part2(passport):
    if all((prop in passport) for prop in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
        if not (1920 <= int(passport["byr"]) <= 2002):
            return False
        if not (2010 <= int(passport["iyr"]) <= 2020):
            return False
        if not (2020 <= int(passport["eyr"]) <= 2030):
            return False
        height = passport["hgt"]
        height_type = height[-2:]
        if height_type == "cm":
            if not (150 <= int(height[:-2]) <= 193):
                return False
        elif height_type == "in":
            if not (59 <= int(height[:-2]) <= 76):
                return False
        else:
            return False
        if len(passport["hcl"]) != 7 or not all((c in string.hexdigits) for c in passport["hcl"][1:]):
            return False
        if not passport["ecl"] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        if len(passport["pid"]) != 9 or not all((c in string.digits) for c in passport["pid"]):
            return False

        return True


