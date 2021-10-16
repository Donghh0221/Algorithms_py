def solution(n):
    ternary_num = decimal_to_ternary(n)
    reversed_ternary_num = ternary_num[::-1]
    answer = ternary_to_decimal(reversed_ternary_num)
    return answer


def decimal_to_ternary(decimal_num: int) -> str:
    rev_base = ''
    while decimal_num > 0:
        decimal_num, mod = divmod(decimal_num, 3)
        rev_base += str(mod)
    return rev_base[::-1]


def ternary_to_decimal(ternary_num: str) -> int:
    return int(ternary_num, 3)
