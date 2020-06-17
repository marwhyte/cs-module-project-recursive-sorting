# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here\
    countArrA = countArrB = 0
    for i in range(elements):
        if countArrA >= len(arrA):
            merged_arr[i] = arrB[countArrB]
            countArrB += 1
        elif countArrB >= len(arrB):
            merged_arr[i] = arrA[countArrA]
            countArrA += 1
        elif arrA[countArrA] < arrB[countArrB]:
            merged_arr[i] = arrA[countArrA]
            countArrA += 1
        else:
            merged_arr[i] = arrB[countArrB]
            countArrB += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        return merge(merge_sort(left), merge_sort(right))

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
