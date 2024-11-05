def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # base case: arrays with 0 or 1 elements are already sorted

    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    i = j = 0  # initialize pointers for left and right lists

    # Merge the lists by comparing elements from each list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append remaining elements from either list
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Example usage:
words = ["banana", "apple", "orange", "mango", "grape"]
sorted_words = merge_sort(words)
print("Sorted list:", sorted_words)
