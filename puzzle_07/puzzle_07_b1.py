from puzzle_07_inputs import example_input, real_input


# TO SLOW FOR REAL INPUT
def puzzle_07_b():
    input = example_input
    # print(input)

    start_index = input[0].find("S")
    timelines = [[start_index]]
    # print(input[0], timelines)

    for line in input[1:]:
        line_new_timelines = []
        for timeline in timelines:
            last_index = timeline[-1]
            if line[last_index] == "^":
                # add left
                line_new_timelines.append([*timeline, last_index - 1])
                # add right
                line_new_timelines.append([*timeline, last_index + 1])
            else:
                # add current
                line_new_timelines.append([*timeline, last_index])
        # update timelines
        timelines = line_new_timelines

        # print(
        #     "Line:",
        #     line,
        #     "Timeline:",
        #     timeline,
        #     "New:",
        #     line_new_timelines,
        #     "Complete:",
        #     timelines,
        # )

    print(f"There are {len(timelines)} possibles timelines")


puzzle_07_b()
