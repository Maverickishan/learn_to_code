n = int(input())
student_marks = {}
for _ in range(n):
      name, *line = input().split()
      scores = list(map(float, line))
      student_marks[name]=scores
      
query_name = input()
list1=[]
if query_name in student_marks:
      list1.append(student_marks[query_name])
else:
      print( f"{query_name} is not a student" )

z=sum(list1[0])

print(format(z/3,"2.f"))


