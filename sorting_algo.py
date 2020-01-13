##sorting algorithm


# #bubble sorting
# def bubble_sorting(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-1):
#             if arr[j+1]<arr[j]:
#                 arr[j+1],arr[j] = arr[j],arr[j+1]
#     return arr


##bubble_soritng_optimized
def bubble_sorting(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for j in range(len(arr)-1):
            if arr[j+1]<arr[j]:
                swap_happened = True
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr


##selection_sorting
def selection_sorting(arr):
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr


##insertion_sorting
def insertion_sorting(arr):
    for i in range(1,len(arr)):
        swap_happened = True
        c = i
        while swap_happened and c>0:
            swap_happened = False
            if arr[c-1]>arr[c]:
                swap_happened = True
                arr[c-1],arr[c] = arr[c],arr[c-1]
                c-=1
    return arr



##quick_sorting_algorithm
def quick_sorting(arr):
    if len(arr)<2:
        return arr
    else:
        a = arr[-1]
        arr1 = []#smaller elements
        arr2 = []#larger elements
        arr3 = []#equal elements
        for item in arr:
            if item<a:
                arr1.append(item)
            elif item==a:
                arr3.append(item)
            else:
                arr2.append(item)
        return quick_sorting(arr1)+ arr3 +quick_sorting(arr2)

##merge_sorting----split -> sort -> merge
def merge_sorting(arr1,arr2):
    ##both array sorted
    ##print(f"performing merge sort on two sorted arrays {arr1} and {arr2}")
    arr3 = []
    i,j=0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    while i<len(arr1):
        arr3.append(arr1[i])
        i+=1
    while j<len(arr2):
        arr3.append(arr2[j])
        j+=1
    #arr3.extend(list(set(arr2+arr1)-set(arr3)))##my_logic
    return arr3

def split_array(arr):
    if len(arr)<2:
        #print(f"base condition arrived and base_array is:{arr[:]}")
        return arr[:]
    else:
        # print("dividing array into two arrays in left and right")
        # print(f"left_array:{arr[:len(arr)//2]}")
        # print(f"right_array:{arr[len(arr)//2:]}")
        l1 = split_array(arr[:len(arr)//2])
        l2 = split_array(arr[len(arr)//2:])
        return merge_sorting(l1,l2)
