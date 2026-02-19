# Program Name: Assignment2.py
# Course: IT3883 / Section 01
# Student Name: Jaleelah Bachou
# Assignment Number: Assignment 2
# Due Date: 02/08/2026
# Purpose: This program reads a file containing student names and six scores,
# calculates each student's average, and prints the results in descending order
# based on the final average.
# Resources: Class notes and personal practice with Python file handling.

file_name = "input.txt"
students = []

# open the file and read each line
with open(file_name, "r") as file:
    for line in file:
        # remove extra spaces and split the line
        parts = line.strip().split()
      
        name = parts[0]

        # remaining parts are the score
        scores = []
        for score in parts[1:]:
            scores.append(int(score))

        # calculate the average score
        total = sum(scores)
        average = total / len(scores)

        # store the result as a tuple
        students.append((name, average))

# sort students by average in descending order
students.sort(key=lambda item: item[1], reverse=True)

# print results 
for student in students:
    print(student[0], format(student[1], ".2f"))
