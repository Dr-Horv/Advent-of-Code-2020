


def solve(data, part_two=False):
    valid = 0
    for l in data:
        (policy, password) = [p.strip() for p in l.split(":")]
        (policy_range, letter) = [p.strip() for p in policy.split(" ")]
        (policy_number_1,policy_number_2) = [int(p) for p in policy_range.split("-")]
        if not part_two:
            count = password.count(letter)
            if policy_number_1 <= count <= policy_number_2:
                valid = valid + 1
        else:
            first_letter = "-1"
            second_letter = "-2"
            pn1 = policy_number_1-1
            pn2 = policy_number_2-1
            if len(password) > pn1:
                first_letter = password[pn1]
            if len(password) > pn2:
                second_letter = password[pn2]
            if first_letter != second_letter and (first_letter == letter or second_letter == letter):
                valid = valid + 1

    return valid