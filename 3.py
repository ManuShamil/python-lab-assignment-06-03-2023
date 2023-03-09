# Question 3
# A man engaged 'n' labourers to make ’t’ toys in ’d’ days. Assume that all men work with same speed and efficiency. 
# After 'd1' days, he found that only 't1' toys were made. Design an algorithm and write a Python code to determine the number of additional men to be employed 
# to complete the task in time. For example, if n is 10, t is 320, d is 5, d1 is 3, and t1 is 120 then the number of additional men to be employed is 12. 
# Assume that the speed of making toys is uniform for all men.

# Input Format:
# Read the number of labourers engaged in work
# Read the total number of toys to be made (t)
# Read the total number of days allotted for completion (d)
# Read the number of days work had been done (d1)
# Read the number of toys made in d1 days (t1)

# Output Format:
# Number of more men required for completing the job in allotted period
    
import sys

if __name__ == "__main__":
    input_lines = [line.strip() for line in sys.stdin.readlines()]
    input_itr = iter(input_lines)

    inp_array = [int(x) for x in next(input_itr).split()]

    labourers = inp_array[0]
    toys_to_be_made = inp_array[1]
    allocated_days = inp_array[2]
    completed_days = inp_array[3]
    toys_made = inp_array[4]

    print(f"Enter number of labourers already engaged in work: {labourers}")
    print(f"Enter the total number of toys to be made: {toys_to_be_made}")
    print(f"Enter the total number of days allocated for the work: {allocated_days}")
    print(f"Enter the number of days already completed: {completed_days}")
    print(f"Enter the number of toys already made: {toys_made}")

    toys_per_day = toys_made / completed_days
    toys_per_person = toys_per_day / labourers
    remaining_toys = toys_to_be_made - toys_made
    remaining_days = allocated_days - completed_days

    required_labourers = remaining_toys / (toys_per_person * remaining_days)
    additional_labourers = required_labourers - labourers

    print(f"Additional labourers required: {additional_labourers}")



