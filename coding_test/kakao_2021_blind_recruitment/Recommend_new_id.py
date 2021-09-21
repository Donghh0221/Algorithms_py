import re


def solution(new_id: str):
    first_step_id = new_id.lower()

    second_step_id = second_step(first_step_id)

    third_step_id = third_step(second_step_id)

    fourth_step_id = fourth_step(third_step_id)
    if len(fourth_step_id) == 0:
        fifth_step_id = "a"
    else:
        fifth_step_id = fourth_step_id
    if len(fifth_step_id) > 15:
        sixth_step_id = fifth_step_id[0:15]
        if sixth_step_id[-1] == ".":
            sixth_step_id = sixth_step_id[:-1]
    else:
        sixth_step_id = fifth_step_id

    while len(sixth_step_id) < 3:
        sixth_step_id += sixth_step_id[-1]

    answer = sixth_step_id
    return answer


def second_step(first_step_id: str):
    second_step_id = re.sub(r'[^\w\_\.\-]', '', first_step_id)
    return second_step_id


def test_second_step():
    first_step_id = "...!@bat#*..y.abcdefghijklm"
    s = second_step(first_step_id)
    assert s == "...bat..y.abcdefghijklm"


def third_step(second_step_id: str):
    third_step_id = re.sub('[.]{2,}', '.', second_step_id)
    return third_step_id


def test_third_step():
    second_step_id = "...bat..y.abcdefghijklm"
    third_step_id = third_step(second_step_id)
    assert third_step_id == ".bat.y.abcdefghijklm"


def fourth_step(third_step_id: str):
    if len(third_step_id) > 0:
        if third_step_id[0] == ".":
            third_step_id = third_step_id[1:]

    if len(third_step_id) > 0:
        if third_step_id[-1] == ".":
            third_step_id = third_step_id[:-1]

    fourth_step_id = third_step_id
    return fourth_step_id


def test_fourth_step():
    third_step_id = ".bat.y.abcdefghijklm"
    fourth_step_id = fourth_step(third_step_id)
    assert fourth_step_id == "bat.y.abcdefghijklm"

    third_step_id = ".bat.y.abcdefghijklm."
    fourth_step_id = fourth_step(third_step_id)
    assert fourth_step_id == "bat.y.abcdefghijklm"


if __name__ == "__main__":
    new_id = "abcdefghijklmn.p"
    print(solution(new_id))
