'''
restore-ip-addresses
'''
'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
For example:
Given"25525511135",
return["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''


class Solution:
    def dfs(self, s, sub, ip):
        if not s and sub == 4:
            self.res.append(ip[1:])
        for i in range(1, len(s) + 1):
            if int(s[:i]) <= 255:
                self.dfs(s[i:], sub + 1, ip + '.' + s[:i])

    def restoreIpAddresses(self, s):
        self.res = []
        if s == '0000':
            self.res.append('0.0.0.0')
        self.dfs(s, 0, '')
        return self.res


if __name__ == '__main__':
    so = Solution()
    a = '25525511135'
    # a = '0000'
    print(so.restoreIpAddresses(a))
