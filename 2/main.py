def main():
    # rock, paper, scissor
    # points for round combinations
    # ------------------------------------
    # A vs X = DRAW  = (1+3) = 4
    # A vs Y = WIN   = (2+6) = 8
    # A vs Z = LOSS  = (3+0) = 3
    # B vs X = LOSS  = (1+0) = 1
    # B vs Y = DRAW  = (2+3) = 5
    # B vs Z = WIN   = (3+6) = 9
    # C vs X = WIN   = (1+6) = 7
    # C vs Y = LOSS  = (2+0) = 2
    # C vs Z = DRAW  = (3+3) = 6

    data = open('input.txt').read().split("\n")

    total_points_pt1, total_points_pt2 = 0, 0

    outcomes = {
        "A X":4, "A Y":8, "A Z":3,
        "B X":1, "B Y":5, "B Z":9,
        "C X":7, "C Y":2, "C Z":6
    }

    for round in data:
        total_points_pt1 += outcomes.get(round)

    desired_outcomes = {
        "A X":3, "A Y":4, "A Z":8,
        "B X":1, "B Y":5, "B Z":9,
        "C X":2, "C Y":6, "C Z":7
    }

    for round in data:
        total_points_pt2 += desired_outcomes.get(round)

    print("Answer to part 1: " + str(total_points_pt1))
    print("Answer to part 2: " + str(total_points_pt2))


if __name__ == "__main__":
    main()
