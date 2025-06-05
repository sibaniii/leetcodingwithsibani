class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Step 1: Sort the array
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first number

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1  # Move right to increase sum
                elif total > 0:
                    right -= 1  # Move left to decrease sum
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for second and third numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


        
