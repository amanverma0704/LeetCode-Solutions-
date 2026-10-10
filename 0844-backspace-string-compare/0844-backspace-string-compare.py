class Solution(object):
    def backspaceCompare(self, s, t):
        st1 = []
        st2 = []
        for i in range(len(s)):
            if s[i] != '#':
                st1.append(s[i])
            else:
                if st1:
                    st1.pop()
        for j in range(len(t)):
            if t[j] != '#':
                st2.append(t[j])
            else:
                if st2:
                    st2.pop()
        if st1 != st2:
            return False
        else:
            return True

        