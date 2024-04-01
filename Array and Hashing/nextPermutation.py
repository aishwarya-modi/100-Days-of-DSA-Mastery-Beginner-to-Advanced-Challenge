A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the largest index i such that nums[i] < nums[i + 1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            # Array is in descending order, reverse it to get the first permutation
            nums.reverse()
            return

        # Step 2: Find the largest index j greater than i such that nums[j] > nums[i]
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1

        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the sub-array from index i + 1 to the end of the array
        nums[i + 1:] = reversed(nums[i + 1:])



Time Complexity:
Finding i: In the worst case, we traverse the entire array once to find the largest index i such that nums[i] < nums[i + 1]. This operation takes O(n), where n is the length of the input list nums.
Finding j: Once i is found, we traverse the array again to find the largest index j greater than i such that nums[j] > nums[i]. This operation takes O(n) in the worst case.
Swapping and Reversing: Swapping two elements and reversing a sub-array both take O(n) time, where n is the length of the sub-array being reversed.
Since all the operations are performed sequentially, the overall time complexity is O(n).

Space Complexity:
The space complexity is O(1) because we are not using any extra space that grows with the input size. We are modifying the input list nums in place without using any additional data structures.

Intuition:
The algorithm for finding the next permutation is based on observing patterns in the sequence of permutations. It aims to find the next lexicographically greater permutation by identifying the rightmost pair of elements that can be swapped to achieve the next permutation. By following a series of steps (finding i, finding j, swapping elements, and reversing a sub-array), we ensure that the resulting permutation is the next lexicographically greater one.

Overall, the algorithm efficiently finds the next permutation while using minimal additional space. It is based on simple operations like comparison, swapping, and reversing, making it easy to understand and implement.





