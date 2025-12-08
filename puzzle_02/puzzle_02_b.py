from puzzle_02_inputs import example_input, real_input


def puzzle_02_b():
    input = real_input

    rangesArray = input.split(",")
    invalidIds = []

    for currentRange in rangesArray:
        [rangeStart, rangeEnd] = currentRange.split("-")
        # print(currentRange, rangeStart, rangeEnd)

        for number in range(int(rangeStart), int(rangeEnd) + 1):
            strNumber = str(number)
            totalDigitsInNumber = len(strNumber)

            isNumberInvalidId = False

            for digitNumber in range(1, totalDigitsInNumber):
                isDivisible = totalDigitsInNumber % digitNumber == 0

                if isDivisible:
                    splittedNumber = [
                        strNumber[i : i + digitNumber]
                        for i in range(0, len(strNumber), digitNumber)
                    ]

                    isEverySplitEqual = len(set(splittedNumber)) == 1

                    if isEverySplitEqual:
                        isNumberInvalidId = True

                    # print(
                    #     number,
                    #     totalDigitsInNumber,
                    #     digitNumber,
                    #     splittedNumber,
                    #     len(set(splittedNumber)),
                    #     isEverySplitEqual,
                    # )

            if isNumberInvalidId:
                invalidIds.append(number)

    # print(invalidIds)

    invalidIDsSum = sum(invalidIds)
    print(f"ANSWER IS {invalidIDsSum}")


puzzle_02_b()
