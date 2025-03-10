import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif ((user_choice == 'rock' and computer_choice == 'scissors') or 
         (user_choice == 'scissors' and computer_choice == 'paper') or 
         (user_choice == 'paper' and computer_choice == 'rock')):
        return 'user'
    else:
        return 'computer'

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game!")
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to end): ").lower()

        if user_choice == 'quit':
            print("\nFinal Scores:")
            print(f"User: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == 'tie':
            print("It's a tie!")
        elif result == 'user':
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score: User {user_score} - {computer_score} Computer")

if __name__ == "__main__":
    main()
