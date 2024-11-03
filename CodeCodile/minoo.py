from functools import reduce
from operator import mul


def productExceptSelf(nums):
        result = []
        for i in range(0, len(nums)):
            arr = nums
            arr.remove(nums[i])
            result.append(reduce(mul, arr))

        return result


print(productExceptSelf([1,2,3,4]))

# arr = [1,2,3,4]
# res = reduce(mul, arr)
# print(res)
