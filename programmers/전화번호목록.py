from collections import defaultdict


def solution(phone_book):
    table = defaultdict(int)
    phone_book = sorted(phone_book, key=len)
    min_len = len(phone_book[0])

    for num in phone_book:
        for i in range(min_len, len(num) + 1):
            if table[num[:i]]:
                return False
        table[num] = 1
    return True


if __name__ == "__main__":
    phone_book = ["12", "123", "1235", "567", "88"]
    print(solution(phone_book))
