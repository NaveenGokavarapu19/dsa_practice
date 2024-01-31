def is_prime(n):
    limit = int(math.sqrt(n))
    for i in range(2,limit+1):
        if(n%i==0):
            return False
    return True


class Solution:
    def countPrimes(self, n: int) -> int:
        prime_sum = 0
        if n==0 or  n==1 or n==2:
            return 0

        
        for i in range(2,n):
            flag = is_prime(i)
            if(flag):
                prime_sum = prime_sum + 1
        return prime_sum