import sys

def additional_men(n_labourers, t_toys, d_days, after_d1_days, t1_toys_made):
    # In 3 days 10 persons made 120 toys # 120/3=40
    # In after_d1_days, n_labourers made t1_toys_made

    # 120 / 3 = 40
    per_day_toys_made = t1_toys_made / after_d1_days

    # each person made 40/4 = 4 toys
    each_person_made = per_day_toys_made / n_labourers

    # 320 - 120 = 200
    remaining_toys = t_toys - t1_toys_made

    # 5-3 = 2
    remaining_days = d_days - after_d1_days

    # to made 200 toys in 2 days we require --200/(4*2)=25
    total_labourer_require = remaining_toys / (each_person_made * remaining_days)

    more_labourer_require = total_labourer_require - n_labourers

    return more_labourer_require



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



