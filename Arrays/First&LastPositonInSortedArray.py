class Solution(object):
    def searchRange(self, nums, target):
            first = self.binarySearch(nums, target, True)
            second = self.binarySearch(nums, target, False)
            return [first, second]

    def binarySearch(self, nums, target, firstOccurrence):
            left, right = 0, len(nums) - 1
            i = -1

            while left <= right:
                middle = (left + right) // 2

                if nums[middle] == target:
                    i = middle
                    if firstOccurrence:
                        right = middle - 1
                    else:  # secondOccurrence i.e. firstOccurrence is False
                        left = middle + 1  # Triggers the 2nd B.S

                elif nums[middle] > target:
                    right = middle - 1

                else:  # nums[middle] < target
                    left = middle + 1

            return i