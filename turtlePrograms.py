import turtle
import pandas
import tkinter

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
answer_state = screen.textinput(title="Guess the State",prompt="What's another state's name?")

# def get_coordinates(x,y):
#     print(x,y)
# turtle.onscreenclick(get_coordinates)
answer_state = answer_state.title()
if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_row = data[data.state == answer_state]
    t.goto(int(state_row.x),int(state_row.y))
    t.write(answer_state)

screen.exitonclick()
# turtle.mainloop()