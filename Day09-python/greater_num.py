class Solution:
    def greatestOfThree(self, a, b, c):
        if a>b and a>c:
            return a
        elif b>a and b>c:
            return b
        else:
            return c
obj=Solution()
print(obj.greatestOfThree(2,5,-6))