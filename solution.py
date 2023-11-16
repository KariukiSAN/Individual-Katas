def find_smallest_subarray(arr):
    if all_same(arr) or is_sorted(arr):
        return [0, 0]

    n = len(arr)
    start, end = 0, n - 1

    while start < n - 1 and arr[start] <= arr[start + 1]:
        start += 1

    while end > 0 and arr[end] >= arr[end - 1]:
        end -= 1

    subarray_min = min(arr[start:end+1])
    subarray_max = max(arr[start:end+1])

    while start > 0 and arr[start - 1] > subarray_min:
        start -= 1

    while end < n - 1 and arr[end + 1] < subarray_max:
        end += 1

    return [start, end]


def all_same(arr):
    return len(set(arr)) == 1


def is_sorted(arr):
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)



arr = [1, 2, 3, 6, 4, 4]
result = find_smallest_subarray(arr)
print(result)  