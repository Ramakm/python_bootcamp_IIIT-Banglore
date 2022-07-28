# Instructions:

# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, 
# you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.
#  The final version of the student_grades dictionary will be checked.
# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for k in student_scores.keys():

  if student_scores[k]>90 and student_scores[k]<=100:
    student_scores[k] = "Outstanding"
    student_grades[k]=student_scores[k] 

  elif student_scores[k]>80 and student_scores[k]<=90:
    student_scores[k] = "Exceeds Expectations"
    student_grades[k]=student_scores[k] 
  elif student_scores[k]>70 and student_scores[k]<=80:
    student_scores[k] = "Acceptable"
    student_grades[k]=student_scores[k] 
  else:
    student_scores[k] = "Fail"
    student_grades[k]=student_scores[k] 

print(student_grades)