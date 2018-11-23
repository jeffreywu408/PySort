#!/usr/local/bin/python3
import random
import time


def bubbleSort(array):
    if not array:
        return

    # The largest element is in correct sorted order after each pass
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]


def selectionSort(array):
    if not array:
        return

    for i in range(len(array)):
        # Linear search for the minimum
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j

        # Put minimum into correct place
        array[i], array[min] = array[min], array[i]


def insertionSort(array):
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


def heapSort(array):
    if not array:
        return

    Heapify(array)

    # The array from [0, ... , i] is the heap
    # The array from [i+1, ... , end] is in sorted order
    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        siftDown(array, 0, i - 1)


def Heapify(array):
    # Root Node is at index 0
    # Nth Node is at index (n + 1)
    # Left Child is at index (2n + 1)
    # Right Child is at index (2n + 2)

    # Start with the parent of the last element
    # Sift down the node to its proper place
    for i in range((len(array) - 2) // 2, -1, -1):
        siftDown(array, i, len(array) - 1);


def siftDown(array, root, end):
    # Continually swap the root with the greatest child
    # until theres's no more children or the root is greater than the children
    while (2 * root + 1 <= end):
        swap = root;
        child = 2 * root + 1  # left child

        # Check left child
        if (array[child] > array[swap]):
            swap = child

        # Check right child
        if ((child + 1 <= end) and (array[child + 1] > array[swap])):
            swap = child + 1

        if (swap == root):
            # The root is greater than its children
            return;
        else:
            array[swap], array[root] = array[root], array[swap]
            root = swap


def mergeSort(array):
    if not array:
        return

    if (len(array) > 1):
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)
        merge(left, right, array)


def merge(first, second, array):
    indexFirst = 0;
    indexSecond = 0;
    j = 0;

    while (indexFirst < len(first) and indexSecond < len(second)):
        if (first[indexFirst] < second[indexSecond]):
            array[j] = first[indexFirst]
            indexFirst += 1
        else:
            array[j] = second[indexSecond]
            indexSecond += 1
        j += 1

    while (indexFirst < len(first)):
        array[j] = first[indexFirst]
        indexFirst += 1
        j += 1

    while (indexSecond < len(second)):
        array[j] = second[indexSecond]
        indexSecond += 1
        j += 1


def quickSort(array, lowerIndex=None, higherIndex=None):
    if not array:
        return

    if (lowerIndex is None and higherIndex is None):
        quickSort(array, 0, len(array) - 1)

    if (lowerIndex is not None) and (higherIndex is not None) and (lowerIndex < higherIndex):
        pivotIndex = partition(array, lowerIndex, higherIndex)
        quickSort(array, lowerIndex, pivotIndex - 1)
        quickSort(array, pivotIndex + 1, higherIndex)


def partition(array, lowerIndex, higherIndex):
    # Pick a pivot between lower index and higher index
    pivotIndex = random.randint(lowerIndex, higherIndex)

    # Place pivot at the end of the subarray
    array[higherIndex], array[pivotIndex] = array[pivotIndex], array[higherIndex]

    pivotIndex = higherIndex
    pivot = array[pivotIndex]

    # Partitioning
    i = lowerIndex
    # for (int j = lowerIndex; j < higherIndex; j++):
    for j in range(lowerIndex, higherIndex):
        if (array[j] <= pivot):
            array[i], array[j] = array[j], array[i]
            i += 1

    # Move the pivot into position i
    array[i], array[pivotIndex] = array[pivotIndex], array[i]

    # Return pivot index
    return i


def quickSort3(array, lowerIndex=None, higherIndex=None):
    if not array:
        return

    if (lowerIndex is None and higherIndex is None):
        quickSort3(array, 0, len(array) - 1)

    if (lowerIndex is not None) and (higherIndex is not None) and (lowerIndex < higherIndex):
        # Pick a pivot between lower index and higher index
        pivotIndex = random.randint(lowerIndex, higherIndex)

        # Place pivot at the start of the sub-array
        array[lowerIndex], array[pivotIndex] = array[pivotIndex], array[lowerIndex]

        pivotIndex = lowerIndex
        pivot = array[pivotIndex]

        # The upper index of the "less than pivot" partition
        lt = lowerIndex
        # The lower index of the "greater than pivot" partition
        gt = higherIndex

        # Partitioning
        i = lowerIndex + 1
        while (i <= gt):
            if (array[i] < pivot):
                array[i], array[lt] = array[lt], array[i]
                i += 1
                lt += 1

            elif (array[i] > pivot):
                array[i], array[gt] = array[gt], array[i]
                gt -= 1

            else:
                i += 1

        # Recursively call on the left and right partitions
        quickSort3(array, lowerIndex, lt - 1)
        quickSort3(array, gt + 1, higherIndex)


def isSorted(list):
    return bool(all(list[i] <= list[i + 1] for i in range(len(list) - 1)))


def main():
    size = 1000;
    n = 1000;

    myList = [(random.randint(0, n)) for _ in range(size)]
    print("Bubble Sort")
    start = time.time()
    bubbleSort(myList)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (isSorted(myList), duration))

    myList = [(random.randint(0, n)) for _ in range(size)]
    print("Selection Sort")
    start = time.time()
    selectionSort(myList)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (isSorted(myList), duration))

    myList = [(random.randint(0, n)) for _ in range(size)]
    print("Insertion Sort")
    start = time.time()
    insertionSort(myList)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (isSorted(myList), duration))

    myList = [(random.randint(0, n)) for _ in range(size)]
    print("Heap Sort")
    start = time.time()
    heapSort(myList)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (isSorted(myList), duration))

    myList = [(random.randint(0, n)) for _ in range(size)]
    print("Merge Sort")
    start = time.time()
    mergeSort(myList)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (isSorted(myList), duration))

    myList = [(random.randint(0, n)) for _ in range(size)]
    print("Quick Sort")
    start = time.time()
    quickSort(myList)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (isSorted(myList), duration))

    myList = [(random.randint(0, n)) for _ in range(size)]
    print("Quick Sort (3-Way Partition)")
    start = time.time()
    quickSort3(myList)
    duration = time.time() - start
    print("(%s): %f seconds\n" % (isSorted(myList), duration))

    myList = [(random.randint(0, n)) for _ in range(size)]
    print("Python Sort")
    start = time.time()
    myList.sort()
    duration = time.time() - start
    print("(%s): %f seconds\n" % (isSorted(myList), duration))


if __name__ == '__main__':
    main()
