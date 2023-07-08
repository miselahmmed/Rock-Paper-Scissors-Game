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
if q1==0:
    print(rock)
elif q1== 1:
    print(paper)
else:
    print(scisr)

import random

a=(random.randrange(0,3))
print(f"Computer Trun:its {a}")
if a==0:
    print(rock)
elif a== 1:
    print(paper)
else:
    print(scisr)
if q1==a:
    print("You won the game")
else:
    print("Good luck for next the time")