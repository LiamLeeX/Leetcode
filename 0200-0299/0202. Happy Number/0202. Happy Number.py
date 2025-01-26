class Solution:
    def get_next(self, num):
        total = 0
        while num > 0:
            num, digit = divmod(num, 10)
            total += digit * digit
        return total

    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
            if fast == 1 or slow == fast:
                return fast == 1


so = Solution()
so.isHappy(19)
