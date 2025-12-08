from puzzle_05_inputs import example_input, real_input


# TO SLOW FOR REAL INPUT
def puzzle_05_b1():
    input = example_input
    fresh_ranges = input["fresh_ranges"]
    print(fresh_ranges)

    fresh_ids_set = set()

    for fresh_range in fresh_ranges:
        fresh_range_indexes = fresh_range.split("-")
        start_range = int(fresh_range_indexes[0])
        end_range = int(fresh_range_indexes[1]) + 1

        fresh_ids_set.update(range(start_range, end_range))

        print(f"{fresh_range} - {fresh_ids_set}")

    print(fresh_ids_set)
    print(f"There are {len(fresh_ids_set)} fresh ingredients")


puzzle_05_b1()
