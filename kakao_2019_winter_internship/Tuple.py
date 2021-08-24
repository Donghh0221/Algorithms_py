def solution(s):
    trimmed_s = s[:-2][2:]
    answer = []
    for t in sorted(trimmed_s.split("},{"), key=len):
        if answer:
            diff_set = set(map(int, t.split(","))) - set(answer)
            answer.append(list(diff_set)[0])
        else:
            answer.append(list(set(map(int, t.split(","))))[0])
    return answer


if __name__ == "__main__":
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"	))
