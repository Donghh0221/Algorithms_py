import collections
import time


def solution(s):
    convert_count = 0
    zero_count = 0
    while s != '1':
        count = collections.Counter(s)
        s = bin(count['1'])[2:]
        zero_count += count['0']
        convert_count += 1
    return [convert_count, zero_count]


print(solution("110010101001"))
