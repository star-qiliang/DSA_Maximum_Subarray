class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        i = 0
        j = 0
        res_list = []        
        while nums[i]<=0:
            i+=1
        res = nums[i]

        while True:
            if i+1>=len_nums:
                break
            if j+1>=len_nums:
                break

            if nums[j]>=0:
                res = res + nums[j]
                j+=1

            elif res + nums[j]<0:
                res_list.append((i, j, res))
                i = j+2
                j = i
                if i>=len_nums:
                    break
                res = nums[i]
            else:
                res = res + nums[j]
                j+=1


        print("j:", j)

        print("res_list:", res_list)

        return 0

            

            

