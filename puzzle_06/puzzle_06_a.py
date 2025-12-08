from puzzle_06_inputs import example_input, real_input


def puzzle_06_a():
    input = real_input
    print(input)

    def format_line(string):
        return list(filter(lambda x: x != "", string.split(" ")))

    formatted_input = [format_line(x) for x in input]
    print(formatted_input)

    index_counts = []

    for index in range(len(formatted_input[0])):
        sign = formatted_input[-1][index]
        index_count = formatted_input[0][index]

        for line in formatted_input[1:-1]:
            index_count = eval(f"{index_count}{sign}{line[index]}")

        index_counts.append(index_count)

        print(f"{index} - sign: {sign} - {index_count}")

    print(index_counts)
    print(f"Result is {sum(index_counts)}")


puzzle_06_a()
