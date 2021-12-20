# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if n==1:
            return True
        q, r = divmod(n, 2)
        if r == 0:
            return self.isUgly(q)
        else:
            q, r = divmod(n, 3)
            if r == 0:
                return self.isUgly(q)
            else:
                q, r = divmod(n, 5)
                if r==0:
                    return self.isUgly(q)
                else:
                    return False

n=20
solution=Solution()
print(solution.isUgly(n))