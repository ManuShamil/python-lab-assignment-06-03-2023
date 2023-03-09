# Question 5
# VIT follows relative grading based on the class average to grade the performance of students in various examinations. 
# Write a program that accepts the marks secured by a student for a given subject along with the average marks of the respective class. 
# Then display the grade he has secured, based on the following instructions.
#     a) Grading is done based on the deviation from class average. 
#     b) If the deviation from class average of the student’s mark is greater than or equal to 20, the student has scored S grade
#     c) If the deviation from class average of the student’s mark is greater than or equal to 10, the student has scored A grade
#     d) If the deviation from class average of the student’s mark is within the range of -5 to + 5, the student has scored B grade
#     e) If the deviation from class average of the student’s mark is less than or equal to 10, the student has scored C grade
#     f) If the deviation from class average of the student’s mark is less than or equal to 15, the student has scored D grade
#     g) If the deviation from class average of the student’s mark is less than 20, the student has scored F grade

import sys

class GradeCalculator:
    def __init__(self, marks, average) -> None:
        self.student_marks = marks
        self.class_average = average
    
    def calculate( self ):
        
        deviation = self.student_marks - self.class_average
        if deviation >= 20:
            return 'S'
        elif deviation >= 10:
            return 'A'
        elif -5 <= deviation <= 5:
            return 'B'
        elif deviation <= 10:
            return 'C'
        elif deviation <= 15:
            return 'D'
        else:
            return 'F'

if __name__ == "__main__":
    input_lines = [line.strip() for line in sys.stdin.readlines()]
    input_itr = iter(input_lines)

    student_marks = int(next(input_itr))
    print(f"Enter the student marks: {student_marks}")

    class_average = int(next(input_itr))
    print(f"Enter the class average: {class_average}")

    grade_calculator = GradeCalculator(student_marks, class_average)
    grade = grade_calculator.calculate()
    print("The grade secured by the student is:", grade)

