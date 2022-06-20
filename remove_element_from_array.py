def removeElement(self, nums: List[int], val: int) -> int:
        indexes = []
        for i in range(len(nums)):
            if nums[i] == val:
                indexes.append(i)
        count = 0
        for index in indexes:
            nums.pop(index - count)
            count += 1
            
        result = len(nums)
        return result
