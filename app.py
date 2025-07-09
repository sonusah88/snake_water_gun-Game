import random

CHOICES = ["snake", "gun", "water"]

def decide_winner(player, computer):
    if player == computer:
        return "Draw"
    elif (player == "snake" and computer == "water") or \
         (player == "water" and computer == "gun") or \
         (player == "gun" and computer == "snake"):
        return "Player"
    else:
        return "Computer"

def main():
    player_score = 0
    computer_score = 0
    history = []

    print("Welcome to Snake-Gun-Water Game!")
    print("Choices: snake, gun, water. Type 'exit' to quit.")

    while True:
        player_choice = input("\nYour choice: ").strip().lower()
        if player_choice == "exit":
            break
        if player_choice not in CHOICES:
            print("Invalid choice. Please choose from snake, gun, water.")
            continue

        computer_choice = random.choice(CHOICES)
        winner = decide_winner(player_choice, computer_choice)

        if winner == "Draw":
            result = "It's a draw! 😐"
        elif winner == "Player":
            result = "You win! 🎉"
            player_score += 1
        else:
            result = "Computer wins! 🤖"
            computer_score += 1

        history.append({
            "player": player_choice,
            "computer": computer_choice,
            "result": result
        })

        print(f"Computer chose: {computer_choice}")
        print(result)
        print(f"Score => You: {player_score} | Computer: {computer_score}")

    print("\nGame Over!")
    print("Game History:")
    for i, round in enumerate(history, 1):
        print(f"Round {i}: You - {round['player']}, Computer - {round['computer']}, Result - {round['result']}")

if __name__ == "__main__":
    main()
