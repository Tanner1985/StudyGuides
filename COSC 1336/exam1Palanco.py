#Simple script to ask questions and print answers for study
def main():
    question_list = questionList()
    answer_list = answerList()
    questionNum = random_question(len(question_list))
    answer = input(f'{question_list[questionNum]}: ')
    print(f'You answered: {answer}')
    print(f'The correct answer is: {answer_list[questionNum]}')
    play_again = input('Would you like to play again? (yes or no): ')
    if play_again == 'yes'or play_again == 'Yes' or play_again == 'YES':
        main()
    else:
        print('Thank you for playing!')

def random_question(length):
    import random
    random_number = random.randint(0,length)
    return random_number

def questionList():
    question_list = ['What is the binary representation of 185?', 'What is a key word in programing?', 'What translates an assembly language program to a machine language program?', \
                     'What are the rules that must be follwed when writing a program called?']
    return question_list
def answerList():
    answer_list = ['10111001','A predefined term in a programming language that is used for a specific operation', 'An assembler', 'Syntax' ]
    return answer_list

main()
