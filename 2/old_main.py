def main():
    rules = {
        'X': {'defeat': 'B', 'win': 'C', 'draw': 'A', 'point': 1},  # my hand is rock
        'Y': {'defeat': 'C', 'win': 'A', 'draw': 'B', 'point': 2},  # my hand is paper
        'Z': {'defeat': 'A', 'win': 'B', 'draw': 'C', 'point': 3},  # my hand is scissor
        'A': {'defeat': 'Y', 'win': 'Z', 'draw': 'X', 'point': 1},  # my hand is rock
        'B': {'defeat': 'Z', 'win': 'X', 'draw': 'Y', 'point': 2},  # my hand is paper
        'C': {'defeat': 'X', 'win': 'Y', 'draw': 'Z', 'point': 3}  # my hand is scissor
    }
    data = open('input.txt').read().split("\n")

    opponent_hand, my_hand, part1_pts, part2_pts = '', '', 0, 0

    for hands in data:
        opponent_hand = hands.split(' ')[0]
        my_hand = hands.split(' ')[1]

        my_round_options = rules.get(my_hand)
        oppenent_round_options = rules.get(opponent_hand)

        # part 1
        # wins = 6pts, draw = 3pts, lost = 0pts. Hand point is always received.
        if opponent_hand == my_round_options.get('win'):
            part1_pts += (my_round_options.get('point') + 6)  # win gives 6 pts
        elif opponent_hand == my_round_options.get('draw'):
            part1_pts += (my_round_options.get('point') + 3)  # draw gives 3 pts
        elif opponent_hand == my_round_options.get('defeat'):
            part1_pts += my_round_options.get('point')

        # part 2
        # Z = win, Y = draw, X = defeat
        if my_hand == 'Z':
            point = rules.get(rules.get(opponent_hand).get('defeat')).get('point')
            part2_pts += (point + 6)
        elif my_hand == 'Y':
            part2_pts += (rules.get(opponent_hand).get('point') + 3)
        elif my_hand == 'X':
            point = rules.get(rules.get(opponent_hand).get('win')).get('point')
            part2_pts += point
    print(part1_pts)
    print(part2_pts)

if __name__ == "__main__":
    main()