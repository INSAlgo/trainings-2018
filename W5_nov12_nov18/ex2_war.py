from collections import deque


def main():
    cards = list(map(str, range(2, 11))) + ["J", "Q", "K", "A"]
    val = {cards[i]: i for i in range(len(cards))}

    # 1st player's deck
    n = int(input())
    q1 = deque(val[input()[:-1]] for _ in range(n))

    # 2nd player's deck
    m = int(input())
    q2 = deque(val[input()[:-1]] for _ in range(m))

    pat = False
    i = 0
    while q1 and q2 and not pat:
        pat = round(q1, q2, [], [])
        i += 1
    if pat:
        print("PAT")
    else:
        play = 1
        if not q1:
            play = 2
        print(play, i)


def round(q1, q2, l1, l2):
    v1 = q1.popleft()
    v2 = q2.popleft()
    l1.append(v1)
    l2.append(v2)

    if(v1 > v2):
        q1 += l1 + l2
    elif(v1 < v2):
        q2 += l1 + l2
    else:
        return war(q1, q2, l1, l2)

    return False


def war(q1, q2, l1, l2):
    for i in range(3):
        if not q1 or not q2:
            break
        l1.append(q1.popleft())
        l2.append(q2.popleft())

    if not q1 or not q2:
        return True
    else:
        return round(q1, q2, l1, l2)


if __name__ == '__main__':
    main()
