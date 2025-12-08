from puzzle_03_inputs import example_input, real_input


def puzzle_03_b():
    input = real_input
    print(len(input))

    banks_joltages = []

    for bank in input:
        print(bank, len(bank))
        batteries = list(bank)
        current_bank_joltages = []

        max_voltage_numbers = 12

        def recurse(batteries_list, concat_joltage, max_voltage_numbers):
            print(concat_joltage)
            for index, str_number in enumerate(batteries_list):
                current_joltage = concat_joltage + str_number

                if len(current_joltage) == max_voltage_numbers:
                    current_bank_joltages.append(int(current_joltage))
                    # print(f"final string: {current_joltage}")
                else:
                    reamining_list = batteries_list[index + 1 :]
                    if (
                        len(reamining_list) + len(current_joltage)
                        >= max_voltage_numbers
                    ):
                        # print(str_number, reamining_list, current_joltage)
                        recurse(reamining_list, current_joltage, max_voltage_numbers)

        recurse(batteries, "", max_voltage_numbers)

        largest_joltage = max(current_bank_joltages)
        print(largest_joltage)
        banks_joltages.append(largest_joltage)

        # print(batteries)
        # print(current_bank_joltages, largest_joltage)

    print(banks_joltages)

    print(f"ANSWER IS {sum(banks_joltages)}")


puzzle_03_b()


def test_recurse():
    test_str = ["A", "B", "C", "D"]
    print(test_str)

    def recurse_str(str_list, concat_str, max_char):
        for index, letter in enumerate(str_list):
            current_string = concat_str + letter
            if len(current_string) == max_char:
                print(f"final string: {current_string}")
            else:
                reamining_list = str_list[index + 1 :]
                if len(reamining_list) + len(current_string) >= max_char:
                    print(letter, reamining_list, current_string)
                    recurse_str(reamining_list, current_string, max_char)

    recurse_str(test_str, "", 2)


# test_recurse()
