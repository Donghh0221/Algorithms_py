import collections


def solution(k, room_number):
    assigned_table = dict()
    last_assigned_table = dict()

    for wanted_room_number in room_number:
        if wanted_room_number in assigned_table:
            next_assigned_room_number = last_assigned_table[wanted_room_number] + 1
            while True:
                if next_assigned_room_number in assigned_table:
                    next_assigned_room_number += 1
                else:
                    last_assigned_table[wanted_room_number] = next_assigned_room_number
                    assigned_table[next_assigned_room_number] = wanted_room_number
                    break
        else:
            assigned_table[wanted_room_number] = wanted_room_number
            last_assigned_table[wanted_room_number] = wanted_room_number
    return list(assigned_table.keys())





def solution1(k, room_number):
    hashmap = collections.defaultdict(int)
    last_assigned_table = collections.defaultdict(int)

    for wanted_room_number in room_number:
        #last_assigned_table

        if not last_assigned_table[wanted_room_number]:
            assigned_room_number = wanted_room_number

        else:
            assigned_room_number = last_assigned_table[wanted_room_number]

        if not hashmap[assigned_room_number]:
            hashmap[assigned_room_number] = wanted_room_number

        else:
            while hashmap[assigned_room_number]:
                assigned_room_number += 1
            hashmap[assigned_room_number] = wanted_room_number

        last_assigned_table[wanted_room_number] = assigned_room_number

    return list(hashmap.keys())








if __name__ == "__main__":
    k = 10
    room_number = [1, 3, 4, 1, 3, 1]
    print(solution(k, room_number))
