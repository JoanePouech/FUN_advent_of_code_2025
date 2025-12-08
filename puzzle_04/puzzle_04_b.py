from puzzle_04_inputs import example_input, real_input


def identify_accessible_rolls(input_diagram: list[str]):
    accessible_rolls = 0
    new_diagram = input_diagram.copy()

    for index_line, line in enumerate(input_diagram):
        for index_point, point in enumerate(line):
            if point == "@":
                # Indexes
                right_index = index_point if index_point == 0 else index_point - 1
                left_index = index_point + 2

                # Lines
                # previous
                previous_line_points = (
                    input_diagram[index_line - 1][right_index:left_index]
                    if index_line > 0
                    else ""
                )
                # current
                current_line_points = line[right_index:left_index]
                # next
                next_line_points = (
                    input_diagram[index_line + 1][right_index:left_index]
                    if index_line < len(input_diagram) - 1
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
                    new_line = list(new_diagram[index_line])
                    new_line[index_point] = "."
                    new_diagram[index_line] = "".join(new_line)

                # print(
                #     f"roll in line {index_line}, position {index_point} (right: {right_index}, left: {str(left_index).rjust(2,'0')}) - {previous_line_points.rjust(3," ")} {current_line_points.rjust(3," ")} {next_line_points.rjust(3," ")} - {adjacent_points.rjust(9," ")} - {adjacent_rolls} - {is_accessible_roll}"
                # )

    return accessible_rolls, new_diagram


def recurse(diagram_input, rolls_by_turn) -> list[int]:
    accessible_rolls, new_diagram = identify_accessible_rolls(diagram_input)
    print(f"{accessible_rolls} accessible rolls --> {new_diagram}")

    if accessible_rolls != 0:
        rolls_by_turn.append(accessible_rolls)
        recurse(new_diagram, rolls_by_turn)

    return rolls_by_turn


def puzzle_04_b():
    input = real_input
    print(input)

    accessible_rolls_by_turn = recurse(input, [])

    print(accessible_rolls_by_turn)

    print(f"There are {sum(accessible_rolls_by_turn)} removable rolls")


puzzle_04_b()
