import random

while True:
    choices = ['scissors','stone','paper']
    ai_choice = random.choice(choices)
    user_choice = input("I have already chose mine. Choose yours. :-)\n> ")
    final_choice = user_choice.lower()

    if final_choice == 'scissors'and ai_choice == 'stone':
        print('I chose stone and since stone >>>> scissors, I win and You lose!')

    elif final_choice == 'scissors'and ai_choice == 'paper':
        print('I chose paper and you chose scissors and since scissors >>>> paper, I lose and You win.')

    elif final_choice == 'stone'and ai_choice == 'paper':
        print('I chose paper and since paper >>>> stone, I win and You lose!')

    elif final_choice == 'stone'and ai_choice == 'scissors':
        print("I chose scissors and since stone >>>> scissors, I lose and You win.")

    elif final_choice == 'paper'and ai_choice == 'stone':
        print("I chose stone and since paper >>>> stone, I lose and You win.")

    elif final_choice == 'paper'and ai_choice == 'scissors':
        print('I chose scissors and since scissors >>>> paper, I win and You lose!')  

    elif final_choice == ai_choice:
        print("Oh! We both chose the same that means nobody won. Let's Try again.")  

    elif user_choice == 'bye':
        print("It was nice playing with you. Thanks for your time.\nBye Bye ;-)")
        exit()