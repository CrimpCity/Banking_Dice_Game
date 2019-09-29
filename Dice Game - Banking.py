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
I'd like to actually know the math.

Thanks for the help in advance!
"""
import math
import random
random.seed()
 
def d6():
        return random.randint(1, 6)


def T_S(Roll1, Roll2, turn_score, total_score):
    """
    Roll(n) assumes that n dice are thrown.
    It returns the final score and total number
    of dice throws it took.
    """
    S1 = Roll1 + Roll2
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
    Roll(n) assumes that n dice are thrown.
    It returns the final score and total number
    of dice throws it took.
    """
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
            Roll1 = d6()
            Roll2 = d6()
            S1 = Roll1 + Roll2
            turn += 1
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
##            
##            print('New Roll 1 = ', Roll1)
##            print('New Roll 2 = ', Roll2)

            TS = T_S(Roll1, Roll2, turn_score, total_score)
            
            turn_score = TS[0]
            total_score = TS[1]
##            print('End of Turn Score = ', turn_score)
##            print('End of Turn Total Score = ', total_score)

            if turn_score == 0 or total_score >= 100:
                return [turn, total_score]
             
            prev_turn1_R1 = Roll1
            prev_turn1_R2 = Roll2
            
            ## Turn 2
            new_Roll1 = d6()
            new_Roll2 = d6()
            turn += 1
            
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

##            if Roll1 == Roll2 and prev_turn1_R1 == prev_turn1_R2:
##                    turn_score = 0
##                    total_score = 0
##                    return [turn, total_score]
            
            TS = T_S(Roll1, Roll2, turn_score, total_score)
            turn_score = TS[0]
            total_score = TS[1]
            if turn_score == 0 or total_score >= 100:
                return [turn, total_score]
##            print('End of Turn Score = ', turn_score)
##            print('End of Turn Total Score = ', total_score)
            
            prev_turn2_R1 = new_Roll1
            prev_turn2_R2 = new_Roll2

            ## Turn 3
            next_Roll1 = d6()
            next_Roll2 = d6()
            turn += 1
            
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

            if Roll1 == Roll2 and prev_turn2_R1 == prev_turn2_R2 and prev_turn3_R1 == prev_turn3_R2:
                    turn_score = 0
                    total_score = 0
                    return [turn, total_score]
            
            TS = T_S(Roll1, Roll2, turn_score, total_score)
            turn_score = TS[0]
            total_score = TS[1]
            if turn_score == 0 or total_score >= 100:
                return [turn, total_score]
##            print('End of Turn Score = ', turn_score)
##            print('End of Turn Total Score = ', total_score)
            prev_turn3_R1 = next_Roll1
            prev_turn3_R2 = next_Roll2


    return [turn, total_score]

#Roll()


def simRoll(numTrials): 
    """
    Test
    """
    scores = []
    turns = []
    for t in range(numTrials):
        dummy_roll = Roll()
        turns.append(dummy_roll[0])
        scores.append(dummy_roll[1])
    return scores, turns

numTrials = 5
##print(simRoll(numTrials))


def nRollTest(numTrials): 
    """
    This function returns the mean score and mean number of rolls when playing the Dice Game along with some other stats.
    nDiceSet: A list of integers which corresponds to the number n of how many dice are being used.
    numTrials: Integer total number of runs we perform for each n number of dice.
    """
    scores = []
    turns = []
    for t in range(numTrials):
        dummy_roll = Roll()
        turns.append(dummy_roll[0])
        scores.append(dummy_roll[1])
##    print(' Complete Run =', turns, scores) 
    print(' Mean Expected Score =', round(sum(scores)/len(scores), 4)) 
    print(' Max Score =', max(scores), 'Min Score =', min(scores))
    print(' Mean Total Number of Turns =', round(sum(turns)/len(turns), 4)) 
    print(' Max Rolls =', max(turns), 'Min Rolls =', min(turns))
    print('\n')

numTrials = 10000
nRollTest(numTrials)







































                

