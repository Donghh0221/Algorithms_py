import re
from collections import Counter
from math import floor


def solution(str1, str2):
    lower_str1, lower_str2 = str1.lower(), str2.lower()
    duplicated_set_1 = re.findall(r'(?=([a-z]{2}))', lower_str1)
    duplicated_set_2 = re.findall(r'(?=([a-z]{2}))', lower_str2)
    union = Counter(duplicated_set_1) | Counter(duplicated_set_2)
    intersection = Counter(duplicated_set_1) & Counter(duplicated_set_2)
    numerator = sum(intersection.values())
    denominator = sum(union.values())

    if denominator == 0:
        return 65536

    j = sum(intersection.values())/sum(union.values())
    return floor(j * 65536)


if __name__ == "__main__":
    print(solution('E=M*C^2', 'e=m*c^2'))
