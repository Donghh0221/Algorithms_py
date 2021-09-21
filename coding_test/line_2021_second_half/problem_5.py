import difflib


def solution(nicks, emails):
    pair = list()

    for i in range(len(nicks)):
        for j in range(i + 1, len(nicks)):
            if same_user(nicks[i], nicks[j], emails[i], emails[j]):
                pair.append([i, j])

    parent = [0] * (len(nicks))

    for i in range(len(nicks)):
        parent[i] = i

    for i in pair:
        a, b = i[0], i[1]
        union_parent(parent, a, b)

    return len(set(parent))


def find_parnet(parent, x):
    if parent[x] != x:
        parent[x] = find_parnet(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parnet(parent, a)
    b = find_parnet(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def same_user(nick1, nick2, email1, email2):
    if is_string_similarity(nick1, nick2, 2) and is_email_similarity(email1, email2):
        return True


def is_string_similarity(nickname1, nickname2, n):
    diff_list = [li for li in difflib.ndiff(nickname1, nickname2) if li[0] != ' ']

    if len(diff_list) > n:
        return False

    return True


def is_email_similarity(email1: str, email2: str) -> bool:
    host_name1, server_name1 = email1.split("@")
    host_name2, server_name2 = email2.split("@")
    if host_name1 == host_name2:
        return True

    if is_string_similarity(host_name1, host_name2, 1) and server_name1 == server_name2:
        return True

    return False


if __name__ == "__main__":
    nicks = ["imhero111", "moneyman", "hero111", "imher1111", "hro111", "mmoneyman", "moneymannnn"]
    emails = ["superman5@abcd.com", "batman432@korea.co.kr", "superman@abcd.com", "supertman5@abcd.com",
              "superman@erty.net", "batman42@korea.co.kr", "batman432@usa.com"]
    print(solution(nicks, emails))
