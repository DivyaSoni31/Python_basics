roll_no = int(input("roll no: "))
name = input("name of the student: ")
physics = int(input("enter the no. subject: "))
chemistry = int(input("enter the no. subject: "))
comp_app = int(input("enter the no. subject: "))
print("_"*20)
print(f"Name of the student: {name}\nMarks in physics: {physics}\nMarks in Chemistry: {chemistry}\nMarks in comp_app: {comp_app} ")

total_marks = physics + chemistry + comp_app
print("Total marks: ",total_marks)
percentage = (total_marks / 300) * 100
print("percentage: ",percentage)

if percentage >= 60:
    d = "First"
elif percentage >= 50:
    d = "Second" 
elif percentage >= 40:
    d = "Third"
else:
    d = "fail"
print(f"division = {d}")