"""
Python file for performance between python and cython
"""

import time
import py_sort
import cy_sort
import random

python_sort = py_sort
cython_sort = cy_sort

data =[]
for i in range(20000):
    data.append(random.uniform(-1000,1000))




formato_datos="{:.5f},{:5f},{:5f},{:5f}\n"
for i in range(30):    
    if i==0:
        with open("sort_20000.csv","a") as archivo:
	        archivo.write('time_python_bubble,time_cython_bubble,time_python_selection,time_cython_selection\n')


    #Bubble sort time
    init_time = time.time()
    python_sort.bubbleSort(data)
    fin_time = time.time()
    total_time_python_bubble = fin_time - init_time
    init_time = time.time()
    cython_sort.bubbleSort(data)
    fin_time = time.time()
    total_time_cython_bubble = fin_time - init_time

    #Selection sort time
    init_time = time.time()
    py_sort.selectionSort(data, len(data))
    fin_time = time.time()
    total_time_python_selection = fin_time - init_time

    init_time = time.time()
    cy_sort.selectionSort(data, len(data))
    fin_time = time.time()
    total_time_cython_selection = fin_time - init_time
    
    #csv data
    with open("sort_20000.csv","a") as archivo:
	    archivo.write(formato_datos.format(total_time_python_bubble,total_time_cython_bubble,total_time_python_selection,total_time_cython_selection))
