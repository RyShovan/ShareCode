
correct_ans = 0
wrong_ans = 0
pass_ans = 0
a = ""

while a != "exit":
    a = input("> ")
    if a.upper() == "C":
        correct_ans += 1
        print("[", (correct_ans + wrong_ans + pass_ans), "]\n-------------------")
    elif a.upper() == "W":
        wrong_ans += 1
        print("[", (correct_ans + wrong_ans + pass_ans), "]\n-------------------")
    elif a.upper() == "P":
        pass_ans += 1
        print("[", (correct_ans + wrong_ans + pass_ans), "]\n-------------------")
    elif a.upper() == "SHOW":
        print("\nCorrect Answer =", correct_ans, "\nWrong Answer =", wrong_ans, "\nPassed Question =", pass_ans, "\n--------------------\nTotal Questions =", (correct_ans + wrong_ans + pass_ans))
    elif a.upper() == "EXIT":
        print("\nCorrect Answer =", correct_ans, "\nWrong Answer =", wrong_ans, "\nPassed Question =", pass_ans, "\n--------------------\nTotal Questions =", (correct_ans + wrong_ans + pass_ans))
    else:
        print("Wrong input... Try Again...")
