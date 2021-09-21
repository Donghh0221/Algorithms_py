from collections import defaultdict
import bisect

def solution(info, query):
    answer = []

    table = defaultdict(list)

    for i in info:
        split_info = i.split(" ")
        info_lan = [split_info[0][0], '-']
        info_job = [split_info[1][0], '-']
        info_expert = [split_info[2][0], '-']
        info_food = [split_info[3][0], '-']
        score = int(split_info[4])
        for l in info_lan:
            for j in info_job:
                for e in info_expert:
                    for f in info_food:
                        table[l + j + e + f].append(score)
    for k in table.keys():
        table[k].sort()

    for q in query:
        q = q.replace("and ", "")
        conditions = q.split(" ")

        condition = conditions[0][0] + conditions[1][0] + conditions[2][0] + conditions[3][0]
        score = int(conditions[4])
        n = len(table[condition]) - bisect.bisect_left(table[condition], score)
        answer.append(n)
    return answer

if __name__ == "__main__":
    info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
            "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
             "- and - and - and chicken 100", "- and - and - and - 150"]
    print(solution(info, query))
