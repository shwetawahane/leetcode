def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        while(i<length):
            if nums.count(nums[i]) > 1:
                nums.pop(nums.index(nums[i]) +1)
                length-=1
            else:
                i+=1
        return len(nums)
      
