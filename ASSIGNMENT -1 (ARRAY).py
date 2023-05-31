#                                                       ASSIGNMENT -1 
#                                                       Topic - ARRAY

# Solution 1 : 

# from typing import List
# class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        seen = {}
#        for i, value in enumerate(nums):
#            remaining = target - nums[i]
           
#            if remaining in seen:
#                return [i, seen[remaining]]
            
#            seen[value] = i 

# nums = [2,7,11,15]
# target = 9
# s=Solution()
# print(s.twoSum(nums,target))






# Solution 2 : 

# from typing import List
# class RemoveElement:
#     def removeElement(nums: List[int], val: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[count] = nums[i]
#                 count += 1
#         return count
    
#     nums = [3, 2, 2, 3]
#     val = 3

#     count = removeElement(nums, val)
#     print(nums)




# Solution 3:

# def find_index(arr, n, K):
#     for i in range(n):
#         if arr[i] == K:
#             return i
#         elif arr[i] > K:
#             return i
#     return n
# arr = [1, 3, 5, 6]
# n = len(arr)
# K = 2
# print(find_index(arr, n, K))




# Solution 4 :
# from typing import List
# def plusOne(self, digits: List[int]) -> List[int]:
#         for i in range(len(digits)-1,-1,-1):
#             if digits[i]<9:
#                 digits[i]+=1
#                 return digits
#             digits[i]=0

#         return [1]+[0]*len(digits)
# def plusOne(digits):
#     num = 0
#     for i in range(len(digits)):
#     	num += digits[i] * pow(10, (len(digits)-1-i))
#     return [int(i) for i in str(num+1)]

# digits=[1,2,3]    
# new_digits = plusOne(digits)
# print(new_digits)




# solution 5: 

# class Solution(object):
#    def merge(self, nums1, m, nums2, n):
#       i = 0
#       j = 0
#       end = len(nums1)-1
#       while end>=0 and not nums1[end]:
#          end-=1
#       while j<len(nums2) :
#          if i>end and not nums1[i]:
#             nums1[i] = nums2[j]
#             j+=1
#          elif nums1[i]>nums2[j]:
#             self.shift(nums1,i)
#             nums1[i] = nums2[j]
#             end+=1
#             j+=1
#          i+=1
#       return nums1
#    def shift(self,num,i):
#       j = len(num)-1
#       while not num[j]:
#          j-=1
#       while j>=i:
#          num[j+1] = num[j]
#          j-=1
# ob = Solution()
# print(ob.merge([1,2,3,0,0,0],3,[2,5,6],3))




# Solution 6 : 
# def contains_duplicate(nums):
#     if nums is None or len(nums) == 0:
#         return False

#     nums.sort()
#     for i in range(1, len(nums)):
#         if nums[i - 1] == nums[i]:
#             return True

#     return False
# nums = [1, 2, 3, 1]
# print(contains_duplicate(nums))



# Solution 7:

# def move_zeros(nums):

#   non_zero_index = 0

#   for i in range(len(nums)):
    
#     if nums[i] != 0:
#       nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
#       non_zero_index += 1

#   for i in range(non_zero_index, len(nums)):
#     nums[i] = 0

#   return nums
# nums = [0,1,0,3,12]

# print(move_zeros(nums))


