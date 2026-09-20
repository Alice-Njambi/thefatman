students = ["Alice", "Brian", "Charlie", "Diana", "Ethan", "Fatima", "George", "Hannah", "Isaac", "Jane"]
marks = [78, 65, 92, 54, 88, 73, 61, 95, 47, 82]

# Total marks, number of students and  printing the total marks.

total_marks = sum(marks)
number_of_students = len(students)
print (f"\nNumber of students = {number_of_students}")
print (f"Total scores = {total_marks}")

# Average marks of the number of students.

average = float(total_marks/number_of_students)
print(f"Average Score = {average}")

# Finding the highest score.
high_score = max(marks)
print(f"\nHighest score = {high_score}")

#Finding the lowest score.
low_score = min(marks)
print(f"Lowest score = {low_score}")

# Printing every student next to their marks.
print(f"\nStudent names and scores : ")
for i in range(len(students)):
    print(f"{students[i]} : {marks[i]}")

print(f"\n")    

# Students with scores above 50%
above = 0

print(f"Students with above 50% score: ")
for i in range(len(students)):
    if marks[i] >= 50:
        print(f"{students[i]} : {marks[i]}")
        above += 1
print (f"Number of students above 50% = {above}\n")

# Students with below than 50%.
below = 0

print(f"\nStudents with below 50% score: ")
for i in range(len(students)):
    if marks[i] < 50:
        print(f"{students[i]} : {marks[i]}")
        below += 1

print(f"Number of students below 50% = {below}\n")

# Student with the top marks.
highest_score = max(marks)
for i in range(len(students)):
    if marks == highest_score:
        print(f"Student with highest score = {student[i]}, with score = {marks[i]}")
