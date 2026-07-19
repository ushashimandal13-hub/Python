#python quiz game
question=("How many bones are in the human body?",
          "world's largest sweet water lake")
options = (("A. 106" ,"B. 306","c. 206", "D. 90" ),
           ("A. Michigan" ,"B. Eri","c. Ontario", "D. Superior"))
ans=("C","D")
guess=[]
score=0
question_num = 0
for questions in question:
    print(question)
    print()
    for option in options[question_num]:
        print(option)
    guess=input("Enter(A,B,C,D): ").upper()
    if guess == ans[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect")
        print(f"{ans[question_num]} is the correct answer.")
    question_num+=1
print("----Result----")
print()
print("Answers: ", end="")
for answer in ans:
    print(ans, end=" ")
print()

print("Guesses: ", end=" ")
for guesses in guess:
    print(guess, end=" ")
print()