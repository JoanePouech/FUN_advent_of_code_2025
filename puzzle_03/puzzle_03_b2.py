from puzzle_03_inputs import example_input, real_input


def puzzle_03_b():
    input = real_input

    banks_joltages = []

    for bank in input:
        batteries = [int(x) for x in list(bank)]

        joltage_numbers = 12
        max_indexes = []
        largest_joltage = ""

        wip_batteries = batteries.copy()

        for i in range(joltage_numbers):
            if (i + 1) == joltage_numbers:
                search_max_range = wip_batteries
            else:
                search_max_range = wip_batteries[: -(joltage_numbers - i - 1)]

            max_index = wip_batteries.index(max(search_max_range))

            max_indexes.append(max_index)
            # print(i, wip_batteries, search_max_range, max_index)

            for j in range(max_index + 1):
                wip_batteries[j] = 0
            # print(wip_batteries)

        max_indexes.sort()

        for index in max_indexes:
            largest_joltage += str(batteries[index])

        # print(largest_joltage)
        banks_joltages.append(int(largest_joltage))

    # print(banks_joltages)

    print(f"ANSWER IS {sum(banks_joltages)}")


puzzle_03_b()
