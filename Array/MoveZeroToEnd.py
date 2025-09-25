'''
You are given an array arr[] of non-negative integers. You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.
Input: arr[] = [0, 0]
Output: [0, 0]

'''

def moveZeroes(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    print(arr)

    

result = moveZeroes([1, 2, 0, 4, 3, 0, 5, 0])

'''
Dry Run: 

before swapping:  [1, 2, 0, 4, 3, 0, 5, 0]
iteration: 0 -> 1, Count No.: 0 -> 1
after swapping:  [1, 2, 0, 4, 3, 0, 5, 0]
iteration: 0 -> 1, Count No.: 1 -> 2
==================
before swapping:  [1, 2, 0, 4, 3, 0, 5, 0]
iteration: 1 -> 2, Count No.: 1 -> 2
after swapping:  [1, 2, 0, 4, 3, 0, 5, 0]
iteration: 1 -> 2, Count No.: 2 -> 0
==================
Skipped
iteration: 2 -> 0, Count No.: 2 -> 0
=================
before swapping:  [1, 2, 0, 4, 3, 0, 5, 0]
iteration: 3 -> 4, Count No.: 2 -> 0
after swapping:  [1, 2, 4, 0, 3, 0, 5, 0]
iteration: 3 -> 0, Count No.: 3 -> 0
==================
before swapping:  [1, 2, 4, 0, 3, 0, 5, 0]
iteration: 4 -> 3, Count No.: 3 -> 0
after swapping:  [1, 2, 4, 3, 0, 0, 5, 0]
iteration: 4 -> 0, Count No.: 4 -> 0
==================
Skipped
iteration: 5 -> 0, Count No.: 4 -> 0
=================
before swapping:  [1, 2, 4, 3, 0, 0, 5, 0]
iteration: 6 -> 5, Count No.: 4 -> 0
after swapping:  [1, 2, 4, 3, 5, 0, 0, 0]
iteration: 6 -> 0, Count No.: 5 -> 0
==================
Skipped
iteration: 7 -> 0, Count No.: 5 -> 0
=================
'''