def solution(places):
    answer = []
    for place in places:
        paded_place = pad_place(place)
        answer.append(check_distancing(paded_place))

    return answer


def pad_place(place):
    paded_place = []
    paded_place.append("XXXXXXXXX")
    paded_place.append("XXXXXXXXX")
    for row in place:
        paded_place.append("XX" + row + "XX")
    paded_place.append("XXXXXXXXX")
    paded_place.append("XXXXXXXXX")
    return paded_place


def check_distancing(paded_place):
    for i in range(2, 7):
        for j in range(2, 7):
            if paded_place[i][j] == "P":
                if paded_place[i - 1][j] == "P":
                    return 0
                if paded_place[i + 1][j] == "P":
                    return 0
                if paded_place[i][j + 1] == "P":
                    return 0
                if paded_place[i][j - 1] == "P":
                    return 0

                if paded_place[i + 2][j] == "P" and paded_place[i + 1][j] == "O":
                    return 0
                if paded_place[i - 2][j] == "P" and paded_place[i - 1][j] == "O":
                    return 0
                if paded_place[i][j + 2] == "P" and paded_place[i][j + 2] == "O":
                    return 0
                if paded_place[i][j - 2] == "P" and paded_place[i][j - 1] == "O":
                    return 0

                if paded_place[i + 1][j + 1] == "P" and ("O" in [paded_place[i + 1][j], paded_place[i][j + 1]]):
                    return 0
                if paded_place[i - 1][j + 1] == "P" and ("O" in [paded_place[i - 1][j], paded_place[i][j + 1]]):
                    return 0
                if paded_place[i + 1][j - 1] == "P" and ("O" in [paded_place[i + 1][j], paded_place[i][j - 1]]):
                    return 0
                if paded_place[i - 1][j - 1] == "P" and ("O" in [paded_place[i - 1][j], paded_place[i][j - 1]]):
                    return 0
    return 1


if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    solution(places)
