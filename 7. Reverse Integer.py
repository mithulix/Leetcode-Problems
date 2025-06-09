class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0
        neg = x < 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if res > (INT_MAX - digit) // 10:
                return 0

            res = res * 10 + digit

        return -res if neg else res
