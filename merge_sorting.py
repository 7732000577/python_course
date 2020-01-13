
##merge_sorting----split -> sort -> merge
# #l = [6,8,1,4,10,7,8,9,3,2,5]
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
# a = [2,4,6,8,10]
# b = [1,3,5,7,8,9]
# result4 = merge_sorting(a,b)
# print(result4)



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

#arr = [3,4,3,4,55,5]
arr = [6,8,1,4,10,7,8,9,3,2,5]
result = split_array(arr)
print(result)
