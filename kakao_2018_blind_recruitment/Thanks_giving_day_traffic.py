def solution(lines):
    answer = 0
    starts = []
    ends = []

    for log in lines:
        start, end = parser(log)
        start_time = start_time_parser(start)
        end_time = start_time + float(end) + 0.001

        starts.append(start_time)
        ends.append(end_time)

    for start, end in zip(starts, ends):
        count = 0
        for s, e in zip(starts, ends):
            if start <= e and s < end + 1:
                count += 1
        answer = max(count, answer)

    return answer


def parser(line):
    start = line[11:23]
    end = line[24:-1]
    return start, end


def test_parser():
    assert parser("2016-09-15 20:59:57.421 0.351s") == ('20:59:57.421', '0.351')
    assert parser("2016-09-15 20:59:58.299 0.8s") == ('20:59:58.299', '0.8')


def start_time_parser(t: str) -> float:
    return 3600 * float(t[0:2]) + 60 * float(t[3:5]) + float(t[6:])


def test_start_time_parser():
    assert start_time_parser('20:59:57.421') == 20 * 3600 + 59 * 60 + 57.421
    assert start_time_parser('20:59:58.299') == 20 * 3600 + 59 * 60 + 58.299


if __name__ == "__main__":
    print(solution(["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"]))