"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

def searchInsert(self, nums: List[int], target: int) -> int:

        if target in nums:
            return nums.index(target)
        elif target < nums[0]:
            return 0
        elif target > nums[len(nums)-1]:
            return len(nums)
        else:
            if len(nums) > 2:
                nums1 = nums[:len(nums)//2 +1]
                nums2 = nums[len(nums)//2 + 1:]
                # print(nums1, nums2)
                if target < nums2[0]:
                    return self.searchInsert(nums1, target)
                else:
                    return len(nums1) + self.searchInsert(nums2, target)
            else:
                return 1
