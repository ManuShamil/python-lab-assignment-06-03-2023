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

