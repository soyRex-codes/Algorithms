# 1. Sorting Algorithms

# Bubble Sort: Efficient but only for small datasets
"""Application: While not widely used in real-world applications due to inefficiency, it's often taught as an introductory sorting algorithm and is used in educational tools or small datasets where simplicity matters.
Example: Sorting short lists of records or during classroom demos for algorithm comparison."""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Optimized by adding a swapped flag
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # If no elements were swapped, stop early
            break
        
# Test Bubble Sort
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Bubble Sort:", arr)  # Expected: [11, 12, 22, 25, 34, 64, 90]        