import math

#User function Template for python3
class Solution:
    def armstrongNumber (self, n):
        org = n 
        sum1 = 0
        while(n!=0):
            digit = n % 10 
            sum1 = sum1 + int(math.pow(digit,3))
            n = n//10 
        if(sum1 == org):
            return "Yes"
        else:
            return "No"