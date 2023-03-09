# Question 6
# A company wants its employees to work for 'X' hours on average per day in a week (Monday to Friday).  
# Given the number of hours worked by an employee on each day of a week, design a flowchart and write a Python code to compute the average number of hours 
# worked by the employee. Number of hours worked can be floating point values. For example, 7 hours 30 minutes is entered as 7.5 hours
# Input Format:
# Number of hours worked on first day
# Number of hours worked on second day
# Number of hours worked on third day
# Number of hours worked on fourth day
# Number of hours worked on fifth day
# Output Format:
# Average hours worked in a week

import sys

if __name__ == "__main__":
    input_lines = [line.strip() for line in sys.stdin.readlines()]
    input_itr = iter(input_lines)

    work_hours = [ int(x) for x in next(input_itr).split()]
    print(f"Enter the number of hours worked on each day of the week: {work_hours}")


    total_hours = sum( work_hours )
    average = total_hours / len( work_hours )

    print(f"Average hours worked in a week: {average:.2f}")
