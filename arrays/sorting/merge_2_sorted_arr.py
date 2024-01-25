# 1 3 3 5 5  7 9 
# 2 4 6  # input


nums1 = list(map(int,input().split())) 
nums2 = list(map(int,input().split())) 
# n = len(nums)
m = len(nums1)
n = len(nums2)
t = m + n 
nums3 = [0] * t 

i = 0 
j = 0 
k = 0 
while(i<m and j < n):
    e1 = nums1[i]
    e2 = nums2[j]
    if(e1<=e2): # checking for equality to handle duplicates
        nums3[k] = e1
        i = i+ 1 
    elif(e1>=e2):
        nums3[k] = e2
        j = j + 1 
    k = k + 1

while(i<m):
    nums3[k] = nums1[i]
    i = i + 1
    k = k + 1
    
    
while(j<n):
    nums3[k] = nums2[j]
    j = j+ 1
    k = k+1
    

print(nums3)