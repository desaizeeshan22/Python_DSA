import heapq


def second_smallest(arr):
    s_smallest, smallest = float("inf"), float("inf")
    for elem in arr:
        if elem < smallest:
            smallest = elem
        elif elem < s_smallest and elem > smallest:
            s_smallest = elem
    return s_smallest


print(second_smallest([5, 7, 9, 1, 1, 2, 3, 3, 4, 3]))
