student_name=input("Enter students name : ")
semester = int(input("Enter semester : "))
marks=float(input("Enter the marks : "))

print("Student name : ",student_name)
print("Semester : ",semester)
print("Marks : ",marks)

if marks>=90:
    print("Excellent")
elif marks>=75:
    print("very Good")
elif marks>=60:
    print ("Good")
elif marks>=40:
    print("Pass")
else: 
    print("Fail")

sum=0
for i in range(1,6):
    marks=int(input("Enter the marks of the subject : "))
    sum = sum+marks
    percentage =sum/5
print("Total marks:",sum)
print("Percentage:",percentage)

count=1
while count<=5:
    print(count)
    count+=1


file = open("notes.txt","w")
file.write("Welcome to ConceptOS!\n")
file.write("This is my first study note.")
file.close()

file = open("notes.txt","r")
content=file.read()
print(content)
file.close()

