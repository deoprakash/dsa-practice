'''
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Examples :

Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.
Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.
'''

def rotateArray(arr, d):
    n = len(arr)
    d %= n
    print(arr)
    print("=====================")
    reverseArr(arr, 0, d-1)
    reverseArr(arr, d, n-1)
    reverseArr(arr, 0, n-1)

def reverseArr(arr, start, end):
    while start < end :
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

        print("====================")
        print(arr)
        print("====================")

rotateArray([1, 2, 3, 4, 5], 2)


'''
DRY RUN :- 

====================
[2, 1, 3, 4, 5]
====================
====================
[2, 1, 5, 4, 3]
====================
====================
[3, 1, 5, 4, 2]
====================
====================
[3, 4, 5, 1, 2]
====================

'''