from tkinter import *
import random

handMap = [[("r-r", "Draw."),
            ("r-p", "You lose."),
            ("r-s", "You win!" )],
           [("p-r", "You win!" ),
            ("p-p", "Draw."),
            ("p-s", "You lose.")],
           [("s-r", "You lose."),
            ("s-p", "You win!" ),
            ("s-s", "Draw.")]]

hands = ["rock", "paper", "scissors"]

appwindow = Tk()
appwindow.title("Rock Paper Scissors")

frame = Frame(appwindow)
frame.pack()
rock = PhotoImage(file="Rock.png")
paper = PhotoImage(file="Paper.png")
scissors = PhotoImage(file="Scissors.png")

textlabel = Text(appwindow, height=5)
textlabel.insert(INSERT, "Choose your hand.")


def fight(hand):
    opponenthand = random.randint(0, 2)
    result = handMap[hand][opponenthand][1]
    textlabel.delete(1.0, END)
    textlabel.insert(INSERT, "Opponent chooses " + hands[opponenthand] + ". " + result)
    return result

def rockchosen(): fight(0)
def paperchosen(): fight(1)
def scissorschosen(): fight(2)


handsframe = Frame(appwindow)
rockbutton = Button(handsframe, image=rock, command=rockchosen)
paperbutton = Button(handsframe, image=paper, command=paperchosen)
scissorsbutton = Button(handsframe, image=scissors, command=scissorschosen)

rockbutton.pack(side=LEFT)
paperbutton.pack(side=LEFT)
scissorsbutton.pack(side=RIGHT)
handsframe.pack()
textlabel.pack()

appwindow.mainloop()


