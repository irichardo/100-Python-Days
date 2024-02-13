import random

def check_win(blank_word_joined):
    if blank_word_joined.find("_") == -1:
        print("Congratulations you win.")
        return True

def hangedMan():
    words = ["Truck", "Chicken", "Shiiirt", "Lemonade"]
    random_word = random.choice(words)
    letters_sended = [" -"]
    blank_word_separated = list("_" * len(random_word))
    lives = 5
    playing = True
    
    while playing:
        blank_word_joined = "".join(blank_word_separated)
        try:
            if check_win(blank_word_joined):
                playing = False
            elif lives == 0:
                 print(f"Game Over, the solution es {random_word}")
                 break
            else:
                letter = str(input(f"Welcome to the hangedMan!, please introduce a letter to find the word: { blank_word_joined } \n")).lower()
                letters_sended.append("  " + letter + "  -")
                print("letters sended before: ", "".join(letters_sended))
                if letter in random_word.lower():
                #for get the letters where that's exists
                    position = [i for i, char in enumerate(random_word.lower()) if char == letter]
                    for position_letter in position:            
                        if position_letter == 0:
                         blank_word_separated[position_letter] = letter.upper()
                        else:
                            blank_word_separated[position_letter] = letter
                else:
                    lives -= 1
                    print(f"You have only {lives} lives. ")                  
        except ValueError:
            print("Please introduce valid data.")
hangedMan()