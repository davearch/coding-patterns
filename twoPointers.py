'''
Given an array of sorted numbers and a target sum, 
find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) 
such that they add up to the given target.

Example:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

[1, *2, 3, 4*, 6]
1 + 6 = 7
1 + 4 = 5
2 + 4 = 6
'''


def pairWithTargetSum(arr, target_sum):
    left, right = 0, len(arr) - 1

    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        
        if (current_sum > target_sum):
            right -= 1
        else:
            left += 1
    return [-1,-1]


'''
Given an array containing 0s, 1s and 2s, sort the array in-place. 
You should treat numbers of the array as objects, hence, 
we can’t count 0s, 1s, and 2s to recreate the array.

Example:
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

[*1, +0, 2, 1, 0*]
[0, *1, +2, 1, 0*]
[0, *1, +0, *1, 2]
[0, 0, *1, *1, +2]
'''

def dutch_national_flag(arr):
    low, high = 0, len(arr) - 1
    i = 0

    while (i <= high):
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else: # arr[i] == 2
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1