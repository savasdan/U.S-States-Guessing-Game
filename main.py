import turtle, pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []     #L17-18-19. You can write missing_states = [state for state in all_states if state not in guessed_states]
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        making_it_DF = pandas.DataFrame(missing_states)
        making_it_DF.to_csv("missingStates")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] # This returns True or False. Variable 'state_data' returns 1 row if True !
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

