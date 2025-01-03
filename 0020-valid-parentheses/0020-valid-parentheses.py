class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in "([{":
                st.append(i)
            else:
                if not st or \
                i==")" and st[-1]!="(" or \
                i=="]" and st[-1]!="[" or \
                i=="}" and st[-1]!="{":
                    return False
                else:
                    st.pop()
        return not st