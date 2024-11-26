import random

word_list=['paython' , 'java' , 'javascript' , 'programing']

def scramble_word(word):

    word_list = list(word)

    random.shuffle(word_list)
    return ''.join(word_list)

def word_scramble_game():
    word_o = random.choice(word_list)
    scrambled_word = scramble_word(word_o) 


    print("Welcome to the Word Scramble Game!")
    print(f"Try to guess the original word from the scrambled word: {scrambled_word}" )
    print("You have 5 attempts.")

    attempts = 5

    while attempts > 0 :
        guess = input(f"Enter your answer (attempts left:{attempts} )")

        if guess==word_o:
            print ("congratulations you are succes")
            break
        else:
            attempts-=1
            print(f"you faild, try again. you have {attempts} attempts")

            if attempts==0 :
               print(f"you are faild, the correct answer is {word_o}")


if __name__ == "__main__" :
    word_scramble_game()
