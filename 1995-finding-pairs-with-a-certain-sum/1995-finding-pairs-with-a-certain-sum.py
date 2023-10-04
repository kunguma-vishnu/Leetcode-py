class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.dict_nums1 = collections.Counter(nums1)
        self.dict_nums2 = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_value = self.nums2[index]
        new_value = self.nums2[index] + val
        self.nums2[index] = new_value
        self.dict_nums2[old_value] -= 1
        self.dict_nums2[new_value] += 1

    def count(self, tot: int) -> int:
        count = 0
        for key in self.dict_nums1:
            remainder = tot - key
            if remainder in self.dict_nums2:
                count += self.dict_nums1[key] * self.dict_nums2[remainder]
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)