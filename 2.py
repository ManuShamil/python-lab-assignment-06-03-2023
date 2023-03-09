import sys 

class Appreciatation:

    appreciation = "No Appreciation"

    grade = 0
    attendence = 0
    sports = 0

    def __init__(self, grade: int, attendence: int, sports: int ) -> None:
        self.grade = grade
        self.attendence = attendence
        self.sports = sports

            # Check appreciation level based on input parameters
        if self.grade >= 3 and self.attendence >= 90 and self.sports >= 2:
            self.appreciation = "Excellent"
        elif self.grade >= 3 and self.sports >= 2:
            self.appreciation = "Very Good"
        elif self.grade >= 3 and self.sports >= 90:
            self.appreciation = "Good"
        else:
            self.appreciation = "No Appreciation"



if __name__ == "__main__":
    input_lines = [line.strip() for line in sys.stdin.readlines()]
    input_itr = iter(input_lines)

    print("Enter student grades: ", end='')
    results = [int(x) for x in next(input_itr).split()]

    grades = results[0]
    attendence = results[1]
    sports = results[2]

    print(f"{grades} {attendence} {sports}")

    appreciation = Appreciatation( grades, attendence, sports)
    print( appreciation.appreciation )