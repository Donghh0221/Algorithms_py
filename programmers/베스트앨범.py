from collections import defaultdict


def solution(genres, plays):
    genres_counts = defaultdict(int)
    genres_songs = defaultdict(list)
    answer = []

    for i, s in enumerate(zip(genres, plays)):
        index, genre, play_count = i, s[0], s[1]

        genres_counts[genre] += play_count
        genres_songs[genre].append([index, play_count])

    genres_sorted_by_sum_of_count = sorted(genres_counts.items(), key=lambda v: v[1], reverse=True)
    for genres_count in genres_sorted_by_sum_of_count:
        key = genres_count[0]

        s = sorted(genres_songs[key], key=lambda x: (-x[1], x[0]))

        if len(s) > 1:
            answer.append(s[0][0])
            answer.append(s[1][0])
        else:
            answer.append(s[0][0])

    return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))
