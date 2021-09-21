from collections import defaultdict


def solution(records, k, date):
    num_date = int(date[5:7]) * 30 + int(date[8:10])
    table = record_transform(records, k, num_date)



def record_transform(records, k, num_date):
    table = defaultdict(int)
    for record in records:
        sep = record.split(" ")
        date = int(sep[0][5:7]) * 30 + int(sep[0][8:10])
        if num_date - k < date <= num_date:
            table[sep[1] + sep[2]] += 1
    return table


if __name__ == "__main__":
    records = ["2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1", "2020-02-27 uid3 pid2",
               "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3", "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1",
               "2020-03-04 uid2 pid1", "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3",
               "2020-03-06 uid1 pid4"]
    k = 10
    date = "2020-03-05"
    solution(records, k, date)
