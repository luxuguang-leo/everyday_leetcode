#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #add from end of 2 strings, use carry to decide if need carry
        #check the last bit is it's '1' or not
        """
        M, N = len(a)-1, len(b)-1
        carry = 0
        ret = ""
        while M >= 0 or N >= 0:
            ch1 = ord(a[M])-ord('0') if M>=0 else 0
            ch2 = ord(b[N])-ord('0') if N>=0 else 0
            add = ch1 + ch2 + carry
            carry = add/2
            ret = str(add%2) + ret
            print(ch1, ch2, add, carry, ret)
            M -=1
            N -=1
        if carry == 1:
            ret = "1"+ret
        return ret
        """
        #recrsatively
        if not a:
            return b
        if not b:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1]) + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + '1'



        # @lc code=end

