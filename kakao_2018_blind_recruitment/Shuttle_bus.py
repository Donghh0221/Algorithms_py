from collections import Counter

from itertools import accumulate
def solution(n, t, m, timetable):
    converted_timetable = sorted(list(map(convert_HHMM_to_int, timetable)))
    people_count = Counter(converted_timetable)

    val = accumulate(people_count.values())
    key = people_count.keys()


    for i in range(0, n):
        time = 540 + i * t
        if time in people_count.keys():
            people_count[time] -= m
        else:
            people_count[time] = -m



def convert_HHMM_to_int(t: str) -> int:
    converted_time = 60 * int(t[0:2]) + int(t[3:])
    return converted_time


def test_convert_HHMM_to_int():
    assert convert_HHMM_to_int('08:00') == 480
    assert convert_HHMM_to_int('08:01') == 481


if __name__ == "__main__":
    solution(1, 1, 5, ["09:10", "09:09", "08:00", "09:00"])
