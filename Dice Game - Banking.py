########################## Dice Game Banking Probablity Simulation ##########################
"""
Here is the problem:

    1. Each player takes turns throwing 2 dice
    2. Whatever you roll on each turn accumulates - 2+5 = 7 - you have 7 point so far on that turn.
    3. Player may continue to roll, or bank, after each successful roll.
    4. "Bank" ends turn, player adds points earned that turn to their existing bank (if there is one)
    5. First player to 100 wins
    6. Roll double ones and your turn is forfeit, your points accumulated that turn are wiped out,
       AND your bank gets wiped out
    7. Roll a seven and your turn is forfeit and your points accumulated that turn are wiped out.
    8. Roll doubles and the total is doubled. In other words, roll two fives and you receive 20 points
    9. Roll doubles three times in a row and your turn is forfeit, your points accumulated that turn
       are wiped out, AND your bank gets wiped out
    10. Once a player reaches 100, they may continue to roll, or opt to bank. Each player gets one more
        turn to attempt to surpass that player. If someone does, then everyone gets one more turn to do
        the same, and on it goes until someone is over 100 and everyone has had a turn to surpass that player.

When is the optimal time to "bank"?
Most times we bank around 25 points on a single turn. Going over 25 is deemed risky.

"""
import math
import random
random.seed()
 
def d6():
    """
    Randomly rolls a dice with 6 sides.
    Returns integer.
    """
    return random.randint(1, 6)

def T_S(Roll1, Roll2, turn_score, total_score):
    """
    Scoring helper function.
    The function must be initialized.
    This is so it can score mid turn.
    Returns integer.
    """
    # Summing score
    S1 = Roll1 + Roll2
## Check to see if function is working correctly
    # uncomment print statements below:
##    print('Roll 1 = ', Roll1)
##    print('Roll 2 = ', Roll2)
##    print('Sum 1 in theory = ', S1)
    
    if Roll1 == 1 and Roll2 == 1:
        turn_score = 0
        total_score = 0
        return [turn_score, total_score]

    if S1 == 7:
        turn_score = 0
        return [turn_score, total_score]

    if Roll1 != Roll2:
        turn_score = S1
        total_score = total_score + turn_score
        return [turn_score, total_score]
            
    if Roll1 == Roll2:
        turn_score = 2*S1
        total_score = total_score + turn_score
        return [turn_score, total_score]

def Roll():
    """
    Plays one run of the dice game until the player's turn ends
    based on the scoring helper function.
    Turn ends once the total score is over 100 or turn score is 0.
    The function assumes 3 turns are played so that triple doubles
    can be properly scored.
    Returns the final turn number and corresponding score
    as list of integers.
    """
    # Initializes turn 1.
    turn = 0
    turn_score = 0
    total_score = 0
    prev_turn1_R1 = 0
    prev_turn1_R2 = 0
    prev_turn2_R1 = 0
    prev_turn2_R2 = 0
    prev_turn3_R1 = 0
    prev_turn3_R2 = 0

    while True:
            ## Turn 1
            Roll1 = d6()
            Roll2 = d6()
            S1 = Roll1 + Roll2
            turn += 1

## Check to see if function is working correctly
    # uncomment print statements below:
##            print('\n')
##            print('TURN = ', turn)
##            print('Start Turn Score = ', turn_score)
##            print('Start Total Score = ', total_score)
##            print('Previous Roll 1 = ', prev_turn1_R1)
##            print('Previous Roll 2 = ', prev_turn1_R2)
##            print('Previous Roll 1 = ', prev_turn2_R1)
##            print('Previous Roll 2 = ', prev_turn2_R2)
##            print('Previous Roll 1 = ', prev_turn3_R1)
##            print('Previous Roll 2 = ', prev_turn3_R2)
##            print('New Roll 1 = ', Roll1)
##            print('New Roll 2 = ', Roll2)

            # Score turn 1
            TS = T_S(Roll1, Roll2, turn_score, total_score)
            turn_score = TS[0]
            total_score = TS[1]

## Check to see if function is working correctly
    # uncomment print statements below:
##            print('End of Turn Score = ', turn_score)
##            print('End of Turn Total Score = ', total_score)

            # Check exit condition.
            if turn_score == 0 or total_score >= 100:
                return [turn, total_score]

            # Remember roll from turn 1.
            prev_turn1_R1 = Roll1
            prev_turn1_R2 = Roll2
            
            ## Turn 2
            new_Roll1 = d6()
            new_Roll2 = d6()
            turn += 1

