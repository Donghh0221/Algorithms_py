import math
from collections import defaultdict


def solution(fees, records):
    answer = []
    time_table = defaultdict(int)
    cum_table = defaultdict(int)
    last_time = 1439
    for record in records:
        time, car_num, in_out = record.split(" ")
        num_time = convert_time(time)
        if in_out == "IN":
            time_table[car_num] = num_time
        else:
            cum_table[car_num] += num_time - time_table[car_num]
            del time_table[car_num]

    for k, v in time_table.items():
        cum_table[k] += last_time - v

    for k, v in sorted(cum_table.items()):
        answer.append(calculator(v, fees))

    return answer


def calculator(time, fees):
    payed_money = 0
    base_time, base_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
    payed_money += base_fee
    unit_pay_time = max(0, time - base_time)
    unit = math.ceil(unit_pay_time/unit_time)
    payed_money += unit * unit_fee
    return payed_money


def convert_time(time: str):
    return int(time[0:2]) * 60 + int(time[3:])


if __name__ == "__main__":
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
               "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    print(solution(fees, records))
