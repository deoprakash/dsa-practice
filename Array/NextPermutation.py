'''
Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

Note:  A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

Examples:

Input: arr[] = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next permutation of the given array is [2, 4, 5, 0, 1, 7].
Input: arr[] = [3, 2, 1]
Output: [1, 2, 3]
Explanation: As arr[] is the last permutation, the next permutation is the lowest one.
Input: arr[] = [3, 4, 2, 5, 1]
Output: [3, 4, 5, 1, 2]
Explanation: The next permutation of the given array is [3, 4, 5, 1, 2].
'''

def nextPermut(arr):
    n = len(arr)
    pivot = -1

    for i in range(n-2, -1, -1): #finding pivot element
        if arr[i] < arr[i+1]:
            pivot = i
            print(f"Pivot element: {arr[i]}")
            break
    
    if pivot == -1: #if no pivot element then reverse whole array
        arr.reverse()
        return arr
    
    for i in range(n-1, -1, -1): # swap element greater than pivot element
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            print("Swapped Pivot and closest greater element: ", arr[i], " & ", arr[pivot])
            break

    left, right = pivot+1, n-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
    
    return arr

arr = [2, 4, 1, 7, 5, 0]

print("initial arr: ", arr)

result = nextPermut(arr)

print("final result: ", result)

'''
OUTPUT & DRY RUN

initial arr:  [2, 4, 1, 7, 5, 0]
Pivot element: 1
Swapped Pivot and closest greater element:  1  &  5 => [2, 4, 5, 7, 1, 0]
final result:  [2, 4, 5, 0, 1, 7]

'''

     

    