def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        arr (list): List of elements to be sorted.

    Returns:
        list: Sorted list of elements.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted lists into one sorted list.

    Args:
        left (list): First sorted list.
        right (list): Second sorted list.

    Returns:
        list: Merged sorted list.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", sample)
    sorted_sample = merge_sort(sample)
    print("Sorted:", sorted_sample)