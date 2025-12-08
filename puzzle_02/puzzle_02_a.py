from puzzle_02_inputs import example_input, real_input


def puzzle_02_a():
    input = real_input

    rangesArray = input.split(",")
    invalidIds = []

    for currentRange in rangesArray:
        [rangeStart, rangeEnd] = currentRange.split("-")
        # print(currentRange, rangeStart, rangeEnd)

        for number in range(int(rangeStart), int(rangeEnd) + 1):
            digitsInNumber = len(str(number))
            isDigitsNumberPeer = digitsInNumber % 2 == 0
            # print(number, digitsInNumber, isDigitsNumberPeer)

            if isDigitsNumberPeer:
                halfDigitsNumber = int(digitsInNumber / 2)
                numberStart = str(number)[:halfDigitsNumber]
                numberEnd = str(number)[halfDigitsNumber:]

                # print(halfDigitsNumber, numberStart, numberEnd)

                if numberStart == numberEnd:
                    invalidIds.append(number)

    # print(invalidIds)

    invalidIDsSum = sum(invalidIds)
    print(f"ANSWER IS {invalidIDsSum}")


puzzle_02_a()
