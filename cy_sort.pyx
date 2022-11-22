"""
Python class implementing sort methods
Name: Julian Cardenas
Date: 10/11/2022
"""

#imports
from cpython cimport array
import array


"""---------------------------------------------------
BubbleSort in Python
code from https://www.programiz.com/dsa/bubble-sort
---------------------------------------------------"""
def bubbleSort(object array):
    
    cdef int i, j   
    cdef double temp 
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


"""------------------------------------------------------------------------------
Cython program for implementation of Quicksort Sort
---------------------------------------------------------------------------------"""
 
def selectionSort(object array,int size):
    cdef int ind, min_index, j
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
    
    return array
 