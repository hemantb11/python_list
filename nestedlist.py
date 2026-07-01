# x=[[10,20],[11.2,12.3]]
# print(x)
# print(x[1])
# print(x[1][1])


# -------------------- Student List --------------------

# List of Students (ID, Name, Marks)
student = [
    [101, "Ram", 98],
    [102, "Sita", 88],
    [103, "Ramu", 78],
    [104, "Gita", 99]
]

# Take Student Details from User
id = int(input("Enter Student ID: "))
name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

# Add New Student to List
student.append([id, name, marks])

# Display Student Name and Marks
for i in student:
    print(f"{i[1]} {i[2]}")




