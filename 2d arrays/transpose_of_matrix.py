nums = [[1,2,3],[4,5,6],[7,8,9]]

#  1 2 3 
#  4 5 6
#  7 8 9


#  1 4 7 
#  2 5 8
#  3 6 9

n = len(nums)

count = 0 
for row in range(len(nums)):
    j = 0
    while j<row:
        current_row = row 
        current_column = j 
        temp = nums[current_row][current_column]
        nums[current_row][current_column] =  nums[current_column][current_row]
        nums[current_column][current_row] = temp
        j = j + 1
        

print(nums)