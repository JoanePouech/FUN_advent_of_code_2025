from puzzle_04_inputs import example_input, real_input


def puzzle_04_a():
    input = real_input
    print(input, len(input))

    accessible_rolls = 0

    for index_line, line in enumerate(input):
        for index_point, point in enumerate(line):
            if point == "@":
                # Indexes
                right_index = index_point if index_point == 0 else index_point - 1
                left_index = index_point + 2

                # Lines
                # previous
                previous_line_points = (
                    input[index_line - 1][right_index:left_index]
                    if index_line > 0
                    else ""
                )
                # current
                current_line_points = line[right_index:left_index]
                # next
                next_line_points = (
                    input[index_line + 1][right_index:left_index]
                    if index_line < len(input) - 1
                    else ""
                )

                # Total
                adjacent_points = (
                    previous_line_points + current_line_points + next_line_points
                )
                adjacent_rolls = len([x for x in adjacent_points if x == "@"]) - 1
                is_accessible_roll = adjacent_rolls < 4

                if is_accessible_roll:
                    accessible_rolls += 1

                print(
                    f"roll in line {index_line}, position {index_point} (right: {right_index}, left: {str(left_index).rjust(2,'0')}) - {previous_line_points.rjust(3," ")} {current_line_points.rjust(3," ")} {next_line_points.rjust(3," ")} - {adjacent_points.rjust(9," ")} - {adjacent_rolls} - {is_accessible_roll}"
                )

    print(f"There are {accessible_rolls} accessible rolls")


puzzle_04_a()
