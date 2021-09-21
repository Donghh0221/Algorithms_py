from collections import Counter


def solution3(gems):
    number_of_gem_category = len(set(gems))

    left_point = 0
    right_point = number_of_gem_category

    total_length = len(gems) - 1
    answer = [0, total_length]

    map_table = dict(Counter(gems[left_point:right_point]))

    while right_point < total_length and left_point < total_length:
        if len(map_table) == number_of_gem_category:
            left_point += 1

            if right_point - left_point < answer[1] - answer[0]:
                answer = [left_point, right_point]

            map_table[gems[left_point]] -= 1
            if map_table[gems[left_point]] == 0:
                map_table.pop(gems[left_point])

        else:
            right_point += 1

            if gems[right_point] in map_table.keys():
                map_table[gems[right_point]] += 1

            else:
                map_table[gems[right_point]] = 1
    answer = [answer[0] + 1, answer[1]]
    return answer


def solution2(gems):
    gem_set = set(gems)

    max_length = len(gems)

    section_length = max_length

    while True:
        if is_there_smaller_section(gems, gem_set, section_length):
            section_length -= 1
        else:
            break

    for i in range(len(gems) - section_length + 1):
        section = gems[i: i + section_length]
        if set(section) == gem_set:
            return [i + 1, i + section_length]


def is_there_smaller_section(gems, gem_set, section_length):
    check_length = section_length - 1
    for i in range(len(gems) - check_length + 1):
        section = gems[i:i + check_length]
        if set(section) == gem_set:
            return True
    return False


def solution(gems):
    gem_set = set(gems)
    section_length = len(gem_set)

    while True:
        for i in range(len(gems) - section_length + 1):
            section = gems[i:i + section_length]
            if set(section) == gem_set:
                return [i + 1, i + section_length]
        section_length += 1


if __name__ == "__main__":
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution3(gems))
