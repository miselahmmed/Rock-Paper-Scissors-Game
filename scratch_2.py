print("Welcome to rock paper ciger game")
q1= int(input("What do you choose? 0 for rock, 1 for paper, 2 for Scissor"))
rock= ("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
paper = ("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
scisr = """
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """
#Verifing Your input
if q1==0:
    print(rock)
elif q1== 1:
    print(paper)
else:
    print(scisr)

#Computer Turn
import random

a=(random.randrange(0,3))
print(f"Computer Trun:its {a}")
if a==0:
    print(rock)
elif a== 1:
    print(paper)
else:
    print(scisr)

#Logic
if q1==0 and a== 2:
    print("You won this game, Computer Lose this game")
elif q1==2 and a== 1:
    print("You won this game, Computer Lose this game")
elif q1==1 and a== 0:
    print("You won this game, Computer Lose this game")
else:
    print("Good luck for next the time, Computer Won this game")
