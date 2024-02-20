def get_winner():    
    user_input = None
    
    while True:
        
        player1, player2 = "", ""
        
        possible_pos = ['rock', 'paper', 'scissors']

        while player1 not in possible_pos:
            player1 = input("Player 1, would you like to be rock, paper, or scissors: ").lower()
                        
        while player2 not in possible_pos:
            player2 = input("Player 2, Would you like to be rock, paper, or scissors: ").lower()

        if player1 == player2:
            print("Tie!")
            
        elif (player1 == "rock" or player2 == "rock") and (player1 == "scissors" or player2 == "scissors"):
            if player1 == "rock":
                print("Player 1 winner!")
                
            else:
                print("Player 2 winner!")
                
        elif (player1 == "paper" or player2 == "paper") and (player1 == "rock" or player2 == "rock"):
            if player1 == "paper":
                print("Player 1 winner!")
                
            else:
                print("Player 2 winner!")
                
        elif (player1 == "scissors" or player2 == "scissors") and (player1 == "paper" or player2 == "paper"):
            if player1 == "scissors":
                print("Player 1 winner!")
                
            else:
                print("Player 2 winner!")
                
        while user_input not in ['yes', 'no']:
            user_input = input("Would you like to play again: ").lower()
            
        if user_input == "yes":
            continue
        
        else:
            break
        
get_winner()
                