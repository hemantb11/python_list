# -------------------- Linear Search --------------------

# Create List
x = [101, 57, 6, 98, 32, 57, 98]

# Display List
print(x)

# Take Key from User
ip = int(input("Enter your key to find: "))

# Flag Variable
flag = 0

# Search Element
for i in x:
    if ip == i:
        print("Key Found")
        flag = 1

# If Key Not Found
if flag == 0:
    print("Key Not Found")


# -------------------- Find Duplicate Elements --------------------

# Create List
x = [101, 57, 6, 98, 32, 57, 98]

# Display List
print(x)

print("Duplicate Keys:")

# Empty List to Store Printed Duplicates
y = []

# Find Duplicate Elements
for i in x:
    if x.count(i) > 1 and i not in y:
        print(i)
        y.append(i)


# -------------------- Print Unique Elements --------------------

# Create List
x = [101, 57, 6, 98, 32, 57, 98]

# Display List
print(x)

print("Unique Elements:")

# Print Elements Appearing Only Once
for i in x:
    if x.count(i) <= 1:
        print(i)
