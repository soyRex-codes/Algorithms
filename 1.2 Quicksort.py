# 1. Sorting Algorithms

# Quick Sort: Efficient for large datasets
"""Application: Used in various real-world applications due to its efficiency. It’s commonly used in systems that require sorting of large datasets.
Example: Libraries like Python’s sort() and Java’s Arrays.sort() are typically built on the Quick Sort algorithm for large data sets. It is used in databases and file-sorting tools."""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right) 

# Test Quick Sort
arr2 = [10, 7, 8, 9, 1, 5]
sorted_arr2 = quick_sort(arr2)
print("Quick Sort:", sorted_arr2)  # Expected: [1, 5, 7, 8, 9, 10]