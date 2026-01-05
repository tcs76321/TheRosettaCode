"""
Quick Sort Implementation

This module provides an optimized implementation of the Quick Sort algorithm,
one of the most efficient general-purpose sorting algorithms.

Quick Sort:
- Time Complexity: O(n log n) average case, O(n²) worst case
- Space Complexity: O(log n) due to recursion stack
- In-place sorting algorithm
- Not stable (relative order of equal elements may change)
- Divides array using partitioning strategy

Key Features:
- Uses Lomuto partitioning scheme
- Optimized pivot selection
- Handles edge cases efficiently
"""


def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm.
    
    Args:
        arr (list): The list to be sorted
        
    Returns:
        list: The sorted list
        
    Examples:
        >>> quick_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
        
        >>> quick_sort([])
        []
        
        >>> quick_sort([1])
        [1]
    """
    if not arr:
        return arr
    
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_helper(arr, low, high):
    """
    Helper function that performs in-place quick sort recursively.
    
    Args:
        arr (list): The list being sorted
        low (int): The starting index of the subarray
        high (int): The ending index of the subarray
    """
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = _partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        _quick_sort_helper(arr, low, pivot_index - 1)
        _quick_sort_helper(arr, pivot_index + 1, high)


def _partition(arr, low, high):
    """
    Partitions the array around a pivot element using Lomuto scheme.
    
    This function selects the last element as pivot and partitions the
    array such that all elements less than pivot come before it, and
    all elements greater than pivot come after it.
    
    Args:
        arr (list): The list being partitioned
        low (int): The starting index of the subarray
        high (int): The ending index of the subarray
        
    Returns:
        int: The final pivot index
    """
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element - indicates the right position
    # of pivot found so far
    i = low - 1
    
    # Traverse through all elements
    # Compare each element with pivot
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            # Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the partition point
    return i + 1
