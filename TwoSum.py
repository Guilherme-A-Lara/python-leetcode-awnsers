'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
class Solution(object):
    def twoSum(self, nums = [2,7,11,15] , target = 9):
        look_for = {}
        for i,x in enumerate(nums,0):
            try:
                return look_for[x] , i
            except: 
                look_for.setdefault(target - x,i)
                
                
'''
Your input [2,7,11,15]
9
Output
[0,1]
Expected
[0,1]
 '''
