from puzzle_05_inputs import example_input, real_input


def puzzle_05_b2():
    input = real_input
    input_ranges = input["fresh_ranges"]
    # print("INPUT", input_ranges)

    def get_numbers_tuple(string):
        [start, end] = string.split("-")
        return [int(start), int(end)]

    input_tuples = [get_numbers_tuple(x) for x in input_ranges]
    input_tuples.sort()
    # print("SORTED", input_tuples)

    checked_tuples = []

    for [input_start, input_end] in input_tuples:
        start_in_tuples_index = None
        end_in_tuples_index = None

        for index, [checked_start, checked_end] in enumerate(checked_tuples):
            if input_start in range(checked_start, checked_end + 1):
                start_in_tuples_index = index
            if input_end in range(checked_start, checked_end + 1):
                end_in_tuples_index = index

        has_start_index = isinstance(start_in_tuples_index, int)
        has_end_index = isinstance(end_in_tuples_index, int)

        if has_start_index or has_end_index:
            # Start and end with same index -> nothing to do
            # Start but not end -> extends tuple to end value
            if has_start_index and not has_end_index:
                checked_tuples[start_in_tuples_index] = [checked_start, input_end]
            # End but not start -> extends tuple to start value
            if not has_start_index and has_end_index:
                checked_tuples[end_in_tuples_index] = [
                    input_start,
                    checked_end,
                ]
        # Start and end at None -> add to checked
        else:
            checked_tuples.append([input_start, input_end])

        # print(
        #     f"{[input_start, input_end]} - Start: {start_in_tuples_index} - End: {end_in_tuples_index} - {checked_tuples}"
        # )

    # print(checked_tuples)

    fresh_ids_count = 0

    for [start, end] in checked_tuples:
        tuple_range = end - start + 1
        fresh_ids_count += tuple_range

    print(f"There are {fresh_ids_count} fresh ingredients")


puzzle_05_b2()
