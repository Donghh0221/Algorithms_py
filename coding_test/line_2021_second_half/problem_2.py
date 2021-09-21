from collections import defaultdict


def solution(research, n, k):
    search_word = set()
    word_table = defaultdict(list)

    for record in research:
        search_word = search_word | set(record)

    for word in search_word:
        for record in research:
            word_table[word].append(record.count(word))

    table = defaultdict(int)
    for word in search_word:
        for start_day in range(len(research) - n + 1):
            window = word_table[word][start_day:start_day + n]
            if min(window) >= k and sum(window) >= 2 * n * k:
                table[word] += 1

    if len(table) < 1:
        return "None"

    return sorted(table.items(), key=lambda item: (-item[1], item[0]))[0][0]


if __name__ == "__main__":
    solution(["yxxy", "xxyyy"], 2, 1)
