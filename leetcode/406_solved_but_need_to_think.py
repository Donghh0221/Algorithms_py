class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        answer = []

        for p in sorted_people:
            answer.insert(p[1], p)

        return answer