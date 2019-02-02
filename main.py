#!/usr/local/bin/python3
import random
import time


def bubble_sort(array):
    if not array:
        return

    # The largest element is in correct sorted order after each pass
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]


def selection_sort(array):
    if not array:
        return

    for i in range(len(array)):
        # Linear search for the minimum
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        # Put minimum into correct place
        array[i], array[minimum] = array[minimum], array[i]


def insertion_sort(array):
    if not array:
        return

    for i in range(1, len(array)):
        # Take an unsorted element and insert it into correct sorted spot
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def heap_sort(array):
    if not array:
        return

    heapify(array)

    # The array from [0, ... , i] is the heap
    # The array from [i+1, ... , end] is in sorted order
    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        sift_down(array, 0, i - 1)


def heapify(array):
    # Root Node is at index 0
    # Nth Node is at index (n + 1)
    # Left Child is at index (2n + 1)
    # Right Child is at index (2n + 2)

    # Start with the parent of the last element
    # Sift down the node to its proper place
    for i in range((len(array) - 2) // 2, -1, -1):
        sift_down(array, i, len(array) - 1)


def sift_down(array, root, end):
    # Continually swap the root with the greatest child
    # until there's no more children or the root is greater than the children
    while 2 * root + 1 <= end:
        swap = root
        child = 2 * root + 1  # left child

        # Check left child
        if array[child] > array[swap]:
            swap = child

        # Check right child
        if (child + 1 <= end) and (array[child + 1] > array[swap]):
            swap = child + 1

        if swap == root:
            # The root is greater than its children
            return
        else:
            array[swap], array[root] = array[root], array[swap]
            root = swap


def merge_sort(array):
    if not array:
        return

    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, array)


def merge(first, second, array):
    index_first = 0
    index_second = 0
    j = 0

    while index_first < len(first) and index_second < len(second):
        if first[index_first] < second[index_second]:
            array[j] = first[index_first]
            index_first += 1
        else:
            array[j] = second[index_second]
            index_second += 1
        j += 1

    while index_first < len(first):
        array[j] = first[index_first]
        index_first += 1
        j += 1

    while index_second < len(second):
        array[j] = second[index_second]
        index_second += 1
        j += 1


def quick_sort(array, lower_index=None, higher_index=None):
    if not array:
        return

    if lower_index is None and higher_index is None:
        quick_sort(array, 0, len(array) - 1)

    if (lower_index is not None) and (higher_index is not None) \
            and (lower_index < higher_index):
        pivot_index = partition(array, lower_index, higher_index)
        quick_sort(array, lower_index, pivot_index - 1)
        quick_sort(array, pivot_index + 1, higher_index)


def partition(array, lowerIndex, higherIndex):
    # Pick a pivot between lower index and higher index
    pivot_index = random.randint(lowerIndex, higherIndex)

    # Place pivot at the end of the subarray
    array[higherIndex], array[pivot_index] = \
        array[pivot_index], array[higherIndex]

    pivot_index = higherIndex
    pivot = array[pivot_index]

    # Partitioning
    i = lowerIndex
    for j in range(lowerIndex, higherIndex):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    # Move the pivot into position i
    array[i], array[pivot_index] = array[pivot_index], array[i]

    # Return pivot index
    return i


def quick_sort3(array, lowerIndex=None, higherIndex=None):
    if not array:
        return

    if lowerIndex is None and higherIndex is None:
        quick_sort3(array, 0, len(array) - 1)

    if (lowerIndex is not None) and (higherIndex is not None) \
            and (lowerIndex < higherIndex):
        # Pick a pivot between lower index and higher index
        pivot_index = random.randint(lowerIndex, higherIndex)

        # Place pivot at the start of the sub-array
        array[lowerIndex], array[pivot_index] = \
            array[pivot_index], array[lowerIndex]

        pivot_index = lowerIndex
        pivot = array[pivot_index]

        # The upper index of the "less than pivot" partition
        lt = lowerIndex
        # The lower index of the "greater than pivot" partition
        gt = higherIndex

        # Partitioning
        i = lowerIndex + 1
        while i <= gt:
            if array[i] < pivot:
                array[i], array[lt] = array[lt], array[i]
                i += 1
                lt += 1

            elif array[i] > pivot:
                array[i], array[gt] = array[gt], array[i]
                gt -= 1

            else:
                i += 1

        # Recursively call on the left and right partitions
        quick_sort3(array, lowerIndex, lt - 1)
        quick_sort3(array, gt + 1, higherIndex)


def is_sorted(list):
    return bool(all(list[i] <= list[i + 1] for i in range(len(list) - 1)))


def main():
    size = 1000
    n = 1000

    my_list = [(random.randint(0, n)) for _ in range(size)]
    print("Bubble Sort")
    start = time.time()
    bubble_sort(my_list)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (is_sorted(my_list), duration))

    my_list = [(random.randint(0, n)) for _ in range(size)]
    print("Selection Sort")
    start = time.time()
    selection_sort(my_list)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (is_sorted(my_list), duration))

    my_list = [(random.randint(0, n)) for _ in range(size)]
    print("Insertion Sort")
    start = time.time()
    insertion_sort(my_list)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (is_sorted(my_list), duration))

    my_list = [(random.randint(0, n)) for _ in range(size)]
    print("Heap Sort")
    start = time.time()
    heap_sort(my_list)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (is_sorted(my_list), duration))

    my_list = [(random.randint(0, n)) for _ in range(size)]
    print("Merge Sort")
    start = time.time()
    merge_sort(my_list)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (is_sorted(my_list), duration))

    my_list = [(random.randint(0, n)) for _ in range(size)]
    print("Quick Sort")
    start = time.time()
    quick_sort(my_list)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (is_sorted(my_list), duration))

    my_list = [(random.randint(0, n)) for _ in range(size)]
    print("Quick Sort (3-Way Partition)")
    start = time.time()
    quick_sort3(my_list)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (is_sorted(my_list), duration))

    my_list = [(random.randint(0, n)) for _ in range(size)]
    print("Python Sort")
    start = time.time()
    my_list.sort()
    duration = time.time() - start
    print("(%s): %f seconds\n" % (is_sorted(my_list), duration))


if __name__ == '__main__':
    main()
