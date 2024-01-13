##dictionary to store the questions an their answers
questions = {'what is your name? ': 'A',
              'what is my age?': 'B', 
              "what school am I in? ": 'C', 
              "Where is my home?": 'D'}
#print(len(questions))
#creating a 2D list of the multiple questions
options = [['A. Sharleen', 'B. Shamza', 'C. Nicole', 'D. Tressy'],
           ['A. seventeen', 'B. twenty one', 'C. nineteen', 'D. twenty'],
            ['A. MMU', 'B. KU', 'C. KCAU', 'D. JKUAT'],
             ['A. Kikuyu', 'B. vihiga', 'C. Thika', 'D. Machakos']]
##print(answers[0][1]) #accessing a value from the nested list
##print(questions)
def newGame():
    guesses = [] # list of the guesses
    correct_guesses = 0 #
    question_num= 0 ##current question number --represents question one
    for key in questions:  ##loop through the questions
        print('--------------------')
        print(key)
        for i in options[question_num]: ##to display the diferent options for each question using the index no. so as not display all options for each question
            print(i)
        guess = input("Please enter your answer (A/B/C/D):")
        guess = guess.upper() ##incase the user enters a lower case value
        guesses.append(guess) #add the guess to the list of guesses

        correct_guesses += check_answer(questions.get(key), guess) ##count the correct guesses
        question_num += 1 ##increase the number index of the options
    displayScore(correct_guesses, guesses) #display our score, where it compares the correct guesses with out list of guesses

def check_answer(answer, guess):
    if answer== guess:
        print('CORRECT')
        return 1 #return a point if correct
    else:
        print('WRONG')
        return 0 #return no pint to wrong answer
def displayScore(correct_guesses, guesses):
    print('---------------')
    print('RESULTS')
    print("-----------------")

    print('Answers: ', end="") #prints the answers and not end on a new line
    for key in questions:
        print(questions.get(key), end=" ") ##print the values of the questions, by looping through the dictionary
    print()

    print('GUESSES: ', end="") 
    for i in guesses:  ##loop through the elements of the list of guesses
        print(i, end=" ")
    
     ##calculate final score
    score = float((correct_guesses*100) / len(questions))
    print('your score is: ' + str(score) +('%'))

def play_again():
    response = input('Do you want to play again? (yes or no): ')
    response = response.upper()
    if response == 'YES':
        return True
    else:
        return False
newGame()

while play_again():
    newGame()
print('byeeee!')