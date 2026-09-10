from functools import cache

class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        def check(n):
            if n == 0:
                return '0'
            res = ''
            while n:
                n, m = divmod(n, b)
                res = str(m) + res
            return res

        s1, s2 = check(int(l) - 1), check(int(r))
        mod = 10 ** 9 + 7

        @cache
        def f(i, pre, is_limit, is_num, s):
            if i == len(s):
                return int(is_num)
            
            res = 0
            if not is_num:
                # If we haven't started placing numbers, we can skip the current position
                res = f(i + 1, pre, False, False, s)
                
            low = 0 if is_num else 1
            high = int(s[i]) if is_limit else b - 1
            
            for d in range(low, high + 1):
                if d >= pre:
                    res += f(i + 1, d, is_limit and d == high, True, s)
                    
            return res % mod

        # Reset cache between calls to avoid cross-contamination of different strings
        ans2 = f(0, -1, True, False, s2)
        f.cache_clear()
        ans1 = f(0, -1, True, False, s1)
        
        return (ans2 - ans1) % mod