class Solution:
    def firstUniqChar(self, s: str) -> int:
        st = set()
        for idx in range(len(s)):
            if s[idx] in st:
                st.remove(s[idx])
                st.add(s[idx])
                continue
            st.add(s[idx])
        l = list(st)
        print(l)
        return ret
