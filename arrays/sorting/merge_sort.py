def merge_sort(arr, s, e):
    if s >= e:
        return

    mid = (s + e) // 2
    merge_sort(arr, s, mid)
    merge_sort(arr, mid + 1, e)
    merge(arr, s, e)

def merge(arr, s, e):
    mid = (s + e) // 2
    len1 = mid - s + 1
    len2 = e - mid
    arr1 = [0] * len1
    arr2 = [0] * len2

    original_array_index = s
    for i in range(len1):
        arr1[i] = arr[original_array_index]
        original_array_index += 1

    original_array_index = mid + 1
    for i in range(len2):
        arr2[i] = arr[original_array_index]
        original_array_index += 1

    original_array_index = s
    idx1 = 0
    idx2 = 0
    while idx1 < len1 and idx2 < len2:
        if arr1[idx1] < arr2[idx2]:
            arr[original_array_index] = arr1[idx1]
            idx1 += 1
        else:
            arr[original_array_index] = arr2[idx2]
            idx2 += 1
        original_array_index += 1

    while idx1 < len1:
        arr[original_array_index] = arr1[idx1]
        idx1 += 1
        original_array_index += 1

    while idx2 < len2:
        arr[original_array_index] = arr2[idx2]
        idx2 += 1
        original_array_index += 1

arr = [8, 9, 2, 5, 1]
size = 5

print("Before Sorting:")
for i in range(size):
    print(arr[i], end=" ")
print()

merge_sort(arr, 0, size - 1)

print("After Sorting:")
for i in range(size):
    print(arr[i], end=" ")
