# Solution 1:

# def threearrays(arr1, arr2, arr3):
#   result = []
#   for i in range(len(arr1)):
#      if arr1[i] in arr2 and arr1[i] in arr3:
#        result.append(arr1[i])
#   return sorted(result)

# arr1 = [1, 2, 3, 4, 5]
# arr2 = [1, 2, 5, 7, 9]
# arr3 = [1, 3, 4, 5, 8]
# print(threearrays(arr1, arr2, arr3))


# Solution 2:

# def unique_arrays(nums1, nums2):
#   nums1_set = set(nums1)
#   nums2_set = set(nums2)
  
#   intersection_set = nums1_set & nums2_set
#   difference_set1 = nums1_set - intersection_set
#   difference_set2 = nums2_set - intersection_set
#   return [list(difference_set1), list(difference_set2)]

# nums1 = [1, 2, 3]
# nums2 = [2, 4, 6]
# print(unique_arrays(nums1, nums2))

# Solution 3: 

# def return_transpose(matrix):

#   num_rows = len(matrix)
#   num_cols = len(matrix[0])
#   transpose = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

#   for row_idx in range(num_rows):
#     for col_idx in range(num_cols):
#       transpose[col_idx][row_idx] = matrix[row_idx][col_idx]

#   return transpose
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transposed_matrix = return_transpose(matrix)
# print(transposed_matrix)



# Solution 4: 

# def maximized_sum(nums):
#    nums.sort()
#    sum_of_min = 0
#    for i in range(0, len(nums), 2):
#        sum_of_min += min(nums[i], nums[i + 1])
#    return sum_of_min

# nums = [1, 4, 3, 2]
# max_sum = maximized_sum(nums)
# print(max_sum)


#Solution 6:

# def square_of_sorted_array(nums):
#   squares = []
#   for num in nums:
#     squares.append(num ** 2)
#   squares.sort()
#   return squares

# nums = [-4, -1, 0, 3, 10]
# squares = square_of_sorted_array(nums)
# print(squares)



