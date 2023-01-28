import random


# set variables
score = 100  # score of user
operator = ["+", "-", "*", "/"]  # operators
# open log file
file1 = open('log.txt', 'a')


# this function prints the dashes
def dash():
    print("-" * 50)


while 0 <= score <= 200:  # while score greater than 0 and less than 200
    dash()
    print("You currently hold: ", score, " points")
    print("Get more than 200 points you win, under 0 you lose")
    number_1 = random.randint(1, 9)  # this variable will be a random number between 1 and 9
    number_2 = random.randint(0, 10)  # this variable will be a random number between 0 and 10
    sign = random.choice(operator)  # chooses random operator
    real_answer = eval(str(number_1) + str(sign) + str(number_2))  # evaluates the real answer

    print(str(number_1) + str(sign) + str(number_2), "=")
    dash()
    print("Press x to close program")
    answer = input("Enter your guess of number: ")
    equal_sign = "="
    question_log = str(number_1) + str(sign) + str(number_2) + str(equal_sign) + str(answer) + str("\n")

    if answer == "x":  # when answer = x terminate
        print("Program has been terminated properly")
        break
    try:  # test weather answer is float otherwise return INVALID INPUT
        float(answer)
    except:
        print("INVALID INPUT PLEASE TRY AGAIN")
        continue

    if float(answer) == real_answer:  # if answer correct add 9 to score
        score = score + 9
        file1.write(question_log)
        continue
    elif float(answer) != real_answer:  # if answer wrong subtract 10 from score
        score = score - 10
        file1.write(question_log)
        continue
#losing message
if score < 0:
    dash()
    print("UNLUCKY YOU LOST!")
    dash()
#winning message
elif score > 200:
    dash()
    print("            CONGRATULATIONS YOU WON!       ")
    dash()

#close log file
file1.close()
