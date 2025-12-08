from puzzle_01_inputs import example_input, real_input


def puzzle_01_b():
    input = real_input
    current_dial = 50
    zero_dials = 0

    for turn in input:
        turn_side = turn[0]
        turn_count = int("".join(list(turn)[1:]))

        current_count = int(0)
        while current_count != turn_count:
            if turn_side == "L":
                if current_dial == 0:
                    current_dial = 99
                else:
                    current_dial = current_dial - 1

            if turn_side == "R":
                if current_dial == 99:
                    current_dial = 0
                else:
                    current_dial += 1

            if current_dial == 0:
                zero_dials += 1

            current_count += 1

    print(f"CODE PASSWORD IS {zero_dials}")


puzzle_01_b()
