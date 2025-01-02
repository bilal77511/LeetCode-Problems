class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s)<numRows:
            return s
        count=0
        sw= False
        a=[""]*numRows
        for i in s:
            a[count]=a[count]+i
            if count == 0 or count == numRows-1:
                sw = not sw
            if sw:
                count+= 1
            else:
                count-=1
        return "".join(a)