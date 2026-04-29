import random

def knn_distance(arr, q, k):
    pairs = [(abs(x - q), x) for x in arr]
    return quickselect(pairs, 0, len(pairs), k - 1)

def quickselect(arr, start, stop, k):
    pivot_ix = random.randint(start, stop - 1)
    pivot_final_ix = partition(arr, start, stop, pivot_ix)

    if pivot_final_ix == k:
        return arr[pivot_final_ix]
    elif k < pivot_final_ix:
        return quickselect(arr, start, pivot_final_ix, k)
    else:
        return quickselect(arr, pivot_final_ix + 1, stop, k)

def partition(arr, start, stop, pivot_ix):
    pivot = arr[pivot_ix]
    arr[pivot_ix], arr[stop - 1] =  arr[stop - 1], arr[pivot_ix]
    store_ix = start
    for i in range(start, stop - 1):
        if arr[i][0] < pivot[0]:
            arr[i], arr[store_ix] = arr[store_ix], arr[i]
            store_ix += 1
    
    arr[store_ix], arr[stop - 1] = arr[stop - 1], arr[store_ix]
    return store_ix