from random import randint

def main():
    s = ''
    name = ''
    stake = 0
    stake1 =0
    bet = 0
    player, stake, stake1 = get_player()
    while not s or s[0] in 'Yy':
        stake = play_the_game(stake)
        s = input('Play again? (Y or N): ')
    if s[0] in 'Nn':
        print('{} are quitting the game with {} of your original {}'.format(player, stake, stake1))

def get_player():
    player = str(input('Enter your player name: '))
    stake = int(input('How much do you have to stake in this game?'))
    stake1 = stake
    return player, stake, stake1

def play_the_game(stake):
    bet = int(input('How much do you want to bet? '))
    r = roll()
    if r == 7 or r == 11:
        print(r, 'is an instant WINNER!\n')
        stake += bet
        print('stake at instant winner 7 11 {}'.format(stake))
        return stake
    if r ==2 or r==3 or r==12:
        print(r, 'is an instant LOSER. So Sorry.\n')
        stake -= bet
        print('stake at instant LOSER is {}'.format(stake))
        return stake
    print('Your point to roll is now a ', r)
    point = r
    while True:
        s=input('Roll again (E=exit game)?')
        if len(s) > 0 and s[0] in 'Ee':
            return 
        r = roll()
        print('You rolled a ', r)
        if r == point:
            print('You\'re a WINNER!\n')
            stake += bet
            print('stake at this point is {}'.format(stake))

            return stake
        elif r == 7:
            print('So Sorry, you\'re a LOSER.\n')
            stake -= bet
            print('stake at this point is {}'.format(stake))
            return stake

def roll():
    d1 = (randint(1, 600) % 6) + 1
    d2 = (randint(1, 36) % 6) + 1
    print(d1, d2)
    return d1 + d2

main()
                  
            
    
