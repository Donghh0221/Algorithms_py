from collections import defaultdict


def solution(id_list, report, k):
    answer = []

    report_table = defaultdict(set)
    reported_table = defaultdict(set)
    for r in report:
        reporter, poor_user = r.split(" ")
        report_table[reporter].add(poor_user)
        reported_table[poor_user].add(reporter)

    banned_user = set()
    for reported_user, s in reported_table.items():
        if k <= len(s):
            banned_user.add(reported_user)

    for user_id in id_list:
        answer.append(len(set(report_table[user_id]) & banned_user))

    return answer


if __name__ == "__main__":
    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    print(solution(id_list, report, k))
