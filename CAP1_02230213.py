# Jasma Tamang
# BE.Instrumentation and Control Engineering
# 02230213
###############################
# References
# How to handle file
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://www.w3schools.com/python/python_file_open.asp
#
# Defining a function
# https://www.geeksforgeeks.org/python-functions/
#
###############################
# Solution
# Solution score:
# 49483
##############################


def read_input(filename):
    # Open the file specified by the filename for reading
    with open(filename, 'r') as file:
        # Read all lines from the file into a list
        lines = file.readlines()

        # Extract rounds data as tuples from each line
        # Each line contains opponent's move and result separated by whitespace
        # Split each line into two parts and form a tuple (opponent_move, result)
        rounds = [(line.split()[0], line.split()[1]) for line in lines]

        # Return the list of tuples representing rounds
        return rounds

def read_input(inputfile):
    # Open the file specified by the filename for reading
    with open(inputfile, 'r') as file:
        # Read all lines from the file into a list
        lines = file.readlines()

        # Extract rounds data as tuples from each line
        # Each line contains opponent's move and result separated by whitespace
        # Split each line into two parts and form a tuple (opponent_move, result)
        rounds = [(line.split()[0], line.split()[1]) for line in lines]

        # Return the list of tuples representing rounds
        return rounds

def calculate_score(rounds):
    # Dictionary to store the values corresponding to each move
    # 'A' represents Rock, 'B' represents Paper, and 'C' represents Scissors
    move_points = {'A': 1, 'B': 2, 'C': 3}
    # Dictionary to store the scores corresponding to each round result
    # 'X' represents losing, 'Y' represents drawing, and 'Z' represents winning
    round_points = {'X': 0, 'Y': 3, 'Z': 6}
    # Initialize the total score to 0
    total_score = 0

    # Iterate through each round data (opponent's move and result)
    for opponent_move, result in rounds:
        # Check if the opponent's move and result are valid
        if opponent_move not in move_points or result not in round_points:
            # Print an error message if the data is invalid
            print(f"Invalid input: {opponent_move} {result}")
            # Move to the next round if the data is invalid
            continue

        # Determine your move based on the opponent's move and result
        # Using a dictionary lookup to map opponent's move and result to your move
        players_move = {'AX': 'C', 'AY': 'A', 'AZ': 'B',
                        'BX': 'A', 'BY': 'B', 'BZ': 'C',
                        'CX': 'B', 'CY': 'C', 'CZ': 'A'}.get(opponent_move + result, '')
        # Check if the calculated move is valid
        if players_move:
            # Calculate the total score for the current round
            # Add the value of your move and the score of the round result
            total_score += move_points[players_move] + round_points[result]
        else:
            # Printing an error message if the move combination is invalid
            print('Invalid move combination')
    # Returning the total score after iterating through all rounds
    return total_score

def main():
    # Specify the input file name
    inputfile = 'input_3_cap1.txt'
    # Reading rounds data from the input file
    rounds = read_input(inputfile)
    # Checking if there are valid rounds data
    if not rounds:
        # Print a message if there are no valid data to calculate the score
        print("No valid data to calculate the score.")
        # Exit the program
        return
    # Calculate the total score based on rounds data
    total_score = calculate_score(rounds)
    # Print the calculated total score
    print(f"The total score is: {total_score}")

if __name__ == "__main__":
    # Call the main function to start the program
    main()
