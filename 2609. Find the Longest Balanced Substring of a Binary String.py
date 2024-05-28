class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        rv = 0
        zcount = 0
        ocount = 0
        for i in s:
            if i == '0' and ocount == 0:
                zcount += 1
            elif i == '0' and ocount > 0:
                rv = max(rv, ocount)
                zcount = 1
                ocount = 0
            elif i == '1' and zcount == 0:
                zcount = 0
                ocount = 0
            elif i == '1' and zcount > 0 and zcount > ocount:
                ocount += 1
            else:
                rv = max(rv, zcount)
                zcount = 0
                ocount = 0
        return 2*max(rv,ocount)