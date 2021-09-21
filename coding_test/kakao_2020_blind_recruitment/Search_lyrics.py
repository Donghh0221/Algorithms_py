import re
from collections import deque

def solution(words, queries):
    answer = deque()
    lyrics = "  " + "  ".join(words) + "  "

    for i, query in enumerate(queries):
        pattern = " " + re.sub("\?+", f'[a-z]{"{" + str(query.count("?")) + "}"}', query) + " "
        answer.append(len(re.findall(pattern, lyrics)))
    return list(answer)


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))
