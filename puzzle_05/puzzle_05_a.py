from puzzle_05_inputs import example_input, real_input


def puzzle_05_a():
    input = real_input
    fresh_ranges = input["fresh_ranges"]
    ingredients_ids = input["ingredients_ids"]
    print(input)
    print(fresh_ranges, ingredients_ids)

    fresh_ingredients = []

    for ingredient in ingredients_ids:
        is_fresh_ingredient = False

        for fresh_range in fresh_ranges:
            fresh_range_indexes = fresh_range.split("-")
            start_range = int(fresh_range_indexes[0])
            end_range = int(fresh_range_indexes[1]) + 1

            if int(ingredient) in range(start_range, end_range):
                is_fresh_ingredient = True
                break

            # print(f"{ingredient} - {fresh_range} - {is_fresh_ingredient}")

        if is_fresh_ingredient:
            fresh_ingredients.append(ingredient)

    print(fresh_ingredients)
    print(f"There are {len(fresh_ingredients)} fresh ingredients")


puzzle_05_a()
