from puzzle_07_inputs import example_input, real_input


def puzzle_07_a():
    input = real_input
    # print(input)

    beam_indexes = set()
    split_times = 0

    input_with_beams = input.copy()

    for line_index, line in enumerate(input):
        if line_index == 0:
            beam_indexes.add(input[0].find("S"))
        else:
            next_beam_indexes = set()
            for beam_index in beam_indexes:
                if line[beam_index] == "^":
                    split_times += 1
                    next_beam_indexes.add(beam_index - 1)
                    next_beam_indexes.add(beam_index + 1)

                    input_with_beams_line = list(input_with_beams[line_index])
                    input_with_beams_line[beam_index - 1] = "|"
                    input_with_beams_line[beam_index + 1] = "|"
                    input_with_beams[line_index] = "".join(input_with_beams_line)
                else:
                    next_beam_indexes.add(beam_index)

                    input_with_beams_line = list(input_with_beams[line_index])
                    input_with_beams_line[beam_index] = "|"
                    input_with_beams[line_index] = "".join(input_with_beams_line)

            beam_indexes = next_beam_indexes

        print(
            f"{line} - {input_with_beams[line_index]} - {split_times} - {beam_indexes}"
        )

    print(f"Beam split {split_times} times")


puzzle_07_a()
