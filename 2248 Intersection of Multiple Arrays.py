class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        numbers = {}
        for i in nums:
            for j in i:
                if j in numbers.keys():
                    numbers[j] += 1
                else:
                    numbers[j] = 1
        output = []
        for i in numbers:
            if numbers[i]== len(nums):
                output.append(i)
        output.sort()
        return(output)