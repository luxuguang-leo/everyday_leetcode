#
# @lc app=leetcode id=273 lang=python
#
# [273] Integer to English Words
#

# @lc code=start
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        #三个一组来处理，最多处理四组，每组需要判断后两位是否小于20，因为20以内的数需要查表
        #大于20小于99就取出十位和个位来组成就行
        lessThan20 = ["","One","Two","Three","Four","Five",
        "Six","Seven","Eight","Nine","Ten","Eleven","Twelve",
        "Thirteen","Fourteen","Fifteen","Sixteen","Seventeen",
        "Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty",
        "Fifty","Sixty","Seventy","Eighty","Ninety"]
        thousands = ["","Thousand","Million","Billion"]
        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return lessThan20[num] + " "
            elif num < 100:
                return tens[num/10]+" "+ helper(num%10)
            else:
                return lessThan20[num/100]+ " Hundred " + helper(num%100) 
        if num == 0:
            return "Zero"
        ret = ""    
        for i in range(len(thousands)):
            if num % 1000 != 0:#将100之内的数调用helper函数来处理
                ret = helper(num%1000) + thousands[i] + " " + ret
            num /= 1000
        return ret.strip()

            
        
# @lc code=end

