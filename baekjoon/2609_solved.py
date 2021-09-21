def get_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def get_lcm(a: int, b: int, gcd: int) -> int:
    return (a * b) // gcd


N, M = map(int, input().split())

gcd = get_gcd(N, M)
lcm = get_lcm(N, M, gcd)

print(gcd)
print(lcm)
