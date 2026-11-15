def calculate_average(mark1,mark2,mark3):
    total = mark1+mark2+mark3
    average=total/3
    return average

student_name = "Rohita"

average_marks = calculate_average(90,89,98)

print("Student Name : ",student_name)
print("Average Marks :",round(average_marks,2))

def check_result(marks):
    if marks>=40:
        return "Pass"
    else:
        return "Fail"

result = check_result(35)
print("result : ",result)