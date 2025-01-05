class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums = len(nums)

        stack = nums.copy()
        while stack:
            if stack[0]<0:
                stack.pop(0)
            else:
                break

        if not stack:
            return max(nums)

        res = stack.pop(0)
        max_res = res
        while stack:
            # print("res:", res)
            # print("max_res:", max_res)
            cur = stack.pop(0)
            if cur>=0:
                res+=cur
            elif cur+res>=0:
                res = cur + res
            else: # cur+res<0
                res = 0

            if res>max_res:
                max_res = res

        return max_res
            

