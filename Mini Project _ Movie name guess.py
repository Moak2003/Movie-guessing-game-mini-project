
import random

#Movie list (contains the name of all the movies used while playing the game)


movie_list = ["Matrix", "Spiderman Homecoming","Free Guy","Jumanji", "Red Notice",
              "Lucifer","Avatar", "Ironman", "Tenet", "Interstellar",
              "Dark Knight", "Prestige", "Predestination", "Titanic", "Momento",
              "Jurassic Park","Inception","John Wick","Batman","Superman",
              "Justice League","Captain Marvel","Ant Man","Ted","Bladerunner"]


def question(movie):                                                              # Generates the string where only the first and last characters of the string are shown
    question_string = ""                                                          # For Example: 
    for i in range(len(movie)):                                                   # Spiderman ==> S-------n
        if movie[i].isspace():
            question_string += " "
        elif i == 0:
            question_string+=movie[i]
        elif i == len(movie)-1 :
            question_string+=movie[i]
        else:
            question_string += "-"
    return question_string
        
def guess(string):                                                                #Takes a letter as input and reveals all of the entered letters present in the word
    question_string = ""                                                          # For example:
    for i in range(len(movie)):                                                   #       Word is  "Free Guy" presented as "F--- --y"
        if movie[i].isspace():                                                    #       For the input "e", the function outputs ===> "F-ee --y"
            question_string += " "
        elif movie[i] == string:
            question_string+=string
        elif movie[i] == string.upper():
            question_string += string.upper()
        else:
            question_string += mov_ques[i]
    return question_string

def new_game():                                                                    # This function starts a new game as in
    global movie                                                                   # It initiates/resets all the required variables and
    global mov_ques                                                                # removes all the movies names that have been used in previous runs
    global count
    global run
    global trylimit
    movie = random.choice(movie_list) # Picks a random movie from the list
    movie_list.remove(movie)          # Removes the movie from the list, so that the same movie does not get repeated.
    print("-"*50,end="\n\n")
    print("\t"+"--"*3,"! Movie Game !","--"*3,sep = '')
    mov_ques = question(movie)
    count = 0                      # No of guesses used up by the user
    run = True
    trylimit = 3                   # No of guesses available to the user

    
def endgame():                                                                      #This function is executedat the end of the game,
    global run                                                                      # to prompt the user, if he wants to continue or not
    if bool(movie_list):           #Checks if the movie list is empty               #The game ends automatically if the list of movies is exhausted.
        choice = str(input("Would you like to continue?(y/n)"))
        if choice == "y":
            return new_game()      # starts a new game
        else:
            run = False            # terminates the main loop
    else:
        print("Thank You for Playing!")                                             #After the movie list is exhausted the game ends and the main loop terminates
        run = False

new_game()  #Game starts
while run:
    print("\n\t"+mov_ques)
    print("\t"+"_"*len(mov_ques))
    print("\n\nChoices:\n1. Letter Guess\n2. Movie Guess",end="\n\n")    
    choice = str(input("Enter Choice: "))
    if choice == "1":  #Guess letter
        letter = str(input("Input a letter: "))
        if len(letter) == 1:
            mov_ques = guess(letter)
            count+=1    # no. of guesses reduce
        else:
            print("\n\nInvalid Input\n\n")
            
    elif choice == "2":
        ans = str(input("Enter your guess: "))                                          #Guess the name of the movie
        ans = ans.title()
        if ans == movie:  
            print("\n\nCongrats! You Won!",end="\n\n")                                  #If the guess is correct you win!
            endgame() 
            continue
        else:
            print("\n\nWrong! Try Again!",end="\n\n")                                   #If the guess is not correct you can retry (if you hv more guesses left)
        count+=1
    
    else:
        print("\n\n"+"Invalid Input"+"\n\n")

    print("No. of guesses left: ", trylimit-count)                                      # max no. of guesses - no. of guesses used = no. of guesses left
    
    if trylimit-count == 0:
        print("\n\nYou Lost! Out of guesses!")                                          # if the user is out of guesses the game ends
        print("\n The Movie was: ", movie)                                              # and the answer is displayed
        endgame()
        continue
    
