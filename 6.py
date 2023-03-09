import sys

if __name__ == "__main__":
    input_lines = [line.strip() for line in sys.stdin.readlines()]
    input_itr = iter(input_lines)

    work_hours = [ int(x) for x in next(input_itr).split()]
    print(f"Enter the number of hours worked on each day of the week: {work_hours}")


    total_hours = sum( work_hours )
    average = total_hours / len( work_hours )

    print(f"Average hours worked in a week: {average:.2f}")
