"""
Objective: You are given a nested list (a list of lists) where each inner list represents the grades a student received for their assignments throughout a semester. Your task is to use a list comprehension to identify students who have improved over the semester. An improvement is defined as having a higher grade on the last assignment compared to their average grade for the entire semester (excluding the last assignment).

grades = [
    [85, 90, 88, 78, 85],
    [72, 88, 85, 82, 87],
    [90, 90, 85, 80, 85],
    [78, 75, 80, 85, 90]
]

Each inner list contains the grades of a single student over five assignments. The last grade in each inner list is for the final assignment.

Expected Output:

For the given grades list, the expected output is [1, 3] since:

- Student at index 1 (2nd student) has an average grade of
(72 + 88 + 85 + 82) / 4 = 81.75
for the first four assignments and scored 87 on the last assignment.

- Student at index 3 (4th student) has an average grade of 
(78 + 75 + 80 + 85) / 4 = 79.5 for the first four assignments and scored 90 on the last assignment.
"""

grades = [
    [85, 90, 88, 78, 85],
    [72, 88, 85, 82, 87],
    [90, 90, 85, 80, 85],
    [78, 75, 80, 85, 90]
]
