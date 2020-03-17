# recursive-sorting-examples

## Merge Sort

Imagine you are holding _n_ cards in your hand...

1. Divide in half until you have subarrays of length 1 (remember, lists with len(1) are sorted!)
2. Merge sorted lists together
   --- Compare two subarrays (now holding 2 elements in each) and look at the front of each, compare and merge as needed

To note about MergeSort:

- Is recursive
- Divide and conquer algorithm
- very efficient for large data sets
  Merge Sort does log n merge steps because each merge step doubles the list size.
  O(n logn)

## Quick Sort

Imagine you are holding _n_ cards in your hand...

1. Choose a _pivot_ (we'll choose the 1st element, but that's not set in stone)
2. Move all elements less than the pivot to its LHS
3. Move all elements greater than the pivot to its RHS
4. Repeat steps 1-3 until array is sorted
