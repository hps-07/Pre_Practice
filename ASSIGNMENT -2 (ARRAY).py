

#Solution 1:
# def group_integers_into_pairs(nums):
#   nums.sort()
#   sum_min = 0

#   for i in range(0, len(nums), 2):
#     sum_min += min(nums[i], nums[i + 1])
#   return sum_min

# def main():
#   nums = [1, 4, 3, 2]
#   print(group_integers_into_pairs(nums))

# if __name__ == "__main__":
#   main()




#Solution 2:
# def distribute_candies(candy_type):
#   hash = set()
#   for candy in candy_type:
#     hash.add(candy + 100000)
#   return min(len(candy_type) // 2, len(hash))

# candy_type = [1, 1, 2, 2, 3, 3]
# print(distribute_candies(candy_type))



#Solution 3: 
# def longest_harmonious_subsequence(nums):
#   counts = {}
#   for num in nums:
#     counts[num] = counts.get(num, 0) + 1

#   max_val = max(nums)
#   min_val = min(nums)
#   result = max_val - min_val + 1

#   for num in nums:
#     if num != min_val:
#       result = max(result, counts[num] + 1)
#   return result

# nums = [1, 3, 2, 2, 5, 2, 3, 7]
# print(longest_harmonious_subsequence(nums))


#Solution 4:
# def can_place_flowers(flowerbed, n):
#   result = False
#   for i in range(len(flowerbed)):
   
#     if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
#       flowerbed[i] = 1
#       n -= 1
#       if n == 0:
#         result = True
#         break
#   return result

# flowerbed = [0, 0, 1, 0, 0]
# n = 2
# print(can_place_flowers(flowerbed, n))



#Solution 5: 
# def max_product_of_three(nums):
#   result = nums[0] * nums[1] * nums[2]

#   for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#       for k in range(j + 1, len(nums)):
#         product = nums[i] * nums[j] * nums[k]
#         if product > result:
#           result = product
#   return result

# nums = [1, 2, 3]
# print(max_product_of_three(nums))


#Solution 6 :
# def binary_search(nums, target):
#   low = 0
#   high = len(nums) - 1

#   while low <= high:
#     mid = (low + high) // 2
#     if nums[mid] == target:
#       return mid
#     elif nums[mid] < target:
#       low = mid + 1
#     else:
#       high = mid - 1
#   return -1

# nums = [-1, 0, 3, 5, 9, 12]
# target = 9
# print(binary_search(nums, target))


# Solution 8: 
# def min_score(nums, k):

#   min_val = min(nums)
#   max_val = max(nums)
#   range_of_scores = max_val - min_val

#   if k > range_of_scores:
#     return 0
#   possible_scores = []
#   for i in range(len(nums)):
#     possible_scores.append(max(min_val + k, nums[i]) - min(max_val - k, nums[i]))
#   return min(possible_scores)

# nums = [1]
# k = 0
# print(min_score(nums, k))




