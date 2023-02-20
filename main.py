import turtle
import pandas
import csv


screen = turtle.Screen()
screen.title("US GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop() #this is a way to keep screen running after work has done
# #screen.exitonclick()


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Whats another state name?").title()
    if answer_state == "Exit":
        #print(answer_state ^ all_states) # doesnot work
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states: #this in method requires converting to list first
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #pullout the row where it is equal
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())#or use "answer_state"

#states to learn



