from collections import Counter


def solution(participant, completion):
    participant_table = Counter(participant)
    completion_table = Counter(completion)
    for key in participant_table.keys():
        try:
            num_completed_athlete = completion_table[key]
        except KeyError:
            return key

        if participant_table[key] > num_completed_athlete:
            return key


if __name__ == "__main__":
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(solution(participant, completion))
