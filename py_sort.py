"""
Python class implementing sort methods
Name: Julian Cardenas
Date: 10/11/2022
"""
"""---------------------------------------------------
BubbleSort in Python
code from https://www.programiz.com/dsa/bubble-sort
---------------------------------------------------"""
def bubbleSort(array):
        
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



"""---------------------------------------------------
SelectionSort in Python
https://www.geeksforgeeks.org/python-program-for-selection-sort/#:~:text=The%20selection%20sort%20algorithm%20sorts,Remaining%20subarray%20which%20is%20unsorted.
---------------------------------------------------"""
def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
    return array