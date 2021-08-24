import collections


def solution(k, room_number):
    hashmap = collections.defaultdict(int)
    for wanted in room_number:
        assigned = wanted
        if hashmap[assigned]:
            while hashmap[assigned]:
                assigned += 1
        hashmap[assigned] = wanted
    return list(hashmap.keys())


if __name__ == "__main__":
    k = 10
    room_number = [1, 3, 4, 1, 3, 1]
    solution(k, room_number)
