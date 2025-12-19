from puzzle_07_inputs import example_input, real_input
from functools import reduce


# TO SLOW FOR REAL INPUT
def puzzle_07_b2():
    input = real_input
    print("TOTAL LINES:", len(input) - 1)

    start_index = input[0].find("S")
    last_indexes = [start_index]
    timelines_count = 1
    # print(input[0], timelines)

    for line_index, line in enumerate(input[1:]):
        if line.count("^"):
            print(
                f"Line {str(line_index).rjust(3,"0")}: {line} - start count = {timelines_count}"
            )
            line_new_indexes = []
            for index in last_indexes:
                if line[index] == "^":
                    timelines_count += 1
                    # add left
                    line_new_indexes.append(index - 1)
                    # add right
                    line_new_indexes.append(index + 1)
                else:
                    # add current
                    line_new_indexes.append(index)
            # update timelines
            last_indexes = line_new_indexes

            # print(
            #     "Line:",
            #     line,
            #     "New:",
            #     line_new_indexes,
            #     "Indexes:",
            #     last_indexes,
            #     "Counts:",
            #     timelines_count,
            # )

    print(f"There are {timelines_count} possibles timelines")


puzzle_07_b2()
