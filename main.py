from turtle import Turtle, Screen
import pandas as pd

df = pd.read_csv("50_states.csv")

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
screen.setup(width=725, height=491)

t = Turtle()
t.hideturtle()

states_accounted_for = 0
states_list = []

while states_accounted_for < 50:
    guess = screen.textinput(f"{states_accounted_for}/50 States Correct", "Name a state: ").title()
    for state in df["state"]:
        if state == guess:
            if guess not in states_list:
                row = df[df["state"] == guess]
                state = row["state"].item()
                x = row["x"].item()
                y = row["y"].item()
                states_accounted_for += 1
                states_list.append(guess)
                t.penup()
                t.goto(x, y)
                t.pendown()
                t.write(state)
        else:
            pass

screen.exitonclick()

