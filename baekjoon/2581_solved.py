import math


def get_prime_list(n):
    sieve = [True] * n
    m = math.ceil(math.sqrt(n))
    for i in range(2, m):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i]]


M = int(input())
N = int(input())

primes = get_prime_list(N+1)
primes = [x for x in primes if M <= x]

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])
