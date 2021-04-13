# r>s, s>p, p>r
import random 


def play():
    user = input("Enter your choice -  r,s,p\n")
    computer = random.choice(['r','s','p'])
    
    if user == computer:
        return 'Its a tie'
        print('Its a Tie')
    if win(user, computer):
        return 'You won!' 
        print('You won!')  
        
    return 'You Lost!'
    print ('You lost!')

def win(player, opponent):
    #return true if player wins
    # r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())



