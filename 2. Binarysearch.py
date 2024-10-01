# 2. Search Algorithms

# Binary Search: Efficient for sorted arrays

"""Application: Used to search efficiently in sorted datasets. It is used in scenarios where search performance is critical.
Example: Searching in large databases or file systems, looking up dictionary words in a digital dictionary, or locating entries in an ordered contact list.
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found

# Test Binary Search
sorted_arr3 = [1, 2, 3, 4, 5, 6, 7]
index = binary_search(sorted_arr3, 4)
print("Binary Search (element's target) index is:", index)  # Expected: 3 (index of 4)

index_not_found = binary_search(sorted_arr3, 10)
print("Binary Search (10):", index_not_found)  # Expected: -1 (not found)