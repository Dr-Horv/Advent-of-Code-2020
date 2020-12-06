def solve(data, part_two=False):
    questions = set()
    yes_count = 0
    everyone_count = 0
    count = dict()
    people = 0

    for l in data:
        if len(l) == 0:
            yes_count += len(questions)
            everyone_count += len([q for q in questions if people == count[q]])
            questions = set()
            count = dict()
            people = 0
            continue

        people += 1
        for c in l:
            questions.add(c)
            count[c] = count.get(c, 0) + 1


    yes_count += len(questions)
    everyone_count += len([q for q in questions if people == count[q]])
    if not part_two:
        return yes_count
    else:
        return everyone_count
