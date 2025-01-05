class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp=list(s)
        for shift in shifts:
            if shift[2] == 0:
                for i in range(shift[0],shift[1]+1):
                    if temp[i] == "a":
                        temp[i]= "z"
                    else:
                        temp[i]=chr(ord(temp[i])-1)
            if shift[2] == 1:
                for i in range(shift[0],shift[1]+1):
                    if temp[i] == "z":
                        temp[i]="a"
                    else:
                        temp[i]=chr(ord(temp[i])+1)
        return "".join(temp)
