from puzzle_06_inputs import example_input, real_input


def puzzle_06_b():
    input = real_input
    print(input)

    operators_line = input[-1]
    operators_line_len = len(input[-1])

    operators_count = input[-1].count("+")
    operators_count += input[-1].count("*")

    print(
        f"Operators: {operators_count} - {list(operators_line)} - {operators_line_len}"
    )

    # --- OPERATORS INDEXES ---
    operator_indexes = []

    for i in range(operators_count):
        start_index = operator_indexes[-1] + 1 if len(operator_indexes) else 0

        # Operator + index
        if "+" in operators_line[start_index:]:
            plus_operator_index = operators_line.index("+", start_index)
        else:
            plus_operator_index = operators_line_len

        # Operator * index
        if "*" in operators_line[start_index:]:
            mul_operator_index = operators_line.index("*", start_index)
        else:
            mul_operator_index = operators_line_len

        lowest_index = min(plus_operator_index, mul_operator_index)

        operator_indexes.append(lowest_index)
        # print(lowest_index, operator_indexes)

    print(operator_indexes)

    # --- OPERATIONS GROUPS ---

    operations_groups = []

    for i in range(operators_count):
        start_index = operator_indexes[i]
        end_index = operator_indexes[i + 1] - 1 if i + 1 < operators_count else None
        operation_values = []

        for line in input:
            operation_values.append(line[start_index:end_index])

        operations_groups.append(operation_values)
        # print(
        #     f"Start index: {start_index} - End index: {end_index} - {operation_values}"
        # )

    print(operations_groups)

    # --- CALCULATE FOR EACH GROUP ---

    group_totals = []

    for group in operations_groups:
        group_len = len(group[0])
        group_sign = group[-1][0]
        group_total = 0 if group_sign is "+" else 1

        for i in range(group_len):
            number_str = ""
            for line in group[:-1]:
                number_str += line[i]

            # print(number_str)
            group_total = eval(f"{group_total}{group_sign}{int(number_str)}")

        group_totals.append(group_total)

        print(f"{group} - len: {group_len} - sign: {group_sign} - total: {group_total}")

    print(group_totals)

    print(f"Result is {sum(group_totals)}")


puzzle_06_b()
