# Merge Sort Implementation in Python

This repository contains a simple and clear implementation of the **Merge Sort** algorithm in Python.

## What is Merge Sort?

Merge Sort is a popular, efficient, and stable sorting algorithm that uses the divide-and-conquer approach. It divides the input array into smaller subarrays, sorts them recursively, and then merges the sorted subarrays to produce the final sorted array.

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Stable:** Yes

## Files

- `merge_sort.py` – Contains the implementation of the Merge Sort algorithm and an example usage.

## Usage

1. **Clone the Repository**
    ```sh
    git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>
    ```

2. **Run the Script**
    ```sh
    python merge_sort.py
    ```

    You should see output like:
    ```
    Original: [38, 27, 43, 3, 9, 82, 10]
    Sorted: [3, 9, 10, 27, 38, 43, 82]
    ```

3. **Using the Function in Your Code**
    Import the `merge_sort` function and use it to sort lists:
    ```python
    from merge_sort import merge_sort

    data = [5, 2, 4, 6, 1, 3]
    sorted_data = merge_sort(data)
    print(sorted_data)
    ```

## How It Works

- The `merge_sort` function splits the array into halves recursively.
- The `merge` function then combines two sorted halves into a single sorted list.

## Example

```python
sample = [38, 27, 43, 3, 9, 82, 10]
sorted_sample = merge_sort(sample)
print(sorted_sample)  # Output: [3, 9, 10, 27, 38, 43, 82]
```

## License

This project is licensed under the MIT License.
