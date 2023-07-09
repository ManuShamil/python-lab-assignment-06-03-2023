def check_antakshari(first_player_line, second_player_line):
    # Extract the last word sung by the first player
    first_player_last_word = first_player_line.split()[0].lower()

    # Extract the first word sung by the second player
    second_player_first_word = second_player_line.split()[0].lower()

    if first_player_last_word == second_player_first_word:
        return "Pass"
    else:
        return "Stop"

# Accept the lines sung by the players as input
first_player_line = input()
second_player_line = input()

# Check if the second player follows the rules
result = check_antakshari(first_player_line, second_player_line)

# Print the result
print(result)
