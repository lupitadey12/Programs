"""
        Two Pointer Approach is failing one test case.
        Time Complexity & Space Complexity is O(n) - Singular Traversal
        You will need to sort it #nums.sort() else the logic doesn't hold good, so the T.C = O(nlogn) + O(n) = O(nlogn)

        Plus, when you do 2 Pointer Approach, you restricting the possibile combinations, you are checking one element's possibility with only one element
        You must check one element's possibility with n other elements in the array - Brute Force - O(n*n)
        
        Hence, we use Hash Map (Better T.C & Checks all Combinations)

        left = 0
        right = len(nums) - 1

        while left <= right:
            if (nums[left] + nums[right]) == target:
                return [left,right]
            elif (nums[left] + nums[right]) < target:
                left+= 1
            else: #nums[left] + nums[right] > target:
                right-=1
"""      
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
 
        #Hash Map
        #T.C and S.P is O(n)
        #**By the time I go to the second element, the first element would have already been in the HashMap
        
        #This should also pass for negative test cases.

        HashMap = {}
        #We need to fetch the index, in a dict values are accessed using keys
        #value : index

        #for index, value in enumerate(nums)
        #here- by default in enumerate, the first value will always hold index even if the naming convention is different
        for index, value in enumerate(nums):
            diff = target - value
            if diff in HashMap:
                return(HashMap[diff], index)#**
            HashMap[value] = index #value is the key of the dict, to be able to return the index in the HashMap against that value
        return []

