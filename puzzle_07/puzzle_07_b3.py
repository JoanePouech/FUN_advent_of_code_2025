from puzzle_07_inputs import example_input, real_input
from functools import reduce
import operator


def puzzle_07_b3():
    input = real_input
    print("TOTAL LINES:", len(input) - 1)

    start_index = input[0].find("S")

    # {[index in line]: count}
    beamlines = dict.fromkeys(range(len(input[0])), 0)
    beamlines[start_index] = 1

    def get_beamlines_count(
        line: str, current_beamlines: dict[int, int]
    ) -> dict[int, int]:

        if line.count("^"):
            separator_indexes = [x for x, y in enumerate(line) if y == "^"]

            for separator_index in separator_indexes:
                beam_to_move = current_beamlines[separator_index]
                current_beamlines[separator_index] = 0

                previous_index = separator_index - 1
                current_beamlines[previous_index] += beam_to_move

                next_index = separator_index + 1
                current_beamlines[next_index] += beam_to_move

        return current_beamlines

    for line_index, line in enumerate(input[1:]):
        print(f"----- Processing line {str(line_index).rjust(3,"0")} -----")
        beamlines = get_beamlines_count(line, beamlines)
        print("Beamlines", beamlines)

    print(f"There are {sum(beamlines.values())} possibles timelines")


puzzle_07_b3()
