class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = count2 = 0
        element1,element2 = 0,1
        for num in nums:
            if count1 == 0 and element2 != num:
                count1 = 1
                element1 = num
            elif count2 == 0 and element1 != num:
                count2 = 1
                element2 = num
            elif element1 == num:
                count1 += 1
            elif element2 == num:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [num for num in [element1,element2] if nums.count(num)>len(nums)//3]