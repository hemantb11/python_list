# -------------------- List Basics --------------------

# Creating List
x = [10, 20, 30]

# Display Complete List
print(x)

# Access Elements using Index
print(x[1])
print(x[2])

# Update Element
x[2] = 300
print(x[2])

# Traverse List using for loop
for items in x:
    print(items)


# -------------------- User Input --------------------

# Empty List
x = []
print(x)

# Add Elements using User Input
for i in range(5):
    ip = input(f"Enter {i+1} Element: ")
    x.append(ip)

# Display Updated List
print(x)


# -------------------- extend() Method --------------------

# Create List
x = [1, 2]
print(x)

# Add Multiple Elements
x.extend([3, 4])
print(x)


# -------------------- insert() Method --------------------

# Create List
x = [11, 13]

# Insert Element at Specific Index
x.insert(1, 12)
print(x)


# -------------------- remove(), pop(), clear() --------------------

# Create List
x = [10, 8, 9, "hii", 90, 89]

# Remove Element by Value
x.remove("hii")

# Remove Element by Index
x.pop(4)

print(x)

# Remove All Elements from List
x.clear()
print(x)


# -------------------- List Methods --------------------

# Create List
x = [10, 20, 40, 60, 10, 30]

# Count Occurrence of Element
print(x.count(10))

# Find Index of Element
print(x.index(30))

# Sort List in Ascending Order
x.sort()
print(x)

# Reverse List
x.reverse()
print(x)

# Copy List
y = x.copy()
print(y)


# -------------------- List Functions --------------------

# Create List
x = [78, 90, 12, 8]

# Built-in Functions
print(len(x))                     # Length of List
print(max(x))                     # Maximum Value
print(min(x))                     # Minimum Value
print(sum(x))                     # Sum of Elements
print(sorted(x, reverse=True))    # Sort in Descending Order


# -------------------- Count Elements Manually --------------------

# Create List
x = [10, 20, 45, 30]

# Count Total Elements
count = 0
for i in x:
    count += 1

print(count)


# -------------------- Find Maximum Manually --------------------

# Find Maximum Element
max = 0

for i in x:
    if i >= max:
        max = i

print(max)


# -------------------- Print Only IDs --------------------

# Mixed List
stud = [1, "ram", 2, "sita", 3, "pooja"]

print(stud)

# Print Elements at Even Index
for i in range(len(stud)):
    if i % 2 == 0:
        print(stud[i])


# -------------------- Student Record --------------------

# Student Data (ID, Name, Marks)
stud = [1, "ram", 45, 2, "sita", 78, 3, "pooja", 90]

# Display Student Details
for i in range(0, len(stud), 3):
    print("ID:", stud[i])
    print("Name:", stud[i+1])
    print("Marks:", stud[i+2])
    print()
