from puzzle_08_inputs import example_input, real_input
import math


def puzzle_08_a():
    input = real_input

    boxes_coords = [[int(y) for y in x.split(",")] for x in input]
    boxes_distances = []

    # calculate distances for each combination
    for index1, box1 in enumerate(boxes_coords):
        for box2 in boxes_coords[index1 + 1 :]:
            dist = math.dist(box1, box2)

            x1, y1, z1 = box1
            x2, y2, z2 = box2

            boxes_distances.append([f"{x1},{y1},{z1}-{x2},{y2},{z2}", dist])
            # print(f"{str(box1).rjust(11)}-{str(box2).rjust(11)} : {dist}")

    # print("DIST", boxes_distances)

    # keep X shortest distances
    connections_to_do = 1000

    def sort_by_dist(tuple):
        [boxes, dist] = tuple
        return dist

    boxes_distances.sort(key=sort_by_dist)

    # identify circuits
    circuits = input
    print(f"{len(circuits)} CIRCUITS", circuits)

    for index, dist in enumerate(boxes_distances[:connections_to_do]):
        print(f"----- PROCESS CONNECTION {index +1} -----")
        box1, box2 = dist[0].split("-")

        for circuit_index, circuit in enumerate(circuits):
            if box1 in circuit:
                index1 = circuit_index
            if box2 in circuit:
                index2 = circuit_index

        if index1 != index2:
            circuits[index1] += f"-{circuits[index2]}"
            circuits.pop(index2)

        print(dist, index1, index2)
        print(f"{len(circuits)} CIRCUITS")

    # Sort circuits by length
    def sort_by_string_length(str):
        return len(str)

    circuits.sort(key=sort_by_string_length, reverse=True)
    # print("SORT", circuits)

    # calculate results
    result_1 = circuits[0].count("-") + 1
    result_2 = circuits[1].count("-") + 1
    result_3 = circuits[2].count("-") + 1

    result = result_1 * result_2 * result_3

    print(result_1, result_2, result_3)
    print(f"Result is {result}")


puzzle_08_a()
