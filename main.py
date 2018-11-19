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
            if array[min] > array[j]: 
                min_idx = j   
                
        # Put minimum into correct place     
        array[i], array[min] = array[min], array[i] 
        

def insertionSort(array): 
    if not array:
        return
    
    for i in range(1, len(array)): 
        # Take an unsorted element and insert it into correct sorted spot
        key = array[i]
        j = i - 1
        while j >=0 and key < array[j] : 
            array[j+1] = array[j] 
            j -= 1
        array[j+1] = key 
        

#def heapSort(array):

#def mergeSort(array):

#def quickSort(array):

#def quickSort3(array):

def isSorted(list):
    return bool(all(list[i] <= list[i+1] for i in range(len(list)-1)))

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
    
    

if __name__ == '__main__':
    main()