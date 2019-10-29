class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        while n > 1:
            a = n % 2
            if a == 1:
                return False
            if a == 0:
                n = n // 2
        return True
