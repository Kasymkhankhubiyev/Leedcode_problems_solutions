def removeDuplicates(self, nums: List[int]) -> int:
        amount = 0
        indexs = []
        numbers = []
        for i in range(len(nums)):
            if not nums[i] in numbers:
                numbers.append(nums[i])
                amount += 1
            else:
                indexs.append(i)
        count = 0
        for i in range(len(indexs)):
            nums.pop(indexs[i] - count)
            count += 1
        return amount
