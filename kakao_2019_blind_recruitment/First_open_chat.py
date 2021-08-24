def solution(record):
    nickname_dict = dict()
    parsed_record = []
    for r in record:
        separated = r.split(" ")
        action = separated[0]
        if action == "Enter":
            u_id, nickname = separated[1], separated[2]
            nickname_dict[u_id] = nickname
            parsed_record.append([action, u_id])

        elif action == "Leave":
            u_id = separated[1]
            parsed_record.append([action, u_id])

        elif action == "Change":
            u_id, nickname = separated[1], separated[2]
            nickname_dict[u_id] = nickname

    answer = []
    for r in parsed_record:
        if r[0] == "Enter":
            change = nickname_dict[r[1]] + '님이 들어왔습니다.'
            answer.append(change)
        elif r[0] == "Leave":
            change = nickname_dict[r[1]] + '님이 나갔습니다.'
            answer.append(change)

    return answer


if __name__ == "__main__":
    print(solution(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
