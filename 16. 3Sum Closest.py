class Solution(object):
    def threeSumClosest(self, nums, tar):
        nums.sort()
        c=float('inf')              #closest
        n=len(nums)

        for i in range(n - 2):
            l=i + 1                 #left
            r=n - 1                 #right

            while l<r:
                total = nums[i] + nums[l] + nums[r]

                if abs(total-tar) < abs(c-tar):
                    c=total

                if total<tar:
                    l+=1
                elif total>tar:
                    r-=1
                else:
                    return total  

        return c
