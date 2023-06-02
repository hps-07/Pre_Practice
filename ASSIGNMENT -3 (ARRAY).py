
#Solution 1 :
# def find_closest_triplet(nums, target):
#   min_diff = float("inf")
#   closest_triplet = None

#   for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#       for k in range(j + 1, len(nums)):
#         diff = abs(target - (nums[i] + nums[j] + nums[k]))
#         if diff < min_diff:
#           min_diff = diff
#           closest_triplet = nums[i], nums[j], nums[k]
#   return sum(closest_triplet)

# def main():
#   nums = [-1, 2, 1, -4]
#   target = 1
#   print(find_closest_triplet(nums, target))

# if __name__ == "__main__":
#   main()




#Solution 2 :
# def find_quadruplets(nums, target):
#   quadruplets = []

#   for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#       for k in range(j + 1, len(nums)):
#         for l in range(k + 1, len(nums)):
#           if nums[i] + nums[j] + nums[k] + nums[l] == target:
#             quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
#   return quadruplets

# def main():
#   nums = [1, 0, -1, 0, -2, 2]
#   target = 0
#   quadruplets = find_quadruplets(nums, target)
#   print(quadruplets)

# if __name__ == "__main__":
#   main()


#Solution 4 :
# def find_index(nums, target):
#   start = 0
#   end = len(nums) - 1

#   while start <= end:
#     mid = (start + end) // 2

#     if nums[mid] == target:
#       return mid
#     elif nums[mid] < target:
#       start = mid + 1
#     else:
#       end = mid - 1
#   return start

# def main():
#   nums = [1, 3, 5, 6]
#   target = 5
#   index = find_index(nums, target)
#   print(f"The index of target value {target} is {index}")

# if __name__ == "__main__":
#   main()


#Solution 5 :
# def increment_digits(digits):
#   carry = 1
#   for i in range(len(digits) - 1, -1, -1):
#     digits[i] += carry
#     carry = digits[i] // 10
#     digits[i] %= 10

#   if carry > 0:
#     digits.insert(0, carry)
#   return digits


# def main():
#   digits = [1, 2, 3]
#   incremented_digits = increment_digits(digits)
#   print(f"The incremented digits are {incremented_digits}")


# if __name__ == "__main__":
#   main()

#Solution 6 :
# def find_single_number(nums):
#   result = 0
#   for num in nums:
#     result ^= num
#   return result

# def main():
#   nums = [2, 2, 1]
#   single_number = find_single_number(nums)
#   print(f"The single number is {single_number}")

# if __name__ == "__main__":
#   main()


#Solution 8 :
# def can_attend_all_meetings(intervals):
#   intervals.sort()

#   for i in range(1, len(intervals)):
#     if intervals[i][0] < intervals[i - 1][1]:
#       return False
#   return True

# def main():
#   intervals = [[0, 30], [5, 10], [15, 20]]
#   can_attend = can_attend_all_meetings(intervals)
#   print(f"Can attend all meetings? {can_attend}")

# if __name__ == "__main__":
#   main()

