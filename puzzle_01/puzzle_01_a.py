from puzzle_01_inputs import example_input, real_input


def puzzle_01_a():
    input = real_input
    current_dial = 50
    dial_steps = []

    for turn in input:
        turn_side = turn[0]
        turn_count = int("".join(list(turn)[1:]))

        if turn_side not in ("L", "R"):
            print("ERROR turn side", turn_side)

        if not turn_count or turn_count <= 0:
            print("ERROR turn count", turn_count)

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

            current_count += 1

        dial_steps.append(current_dial)

        # print(turn, turn_side, turn_count, "DIAL:", current_dial)

    # print("STEPS", dial_steps)

    zero_dial_steps = list(filter(lambda x: x == 0, dial_steps))
    # print("ZERO", zero_dial_steps)

    print(f"CODE PASSWORD IS {len(zero_dial_steps)}")


puzzle_01_a()
