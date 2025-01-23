from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        students=deque(students)
        sandwiches=deque(sandwiches)
        while len(students) != 0:

            if students[0] == sandwiches[0]:
 
                students.popleft()
                sandwiches.popleft()
                count = 0
            else:           
                count += 1
                students.append(students.popleft())
       
            if count == len(students):
                return count

        return 0