class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        sum=[]
        for i in nums:
            count +=i
            sum.append(count)
        return sum