# First column
# A = Rock
# B = Paper
# C = Scissors

# Second column
# X = Rock
# Y = Paper
# Z = Scissors

# Scores: 1 = Rock, 2 = Paper, 3 = Scissors + 0 = Loss, 3 = Draw, 6 = Win

def task1():
    with open(f'input/rock_paper_scissors.txt', 'r') as input:
        sanitized_input = [x.replace('\n', '') for x in input.readlines()]

        score = 0

        for game in sanitized_input:
            match game:
                case "A X": # draw rock
                    score += 4
                case "A Y": # win paper
                    score += 8
                case "A Z": # loose scissors
                    score += 3
                case "B X": # loose rock
                    score += 1
                case "B Y": # draw paper
                    score += 5
                case "B Z":  # win scissors
                    score += 9
                case "C X": # win rock
                    score += 7
                case "C Y": # loose paper
                    score += 2
                case "C Z": # draw scissors
                    score += 6
        
        print(score)
    
def task2():
    with open(f'input/rock_paper_scissors2.txt', 'r') as input:
        sanitized_input = [x.replace('\n', '') for x in input.readlines()]

        score = 0

        for game in sanitized_input:
            match game:
                case "A X": # Opponent wins with rock
                    score += 3
                case "A Y": # Opponent draws with rock
                    score += 4
                case "A Z": # Opponent looses with rock
                    score += 8
                case "B X": # Opponent wins with paper
                    score += 1
                case "B Y": # Opponent draws with paper 
                    score += 5
                case "B Z":  # Opponent looses with paper   
                    score += 9
                case "C X": # Opponent wins with scissors    
                    score += 2
                case "C Y": # Opponent draws with scissors 
                    score += 6
                case "C Z": # Opponent looses with scissors 
                    score += 7
        
        print(score)

task1()
task2()