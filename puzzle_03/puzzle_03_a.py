from puzzle_03_inputs import example_input, real_input


def puzzle_03_a():
    input = real_input
    print(input)

    banks_joltages = []

    for bank in input:
        batteries = list(bank)
        largest_joltage = 0

        for index, first_number in enumerate(batteries):
            for second_number in batteries[index + 1 :]:
                current_joltage = int(f"{first_number}{second_number}")
                # print(current_joltage)

                if current_joltage > largest_joltage:
                    largest_joltage = current_joltage

        banks_joltages.append(largest_joltage)

        print(batteries, largest_joltage)

    print(banks_joltages)

    print(f"ANSWER IS {sum(banks_joltages)}")


puzzle_03_a()
