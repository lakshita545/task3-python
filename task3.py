import random

print("******************* WELCOME TO THE ROCK-PAPER-SCISSORS GAME *******************")

print("---------------------------------------------")
print("| RULES TO BE FOLLOWED  :-                  |\n"
      + "|.Rock vs Paper -> Paper wins               |\n"
      + "|.Rock vs Scissors -> Rock wins             |\n"
      + "|.Paper vs Scissors -> Scissor wins         |")
print("---------------------------------------------")
while True:

    print("Choose: \n 1 for Rock \n 2 for Paper \n 3 for Scissors \n")

    user_choice = int(input("Enter your choice :"))

    while user_choice > 3 or user_choice < 1:
        user_choice = int(input('Enter a valid choice please!!'))
    if user_choice == 1: user_choice_name='Rock'
    if user_choice == 2: user_choice_name='Paper'
    if user_choice == 3: user_choice_name='Scissors'
    

    computer_choice = random.randint(1,3)
    if computer_choice == 1:computer_choice_name='Rock'
    elif computer_choice == 2:computer_choice_name='Paper'
    elif computer_choice == 3:computer_choice_name='Scissors'
    

    print("You chose: ", user_choice_name,"\n")
    
    print("Computer's choice: ", computer_choice)
    print("Computer chose:" , computer_choice_name,"\n")

    print(computer_choice_name ,"v/s", user_choice_name,"\n")

    if user_choice == computer_choice:
        print("Waiting for the results.....\n")
        print("<==It's a tie!==>\n")

    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("Waiting for the results.....\n")
        print(user_choice_name,"Wins!")
        print("<==You Win!!!==>\n")

    elif user_choice == "Paper" and computer_choice == "Rock":
         print("Waiting for the results.....\n")
         print(user_choice_name,"Wins!")
         print("<==You Win!!!==>\n")

    elif user_choice == "Scissors" and computer_choice == "Paper":
         print("Waiting for the results.....\n")
         print(user_choice_name,"Wins!")
         print("<==You Win!!!==>\n")

    else:
        print("Waiting for the reults.....\n ")
        print(computer_choice_name,'Wins')
        print("<==Computer Wins!!!==>\n")

    print("Do you want to play again? (Y/N)")
    ans= input().lower()
    if ans == 'n':
        print("------***EXIT***------")
        break
    print("----Thanks for playing!!----")


