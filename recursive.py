"""Recursive

Recursive sorting:
Merge Sort
Quick Sort

"""

# Merge Sort


# def merge_sort(arr):
#     merge_sort2(arr, 0, len(arr) - 1)


# def merge_sort2(arr, first, last):
#     if first < last:
#         middle = (first + last) // 2
#         merge_sort2(arr, first, middle)
#         merge_sort2(arr, middle + 1, last)
#         merge(arr, first, middle, last)


# def merge(arr, first, middle, last):
#     L = arr[first:middle]
#     R = arr[middle:last + 1]
#     L.append(999)
#     R.append(999)
#     i = j = 0
#     for k in range(first, last + 1):
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1

# Merge Sort take 2

# def merge(arr, left, middle, right):
#     n1 = middle - left + 1
#     n2 = right - middle

#     # create temporary arrays
#     L = [0] * n1
#     R = [0] * n2

#     # copy data to temp arrays L[] and R[]
#     for i in range(0, n1):
#         L[i] = arr[left + i]
#     for j in range(0, n2):
#         R[j] = arr[middle + 1 + j]

#     # merge the temp arrays back
#     i = 0
#     j = 0
#     k = left

#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1

#     # copy the remaining elements of L[], if there are any
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#     # copy the remaining elements of R[], if there are any
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1


# def merge_sort(arr, left, right):
#     if left < right:
#         middle = left + (right - 1) // 2
#         merge_sort(arr, left, right)
#         merge_sort(arr, middle + 1, right)
#         merge(arr, left, middle, right)


# Quick Sort

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


test_list = [4, 2, 7, 3, 45, 23, 8, 354, 63, 239, 8, 299, 438, 92, 184, 91]
print("before sort:", test_list)
quick_sort(test_list, 0, len(test_list) - 1)
sorted_list = [*test_list]
print("sorted:", sorted_list)

# test_list2 = [4, 2, 7, 3, 45, 23, 8, 354, 63, 239, 8, 299, 438, 92, 184, 91]
# print("BEFORE MERGE SORT:", test_list2)
# merge_sort(test_list, 0, len(test_list) - 1)
# print("AFTER MERGE SORT:", test_list2)