## Check to see if function is working correctly
    # uncomment print statements below:
##            print('\n')
##            print('TURN = ', turn)
##            print('Turn Score = ', turn_score)
##            print('Total Score = ', total_score)
##            print('Previous Roll 1 = ', prev_turn2_R1)
##            print('Previous Roll 2 = ', prev_turn2_R2)
##            print('Previous Roll 1 = ', prev_turn3_R1)
##            print('Previous Roll 2 = ', prev_turn3_R2)
##            print('Previous Roll 1 = ', prev_turn1_R1)
##            print('Previous Roll 2 = ', prev_turn1_R2)
##            print('New Roll 1 = ', new_Roll1)
##            print('New Roll 2 = ', new_Roll2)
            
            Roll1 = new_Roll1
            Roll2 = new_Roll2
            S1 = Roll1 + Roll2

## Check to see if function is working correctly
    # uncomment print statements below:
##            if Roll1 == Roll2 and prev_turn1_R1 == prev_turn1_R2:
##                    turn_score = 0
##                    total_score = 0
##                    return [turn, total_score]

            # Score turn 2
            TS = T_S(Roll1, Roll2, turn_score, total_score)
            turn_score = TS[0]
            total_score = TS[1]

            # Check exit condition.
            if turn_score == 0 or total_score >= 100:
                return [turn, total_score]

## Check to see if function is working correctly
    # uncomment print statements below:
##            print('End of Turn Score = ', turn_score)
##            print('End of Turn Total Score = ', total_score)

            # Remember roll from turn 2.
            prev_turn2_R1 = new_Roll1
            prev_turn2_R2 = new_Roll2

            ## Turn 3
            next_Roll1 = d6()
            next_Roll2 = d6()
            turn += 1

## Check to see if function is working correctly
    # uncomment print statements below:
##            print('\n')
##            print('TURN = ', turn)
##            print('Turn Score = ', turn_score)
##            print('Total Score = ', total_score)
##            print('Previous Roll 1 = ', prev_turn3_R1)
##            print('Previous Roll 2 = ', prev_turn3_R2)
##            print('Previous Roll 1 = ', prev_turn1_R1)
##            print('Previous Roll 2 = ', prev_turn1_R2)
##            print('Previous Roll 1 = ', prev_turn2_R1)
##            print('Previous Roll 2 = ', prev_turn2_R2)
##            print('New Roll 1 = ', next_Roll1)
##            print('New Roll 2 = ', next_Roll2)
            
            Roll1 = next_Roll1
            Roll2 = next_Roll2
            S1 = Roll1 + Roll2

            # Check triple doubles condition.
            if Roll1 == Roll2 and prev_turn2_R1 == prev_turn2_R2 and prev_turn3_R1 == prev_turn3_R2:
                    turn_score = 0
                    total_score = 0
                    return [turn, total_score]

            # Score turn 3
            TS = T_S(Roll1, Roll2, turn_score, total_score)
            turn_score = TS[0]
            total_score = TS[1]

            # Check exit condition.
            if turn_score == 0 or total_score >= 100:
                return [turn, total_score]

## Check to see if function is working correctly
    # uncomment print statements below:
##            print('End of Turn Score = ', turn_score)
##            print('End of Turn Total Score = ', total_score)

            # Remember roll from turn 3.
            prev_turn3_R1 = next_Roll1
            prev_turn3_R2 = next_Roll2

def nRollTest(numTrials): 
    """
    This function returns the mean score and mean number of rolls
    when playing the banking dice game along with some other stats.
    numTrials: Integer total number of runs we perform.
    """
    scores = []
    turns = []
    for t in range(numTrials):
        dummy_roll = Roll()
        turns.append(dummy_roll[0])
        scores.append(dummy_roll[1])
    print(' Mean Expected Score =', round(sum(scores)/len(scores), 4)) 
    print(' Max Score =', max(scores), 'Min Score =', min(scores))
    print(' Mean Total Number of Turns =', round(sum(turns)/len(turns), 4)) 
    print(' Max Rolls =', max(turns), 'Min Rolls =', min(turns))
    print('\n')

numTrials = 10000
nRollTest(numTrials)
