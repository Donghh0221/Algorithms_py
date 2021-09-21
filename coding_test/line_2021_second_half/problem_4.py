import math


def solution(n):
    array = range(1, n + 1)
    #재귀로 처리

def shuffle(array):
    length = len(array)
    maximum_n = math.floor(math.sqrt(length))
    candidate_nums = get_prime_list(maximum_n)
    n = 1

    for prime_num in candidate_nums:
        pair = divmod(length, prime_num)
        if pair[1] == 0:
            n = prime_num
            break

    if n == 1:
        return array, n

    new_array = [[] for _ in range(n)]

    for idx in range(length):
        new_array[idx % n].append(array[idx])

    return new_array, n


def test_shuffle():
    assert shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])[0] == [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12]]
    assert shuffle([1, 3, 5, 7, 9, 11])[0] == [[1, 5, 9], [3, 7, 11]]
    assert shuffle([2, 4, 6, 8, 10, 12])[0] == [[2, 6, 10], [4, 8, 12]]
    assert shuffle([1, 5, 9])[0] == [1, 5, 9]


def get_prime_list(num):
    primes = []
    if num < 2:
        return primes
    for i in range(2, num + 1):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
            elif j > i ** 0.5:
                break
        if is_prime:
            primes.append(i)
    return primes


if __name__ == '__main__':
    print(solution(12))
