def validate_antakshri(first_player_line, second_player_line):
    first_player_last_word = first_player_line.split()[-1].lower()
    second_player_first_word = second_player_line.split()[0].lower()
    
    if first_player_last_word == second_player_first_word:
        return "Pass"
    else:
        return "Stop"

# Test with given lines of songs
first_player_line = "One two three"
second_player_line = "Three four five"
result = validate_antakshri(first_player_line, second_player_line)
print(result)

first_player_line = "One two"
second_player_line = "Three four five"
result = validate_antakshri(first_player_line, second_player_line)
print(result)
