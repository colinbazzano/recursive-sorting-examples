# Quick Sort

[5, 9, 3, 7, 2, 8, 1, 6]

# pick first number

# append all smaller to new array left
# append all larger to new array right

[3 2 1][5][9 7 8 6]

# recurse left

[2 1][3][5][9 7 8 6]

# recurse left

[1][2][][3][]

# recurse left

# found the base case, as 1 is sorted

# recurse right
# empty array base case

# recurse right
# another empty array base case

# recurse right
[1][2][][3][][5][7 8 6][9][]

# recurse left

[1][2][][3][][5][6][7][8][][9][]

# appending
[1, 2][3]
[1, 2, 3]

# plan
# base case: if array length is 0 or 1
# return array
# else:
# pick pivot (might as well pick first because its unsorted, none are better than the rest)
# put anything smaller into left array
# put anything bigger into right array
# return quicksort(left) + quicksort(right)
