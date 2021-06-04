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
      
#Alternate Java implementation
"""
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
"""