##def simRoll(n, numTrials): 
##    """
##    Test
##    """
##    track_scores = []
##    track_rolls = []
##    for t in range(numTrials):
##        st = random.getstate()
##        random.setstate(st)
##        track_scores.append(Roll(n)[0])
##        random.setstate(st)
##        track_rolls.append(Roll(n)[1])
##    return track_scores, track_rolls
##
##
##def nRollTest(nDiceSet, numTrials): 
##    """
##    This function returns the mean score and mean number of rolls when playing the Dice Game along with some other stats.
##    nDiceSet: A list of integers which corresponds to the number n of how many dice are being used.
##    numTrials: Integer total number of runs we perform for each n number of dice.
##    """
##    for n in nDiceSet:
##        st = random.getstate()
##        random.setstate(st)
##        n_score = simRoll(n, numTrials)[0]
##        random.setstate(st)
##        n_rolls = simRoll(n, numTrials)[1]
##        print(' Rolling ', n, 'dice') 
##        print(' Mean Expected Score =', round(sum(n_score)/len(n_score), 4)) 
##        print(' Max Score =', max(n_score), 'Min Score =', min(n_score))
##        print(' Mean Total Number of Rolls =', round(sum(n_rolls)/len(n_rolls), 4)) 
##        print(' Max Rolls =', max(n_rolls), 'Min Rolls =', min(n_rolls))
##        print('\n')


##nRollTest((1, 3, 5, 10, 50, 100), 150)             # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
            


##def nRollTestgrtK(nDiceSet, numTrials, k): 
##    """
##    This function returns the mean score and mean number of rolls when playing the Dice Game along with some other stats.
##    nDiceSet: A list of integers which corresponds to the number n of how many dice are being used.
##    numTrials: Integer total number of runs we perform for each n number of dice.
##    k: Integer score we would like to be greater than or equal to.
##    """
##    for n in nDiceSet:
##        st = random.getstate()
##        random.setstate(st)
##        n_score = simRoll(n, numTrials)[0]
##        k_score = 0
##        
##        # Part D
##        for s in n_score:
##            if s >= int(k):
##                k_score += 1
##        prob_grtK = round(k_score / len(n_score),5)
##        
##        # Part B
##        random.setstate(st)
##        n_rolls = simRoll(n, numTrials)[1]
##        kr_exact = 0
##        for i in range(len(n_score)-1):
##            if n_score[i] == int(k):
##                kr_exact += n_rolls[i]
##        prob_eqK = round(kr_exact / sum(n_rolls),5)
##
##        # Part C
##        kr_grt = 0
##        for i in range(len(n_score)-1):
##            if n_score[i] >= int(k):
##                kr_grt += n_rolls[i]
##        prob_grt_K = round(kr_grt / sum(n_rolls),5)
##
##        # Summary of Results   
##        print(' Rolling ', n, 'dice') 
##        print(' Mean Expected Score =', round(sum(n_score)/len(n_score), 4)) 
##        print(' Max Score =', max(n_score), 'Min Score =', min(n_score))
##        print(' The probability that I have a score of at least ', k, ' =', prob_grtK)
##        print(' The probability that I get a score of exactly ', k, ' given one dice =', prob_eqK)
##        print(' The probability that I get a score of at least ', k, ' given one dice =', prob_grt_K)
##        print('\n')
##
##
####nRollTestgrtK((1, 3, 5, 10, 50, 100), 150, 12)             # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
####nRollTestgrtK((10, 10, 10, 10, 10, 10), 150, 12)           # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
##nRollTestgrtK((10,10), 150, 10)                               # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
####nRollTestgrtK((10,10), 150, 20)                               # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
####nRollTestgrtK((10,10), 150, 30)                               # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
####nRollTestgrtK((10,10), 150, 40)                               # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
####nRollTestgrtK((10,10), 150, 50)                               # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
####nRollTestgrtK((10,10), 150, 60)                               # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
####nRollTestgrtK((10,10), 150, 70)                               # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
####nRollTestgrtK((10,10), 150, 80)                               # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
####nRollTestgrtK((10,10), 150, 90)                               # Keep the maximum number of dice thrown <= 100 if you are using a CPU.
####nRollTestgrtK((10,10), 150, 100)                              # Keep the maximum number of dice thrown <= 100 if you are using a CPU.



        


