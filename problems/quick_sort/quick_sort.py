import random

def quicksort(arr):
    """
    Sorts the array using the QuickSort algorithm with Hoare's partition scheme
    and random pivot selection for optimal average performance.
    """
    def _quicksort(items, low, high):
        if low < high:
            pivot_index = partition(items, low, high)
            _quicksort(items, low, pivot_index)
            _quicksort(items, pivot_index + 1, high)

    def partition(items, low, high):
        # Random pivot selection to avoid worst-case scenarios
        pivot_idx = random.randint(low, high)
        items[low], items[pivot_idx] = items[pivot_idx], items[low]
        pivot = items[low]
        
        left = low + 1
        right = high
        while True:
            while left <= right and items[left] < pivot:
                left += 1
            while left <= right and items[right] > pivot:
                right -= 1
            if left > right:
                break
            items[left], items[right] = items[right], items[left]
            left += 1
            right -= 1
        items[low], items[right] = items[right], items[low]
        return right

    _quicksort(arr, 0, len(arr)-1)
    return arr
