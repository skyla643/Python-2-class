def quicksort(arr):
    if len(arr) <= 1:
        return arr  # base case: arrays with 0 or 1 elements are already sorted
    else:
        pivot = arr[len(arr) // 2]  # choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # elements less than pivot
        middle = [x for x in arr if x == pivot]  # elements equal to pivot
        right = [x for x in arr if x > pivot]  # elements greater than pivot
        return quicksort(left) + middle + quicksort(right)  # recursively sort and combine

# Example usage:
array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quicksort(array)
print("Sorted array:", sorted_array)
