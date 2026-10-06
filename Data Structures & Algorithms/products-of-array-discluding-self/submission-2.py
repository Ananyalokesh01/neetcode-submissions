class Solution:
    def productExceptSelf(self, nums):
        prod = 1
        zero = 0

        for num in nums:
            if num == 0:
                zero += 1
            else:
                prod *= num

        result = []

        for num in nums:
            if zero > 1:
                result.append(0)
            elif zero == 1:
                if num == 0:
                    result.append(prod)
                else:
                    result.append(0)
            else:
                result.append(prod // num)

        return result
        