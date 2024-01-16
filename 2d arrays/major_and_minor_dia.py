nums = [[1,2,3],[4,5,6],[7,8,9]]

#  1 2 3 
#  4 5 6
#  7 8 9

n = len(nums)


for row in range(len(nums)):
    current_row = row
    major_diagonal_elment = nums[row][row]
    minor_diagonal_element = nums[row][n-current_row-1]
    # print(minor_diagonal_element)
    print(major_diagonal_elment) 
    print(minor_diagonal_element)