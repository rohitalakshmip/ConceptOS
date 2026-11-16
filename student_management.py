# get students info
student_name=input("Enter students name : ")

# get marks 3 subject
#total marks
total = 0
for i in range(1,4):
    marks = int(input("Enter the marks of " + str(i) + " subject : "))
    total = total+marks

print("Total marks : ",total)

# average marks
avg = total/3
print("Average marks : ",avg)

#check result
if avg>=40:
    result = "Pass"
else:
    result = "Fail"

print("Student name : ",student_name)
print("Total marks : ",total)
print("Average marks : ",avg)
print("Result : ", result)

file = open("student_profile.txt","w")
file.write("Student name : "+student_name+"\n")
file.write("Total marks : "+str(total)+"\n")
file.write("Average marks : "+str(avg)+"\n")
file.write("Result : "+result+"\n")
file.close()
"""
use  

with open("student_profile.txt", "w") as file:
    file.write("Student name : " + student_name + "\n")
    file.write("Total marks : " + str(total) + "\n")
    file.write("Average marks : " + str(round(avg, 2)) + "\n")
    file.write("Result : " + result + "\n")
"""

