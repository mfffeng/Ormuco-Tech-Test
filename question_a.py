#!/usr/bin/python3

# Returns True if there is an overlap
def find_overlap(pt1: tuple, pt2: tuple) -> bool:
    return pt2[1] > pt1[0] and pt1[1] > pt2[0]

if __name__ == "__main__":
    print(f"{find_overlap((1, 5), (2, 6))}, {find_overlap((1, 5), (6, 8))}")