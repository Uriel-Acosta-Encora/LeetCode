from collections import Counter

class Solution:
    def unequalTriplets(self, nums):
        count = Counter(nums)
        values = list(count.values())
        total = sum(values)
        triplets = 0
        left = 0
        
        for cnt in values:
            right = total - left - cnt
            triplets += left * cnt * right
            left += cnt

        return triplets


#First#
# Solution 1 o(n^3):
# class Solution:
#     def unequalTriplets(self, nums: List[int]) -> int:
#         triplets = 0
#         for i in range(len(nums)):
#             count = [nums[i]]
#             for k in range(i+1,len(nums)):
#                 sub_count = count.copy()
#                 if nums[k] not  in count:
#                     sub_count.append(nums[k])
#                     for j in range(k+1,len(nums)):
#                         sub_sub = sub_count.copy()
#                         if nums[j] not  in sub_sub:
#                             sub_sub.append(nums[j])
#                             if len(sub_sub) == 3:
#                                 triplets += 1
                                
#         return(triplets)