import requests
from tkinter import *
import random

# Global variable to store questions and current question index
score=0
questions = []
current_question_index = 0

# Fetch questions from the API
def get_questions():
    global questions
    url = ""
    
    if sport_var.get() == 1:
        url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=medium&type=boolean"
    elif anime_var.get() == 1:
        url = "https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=boolean"
    elif computers_var.get() == 1:
        url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean"
    elif geography_var.get() == 1:
        url = "https://opentdb.com/api.php?amount=10&category=22&difficulty=medium&type=boolean"
    elif animals_var.get() == 1:
        url = "https://opentdb.com/api.php?amount=10&category=27&difficulty=medium&type=boolean"
    elif history_var.get() == 1:
        url = "https://opentdb.com/api.php?amount=10&category=23&difficulty=medium&type=boolean"
    
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            questions = data['results']
        else:
            print("Error fetching data from the API")

# Function to display questions in a new window
def show_questions():
    
    global current_question_index 
    
    # Fetch questions if it's the first time or all questions have been answered
    if current_question_index == 0 or current_question_index >= len(questions):
        get_questions()
        current_question_index = 0

    # Create a new Toplevel window if not already created
    global question_window
    try:
        question_window.winfo_exists()
    except NameError:
        question_window = Toplevel()
        question_window.title("Quiz Questions")
        question_window.minsize(600, 400)
        question_window.config(bg="black")

    # Clear the canvas for the new question
    for widget in question_window.winfo_children():
        widget.destroy()
    score_label = Label(question_window, text=f"Score: {score}", bg="black", font=("arial", 15, "bold"), fg="yellow")
    score_label.grid(column=0, row=0)
    # Create a canvas for image and question
    canvas = Canvas(question_window, width=600, height=600, highlightthickness=0, bg="black")
    card = PhotoImage(file="C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/Quize/Untitled design (2).png")
    canvas.create_image(300, 300, image=card)
    canvas.config(bg="black")
    canvas.grid(column=0, row=1, columnspan=2)
    canvas.image = card

    # Display the current question
    current_question = questions[current_question_index]
    canvas.create_text(300, 200, text=current_question['question'], font=("arial", 16, "bold"), fill="black", 
                    width=300, anchor='n')

    # Create buttons for True/False answers
    true_button = Button(question_window, text="True", font=("Arial", 16), bg="#a8e6cf", 
                        command=lambda: check_answer(question_window, current_question, "True"))
    true_button.grid(column=0, row=2, padx=20, pady=20)
    
    false_button = Button(question_window, text="False", font=("Arial", 16), bg="#ff8b94", 
                        command=lambda: check_answer(question_window, current_question, "False"))
    false_button.grid(column=1, row=2, padx=20, pady=20)

    # Global result label for feedback
    global result_label
    result_label = Label(question_window, text="", font=("arial", 16, "bold"), bg="black", fg="white")
    result_label.grid(column=0, row=3, columnspan=2)


# Function to check if the selected answer is correct
def check_answer(window, question, selected_answer):
    global current_question_index , score

    # Determine if the answer is correct
    if selected_answer == question['correct_answer']: 
        result_text = "Correct!"
        result_color = "green"
        score+=1
        
    else:
        result_text = "Wrong!"
        result_color = "red"

    # Show result in the global result_label
    result_label.config(text=result_text, fg=result_color)

    # Move to the next question after a short delay
    current_question_index += 1
    window.after(1000, show_questions)  # 1 second delay before loading the next questi
        


# Function to display the game window
def game():
    global sport_var,history_var , animals_var , anime_var , computers_var , geography_var
    sport_var = IntVar()
    history_var = IntVar()
    animals_var = IntVar()
    anime_var = IntVar()
    computers_var = IntVar()
    geography_var = IntVar()

    window1 = Toplevel()
    window1.title("Game")
    window1.minsize(1000, 1000)
    window1.config(padx=0, pady=0, bg="black")

    select = Label(window1, text="Please pick one niche:", font=("arial", 24, "bold"), bg="#ffd230")
    select.grid(column=0, row=0)

    sport = Checkbutton(window1, text="Sport", font=("arial", 24, "bold"), bg="#ffd230", variable=sport_var)
    sport.grid(column=0, row=2)

    history = Checkbutton(window1, text="History", font=("arial", 24, "bold"), bg="#ffd230", variable=history_var)
    history.grid(column=0, row=4)

    animals = Checkbutton(window1, text="Animals", font=("arial", 24, "bold"), bg="#ffd230", variable=animals_var)
    animals.grid(column=0, row=6)

    anime = Checkbutton(window1, text="Anime (Japan)", font=("arial", 24, "bold"), bg="#ffd230", variable=anime_var)
    anime.grid(column=0, row=10)

    computers = Checkbutton(window1, text="Computers", font=("arial", 24, "bold"), bg="#ffd230", variable=computers_var)
    computers.grid(column=0, row=12)

    geography = Checkbutton(window1, text="Geography", font=("arial", 24, "bold"), bg="#ffd230", variable=geography_var)
    geography.grid(column=0, row=14)

    # Create an image button to trigger questions display
    pic = PhotoImage(file="C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/Quize/let’s start (1).png")
    
    image_button = Button(window1, image=pic, command=show_questions, borderwidth=0, highlightthickness=0)
    image_button.image = pic  # To prevent garbage collection
    image_button.grid(column=3, row=7, rowspan=6)

    # Add spacers for layout
    space = Label(window1, text=" ", bg="black")
    space.grid(column=1, row=3)
    space1 = Label(window1, text=" ", bg="black")
    space1.grid(column=1, row=5)
    space2 = Label(window1, text=" ", bg="black")
    space2.grid(column=0, row=7)
    space3 = Label(window1, text=" ", bg="black")
    space3.grid(column=0, row=9)
    space4 = Label(window1, text=" ", bg="black")
    space4.grid(column=1, row=11)
    space5 = Label(window1, text=" ", bg="black")
    space5.grid(column=1, row=13)
    space6 = Label(window1, text=" ", bg="black")
    space6.grid(column=1, row=1)

    window1.mainloop()

# Main window setup
window = Tk()
window.title("Quiz Game")
window.minsize(600, 600)
window.config(padx=50, pady=50, bg="black")

canvas = Canvas(window, width=600, height=600, highlightthickness=0, bg="black")

# Load and display the main window image
card = PhotoImage(file="C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/Quize/Untitled design (2).png")
canvas.create_image(300, 300, image=card)
canvas.config(bg="black")
canvas.grid(column=0, row=0)

# Prevent garbage collection of the image
canvas.image = card

# Adding welcome text to the canvas
canvas.create_text(300, 150, text="Welcome", font=("Lucida Handwriting", 30, "bold"), fill="black")
canvas.create_text(300, 200, text="to", font=("Lucida Handwriting", 30, "bold"), fill="black")
canvas.create_text(300, 240, text="Quiz Game", font=("Lucida Handwriting", 30, "bold"), fill="black")
canvas.create_text(300, 360, text="Press the button", font=("Lucida Handwriting", 30, "bold"), fill="black")
canvas.create_text(300, 420, text="to start", font=("Lucida Handwriting", 30, "bold"), fill="black")

# Adding start button
start = Button(text="Start", width=35, font=("Arial", 16, "bold"), bg="#ffd230", command=game)
start.grid(column=0, row=1)

window.mainloop()
