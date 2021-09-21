import math


def solution(n, k):
    answer = 0

    converted_num = convert_to_k(n, k)

    nums = converted_num.split("0")
    target_nums = [int(x) for x in nums if x.isdigit() and int(x) > 1]

    for num in target_nums:
        if is_prime_num(num):
            answer += 1
    return answer


def is_prime_num(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def convert_to_k(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]


def test_convertor():
    assert convert_to_k(437674, 3) == '211020101011'
    assert convert_to_k(110011, 10) == '110011'
    assert convert_to_k(1, 3) == '1'


if __name__ == "__main__":
    print(solution(437674, 3	))
