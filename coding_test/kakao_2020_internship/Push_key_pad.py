def solution(numbers, hand):
    key = [1, 2, 3,
           4, 5, 6,
           7, 8, 9,
           '*', 0, '#']
    coordinate = [[0, 0], [1, 0], [2, 0],
                  [0, 1], [1, 1], [2, 1],
                  [0, 2], [1, 2], [2, 2],
                  [0, 3], [1, 3], [2, 3]]

    key_map = dict(zip(key, coordinate))

    result = ''

    left_hand = key_map['*']
    right_hand = key_map['#']

    def choose_hand_for_move(l, r, next_number, hand):
        left_distance = abs(l[0] - key_map[next_number][0]) + abs(l[1] - key_map[next_number][1])
        right_distance = abs(r[0] - key_map[next_number][0]) + abs(r[1] - key_map[next_number][1])

        if left_distance > right_distance:
            return 'right'

        elif right_distance > left_distance:
            return 'left'

        return hand

    for number in numbers:
        if number in [1, 4, 7]:
            left_hand = key_map[number]
            result += 'L'
        elif number in [3, 6, 9]:
            right_hand = key_map[number]
            result += 'R'

        else:
            if choose_hand_for_move(left_hand, right_hand, number, hand) == 'left':
                left_hand = key_map[number]
                result += 'L'
            else:
                right_hand = key_map[number]
                result += 'R'

    return result
