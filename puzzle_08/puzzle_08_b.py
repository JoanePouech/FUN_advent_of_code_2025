from puzzle_08_inputs import example_input, real_input
import math


def puzzle_08_b():
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

    # Sort by shortest distances
    def sort_by_dist(tuple):
        [boxes, dist] = tuple
        return dist

    boxes_distances.sort(key=sort_by_dist)

    # identify circuits
    circuits = input
    print(f"{len(circuits)} CIRCUITS", circuits)

    current_distance_index = 0
    current_boxes = ""

    while len(circuits) > 1:
        print(f"----- PROCESS CONNECTION {current_distance_index +1} -----")
        current_boxes = boxes_distances[current_distance_index][0]
        box1, box2 = current_boxes.split("-")

        for circuit_index, circuit in enumerate(circuits):
            if box1 in circuit:
                index1 = circuit_index
            if box2 in circuit:
                index2 = circuit_index

        if index1 != index2:
            circuits[index1] += f"-{circuits[index2]}"
            circuits.pop(index2)

        current_distance_index += 1

        print(dist, index1, index2)
        print(f"{len(circuits)} CIRCUITS")

    # Calculate results
    result_boxes = [[int(y) for y in x.split(",")] for x in current_boxes.split("-")]

    print(f"Result is {result_boxes[0][0]*result_boxes[1][0]}")


puzzle_08_b()
