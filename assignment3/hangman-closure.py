# Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []
    
    def hangman_closure(letter):
        guesses.append(letter)
        display = ""
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"
        print(display)
        # Check if all letters guessed
        all_guessed = all(char in guesses for char in secret_word)
        return all_guessed
    
    return hangman_closure

# Game
if __name__ == "__main__":
    secret = input("Enter secret word: ").lower()
    hangman = make_hangman(secret)
    
    while True:
        guess = input("Guess a letter: ").lower()
        done = hangman(guess)
        if done:
            print("Congratulations! You guessed the word!")
            break