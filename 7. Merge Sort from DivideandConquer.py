# 7. Divide and Conquer Algorithms

# Merge Sort
"""Application: Merge Sort is used when large datasets need to be sorted, especially when the data can't fit entirely into memory (external sorting).
Example: It is commonly used in database management systems for efficient data sorting when dealing with large files and in situations like processing large lists of transactions or records."""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
# Test Merge Sort
arr4 = [12, 11, 13, 5, 6, 7]
merge_sort(arr4)
print("Merge Sort:", arr4)  # Expected: [5, 6, 7, 11, 12, 13]
            