from puzzle_09_inputs import example_input, real_input
import math


def puzzle_09_a():
    input = real_input
    print(input)

    red_coords = [[int(y) for y in x.split(",")] for x in input]
    print(red_coords)

    largest_square = 0

    for index_1, coords_1 in enumerate(red_coords):
        for coords_2 in red_coords[index_1 + 1 :]:
            col_1, row_1 = coords_1
            col_2, row_2 = coords_2

            col_diff = int(math.fabs(col_1 - col_2)) + 1
            row_diff = int(math.fabs(row_1 - row_2)) + 1

            current_square = col_diff * row_diff

            if current_square > largest_square:
                largest_square = current_square

            print(
                coords_1,
                coords_2,
                col_diff,
                row_diff,
                "Square =",
                current_square,
                "Largest =",
                largest_square,
            )

    print(f"The largest square is {largest_square} tiles")


puzzle_09_a()
