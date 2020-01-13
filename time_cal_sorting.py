import random
import sorting_algo
import time

def rand_int(size,max):
    arr = []
    for i in range(size):
        arr.append(random.randint(1,max))
    return arr

size = int(input("enter the size of list "))
max = int(input("enter the range of integer list "))
times = int(input("how many times you want to run it"))

l = rand_int(size,max)

def analyse_func(func_name,arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t-->elapsed time: {seconds:.5f}")

for num in range(times):
    #analyse_func(sorting_algo.bubble_sorting,l.copy())
    #analyse_func(sorting_algo.split_array,l)
    analyse_func(sorting_algo.quick_sorting,l)
    analyse_func(sorted,l)
    print("-"*30)
# analyse_func(sorting_algo.selection_sorting,l.copy())
# analyse_func(sorting_algo.insertion_sorting,l.copy())
