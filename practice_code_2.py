import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
"""Creates and modifies images."""
from PIL import ImageTk
"""Provides the python intepreter with image editing capabilities."""
from PIL import Image
import os
"""Allows the current date to be imported."""
from datetime import date
"""Allows the current time to be imported."""
from datetime import datetime
"""Allows json file to be used for data."""
import json

class MainWindow:
    def __init__(self, master):
        self.master=master
        master.title("Main Window")
        master.geometry("1200x700")
        master.resizable(False, False)
        master.configure(background="lemon chiffon")
        
        # Display labels for title and substitle.
        program_title=tk.Label(master,
                                 text="KiwiDrive",
                                 font=("Helvetica", 100, "bold"),
                                 fg="gold",
                                 bg="lemon chiffon")
        program_title.place(x=100, y=200)

        sub_title=tk.Label(master, 
                             text="Learn. Quiz. Test.", 
                             font=("Helvetica", 20),
                             bg="lemon chiffon")
        sub_title.place(x=100, y=370)

        # Create image.
        image=Image.open("yellow_road_image.png")
        resize_image=image.resize((400, 400))
        img=ImageTk.PhotoImage(resize_image)
        road_image=tk.Label(image=img, bd=0, highlightthickness=0)
        road_image.image=img
        road_image.place(x=750, y=200)

        # Create dots for the letter I. To look like a traffic light.
        dots=[(193, 'red'), (335, 'goldenrod1'), (522, 'green')]
        for x, color in dots:
            canvas=tk.Canvas(master, width=50, height=50, bg="lemon chiffon", bd=0, highlightthickness=0)
            canvas.place(x=x, y=202)
            canvas.create_oval(15, 15, 35, 35, fill=color, outline='')

        # Create a coloured box for the top where navigation bar will be.
        canvas=Canvas(master,
                        height=70,
                        width=1210,
                        bg="black")
        canvas.place(x=0, y=0)

        # Create Sign up, log in, and exit buttons.
        login_btn=tk.Button(master, text="Log in", width=11, height=2,
                             font=("Helvetica", 10, "bold"), command=self.open_login_window)
        signup_btn=tk.Button(master, text="Sign up", width=11, height=2,
                             font=("Helvetica", 10, "bold"), command=self.open_signup_window)
        exit_btn=tk.Button(master, text="Exit", width=11, height=2,
                             font=("Helvetica", 10, "bold"), command=self.checkexit)
        
        # Place signup, login, and exit buttons.
        login_btn.place(x=830, y=15)
        signup_btn.place(x=940, y=15)
        exit_btn.place(x=1080, y=15)

        # Set windows to none.
        self.login_window = None
        self.signup_window = None

    def open_login_window(self):
        if self.login_window is not None and self.login_window.winfo_exists():
            return
        # Destroy signup window if open
        if self.signup_window is not None and self.signup_window.winfo_exists():
            self.signup_window.destroy()
            self.signup_window = None

        self.login_window = tk.Toplevel(self.master)
        self.login_window.geometry("+800+150")
        LoginWindow(self.login_window, self)

    def open_signup_window(self):
        if self.signup_window is not None and self.signup_window.winfo_exists():
            return
        # Destroy login window if open
        if self.login_window is not None and self.login_window.winfo_exists():
            self.login_window.destroy()
            self.login_window = None

        self.signup_window = tk.Toplevel(self.master)
        self.signup_window.geometry("+800+150")
        SignupWindow(self.signup_window, self)

    def checkexit(self):
        """Function to confirm user wants to exit application."""
        response=mb.askquestion("Exit Programme?","Your "
                                              + "progress will NOT be saved."
                                              + "\nAre you sure you want to "
                                              + "exit the program?",
                                            icon='warning')
        if response == "yes":
            self.master.destroy()


class LoginWindow:
    def __init__(self, master, app):
        """Function to initialise window."""

        def login():
            """Function to validate user input and login user."""

            username=username_var.get()
            password=password_var.get()

            if username and password:
                if os.path.exists(f"{username}_info.txt"):
                    # Check for password.
                    with open(f"{username}_info.txt", "r") as file:
                        lines = file.read().splitlines()
                        words = (lines[4]).split()
                        stored_password = (words[1]).strip()

                        if password == stored_password:

                            # Create dictionary of user info for later access.
                            user_info = {
                                 "Username": username,
                                 "First name": ((lines[2]).split())[2].strip(),
                                 "Last name": ((lines[3]).split())[2].strip(),
                                 "Birthdate": ((lines[5]).split())[1].strip()
                                 }
                            
                            mb.showinfo("Successful", "Log in successful." +
                                        f"\nWelcome back {username}", parent=self.master)
                            self.master.destroy()
                            NewWindow(tk.Tk(), user_info)
                        else: 
                            mb.showerror("Invalid input", "Incorrect password. Please enter a valid password or signup.", parent=self.master)
                else:
                    mb.showerror("Invalid input", "Incorrect username. Please enter a valid username or signup.", parent=self.master)
            else:
                mb.showerror("Invalid input", "There are missing " +
                                    "fields.\nPlease enter all fields.", parent=self.master)

        self.master=master
        self.master.attributes('-topmost', True)
        master.title("Login")
        master.geometry("350x450")
        master.resizable(False, False)
        master.configure(background="lemon chiffon")
        self.app = app

        canvas=Canvas(master,
                        height=70,
                        width=350,
                        bg="black")

        # Create labels/buttons for title and user navigation.
        tk.Label(master, text="Log in:", font=("Helvetica", 15), fg="white", bg="black").place(x=10, y=24)
        tk.Label(master, text="Log into your account", font=("Helvetica", 10), fg="white", bg="black").place(x=82, y=30)
        tk.Button(master, text="Sign up", width=11, height=2, font=("Helvetica", 10, "bold"), command=self.switch_to_signup).place(x=240, y=15)
        login_btn=tk.Button(master, text="Log in", font=("Helvetica", 10, "bold"), width=11, height=2, fg="black", bg="gold", command=login)

        # Declaring name and password as string variables.
        username_var=tk.StringVar()
        password_var=tk.StringVar()

        # Create labels and entries for username and password.
        username_lbl=tk.Label(master,
                            text="Username:",
                            font=("Helvetica", 10, "bold"),
                            bg = "lemon chiffon")
        username_entry=tk.Entry(master,
                                textvariable=username_var)
        password_lbl=tk.Label(master,
                            text="Password:",
                            font=("Helvetica", 10, "bold"),
                            bg = "lemon chiffon")
        password_entry=tk.Entry(master,
                                textvariable=password_var,
                                show="*")
        
        # Place labels and entries.
        username_lbl.place(x=40, y=200)
        username_entry.place(x=120, y=200)
        password_lbl.place(x=40, y=240)
        password_entry.place(x=120, y=240)
        canvas.place(x=0, y=0)
        login_btn.place(x=120, y=400)

        # When the login window is closed manually.
        master.protocol("WM_DELETE_WINDOW", self.on_close)

    def switch_to_signup(self):
        """Function to close current window and open signup window."""
        self.master.destroy()
        self.app.login_window = None
        self.app.open_signup_window()

    def on_close(self):
        """Function to close this window."""
        self.app.login_window = None
        self.master.destroy()


class SignupWindow:
    def __init__(self, master, app):
        """Initialise the signup window."""
        def signup():
            """Function to validate user input when signing up."""
            first_name=first_name_var.get()
            last_name=last_name_var.get()
            username=username_var.get()
            password=password_var.get()
            confirm_password=confirm_password_var.get()
            birthdate=birthdate_var.get()
            age=None # Initialise the value.

            # Validate the user input if all fields are entered.
            if first_name and last_name and username and password and \
                confirm_password and birthdate:
                if not first_name.isalpha() or not last_name.isalpha():
                    mb.showerror("Invalid first name/last " +
                                        "name", "Please only enter letters " +
                                        "for first name and last name.", parent=self.master)
                elif not username.isalnum():
                    mb.showerror("Invalid username", "Please only " +
                                        "enter numbers or letters for username.", parent=self.master)
                elif os.path.exists(f"{username}_info.txt"):
                    mb.showerror("Invalid username", "This username " +
                                         "already exists.\nPlease enter a " +
                                         "different username.", parent=self.master)
                elif password != confirm_password:
                    mb.showerror("Invalid password", "Please check " +
                                        "that your passwords match.", parent=self.master)
                elif birthdate:
                    # Validate the birthdate entry.
                    try:
                        # Convert the string to a datetime object.
                        birthdate=datetime.strptime(birthdate, '%d/%m/%Y')
                        # Get todays date.
                        today=date.today()
                        # Find the difference between today and the date of birth.
                        difference=today.year - birthdate.year
                        # Find out if today preceeds the date of birth this year.
                        today_precedes_dob=(today.month, today.day) < \
                            (birthdate.month, birthdate.day)
                        age=difference - today_precedes_dob
                        if age <= 0 or age >=99:
                            mb.showerror("Invalid input", "Please enter a valid "
                                                "birthdate (dd/mm/yyyy)", parent=self.master)
                            return
                        elif age < 15 or age > 24:
                            age_maybe = mb.askquestion("Note", "Please note that "
                                                            "this application is "
                                                            "primarily designed for "
                                                            "ages 15-24, and may not "
                                                            "meet your individual "
                                                            "needs.\n\nAre you sure "
                                                            "you want to continue?", parent=self.master)
                            if age_maybe == "no":
                                return False
                        else:
                            mb.showinfo("Note", "Please enjoy this applications "
                                                "features and resources which are "
                                                "tailored specifically for ages 15-24 "
                                                "like yourself.", parent=self.master)
                    except ValueError:
                        # Show an error if the date format is incorrect.
                        mb.showerror("Invalid input", "Please enter a valid "
                                            "birthdate (dd/mm/yyyy)", parent=self.master)
                        return
                    
                    # Create an individual file for the user.
                    with open(f"{username}_info.txt", "a") as file:
                        file.write(f"\nUsername: {username}\n"
                                   f"First name: {first_name}\n"
                                   f"Last name: {last_name}\n"
                                   f"Password: {password}\n"
                                   f"Birthdate: {birthdate.strftime('%d/%m/%Y')}")
                        
                    #Debugging statment
                    print(age)
                        
                    # Create a dictionary of user info.
                    user_info = {
                                 "Username": username,
                                 "First name": first_name,
                                 "Last name": last_name,
                                 "Birthdate": birthdate.strftime('%d/%m/%Y')
                                 }

                    mb.showinfo("Successful", "Sign up successful." +
                                        f"\nWelcome {username}", parent=self.master)
                    self.master.destroy()

                    NewWindow(tk.Tk(), user_info)

            else:
                mb.showerror("Invalid input", "Please enter all fields", parent=self.master)
                        
        self.master=master
        self.master.attributes('-topmost', True)
        master.title("Signup")
        master.geometry("350x450")
        master.resizable(False, False)
        master.configure(background="lemon chiffon")
        self.app = app

        # Print today's date, neccassary for calculating the users age.
        # Print todays date.
        today=date.today()
        d=today.strftime("%d/%m/%y")
        print(f"Date: {d}")

        canvas=Canvas(master,
                        height=70,
                        width=350,
                        bg="black")

        # Create labels/buttons for title and user navigation.
        tk.Label(master, text="Sign up:", font=("Helvetica", 15), fg="white", bg="black").place(x=10, y=24)
        tk.Label(master, text="Create an account", font=("Helvetica", 10), fg="white", bg="black").place(x=82, y=30)
        tk.Button(master, text="Log in", width=11, height=2, font=("Helvetica", 10, "bold"), command=self.switch_to_login).place(x=240, y=15)
        tk.Button(master, text="Sign up", font=("Helvetica", 10, "bold"), width=11, height=2, fg="black", bg="gold", command=signup).place(x=120, y=400)

        # Declaring name and password as string variables.
        first_name_var=tk.StringVar()
        last_name_var=tk.StringVar()
        username_var=tk.StringVar()
        password_var=tk.StringVar()
        confirm_password_var=tk.StringVar()
        birthdate_var=tk.StringVar()

        fields=[
            ("First name:", first_name_var, False),
            ("Last name:", last_name_var, False),
            ("Username:", username_var, False),
            ("Password:", password_var, True),
            ("Confirm \nPassword:", confirm_password_var, True),
            ("Birthdate \n(dd/mm/yyyy):", birthdate_var, False),
        ]

        labels=[]
        entries=[]

        # Starting coordinates and spacing between fields.
        start_y=100
        y_step=45
        label_x=20
        entry_x=120

        # Use iteration to create labels and entries.
        for i, (label_text, var, is_password) in enumerate(fields):
            y=start_y + i * y_step
            
            # Create and place labels.
            lbl=tk.Label(master, text=label_text, font=("Helvetica", 10, "bold"), bg="lemon chiffon")
            lbl.place(x=label_x, y=y)
            labels.append(lbl)
            # Create and place entries.
            entry=tk.Entry(master, textvariable=var, show="*" if is_password else "")
            entry.place(x=entry_x, y=y)
            entries.append(entry)

        canvas.place(x=0, y=0)

        # When the signup window is closed manually
        master.protocol("WM_DELETE_WINDOW", self.on_close)

    def switch_to_login(self):
        """Function to close this window and open new login window."""
        self.master.destroy()
        self.app.signup_window = None
        self.app.open_login_window()

    def on_close(self):
        """Function to close this window."""
        self.app.signup_window = None
        self.master.destroy()


class NewWindow:
    def __init__(self, master, user_info):
        self.master=master
        master.title("New Window")
        master.geometry("1200x700")
        master.resizable(False, False)
        master.configure(background="lemon chiffon")

        # Save user_info to this class.
        self.user_info = user_info

        tk.Label(master, text="Testing visibility in new window").place(x=200, y=300)

        # Create a coloured box for the top where navigation bar will be.
        canvas=Canvas(master,
                        height=70,
                        width=1210,
                        bg="black")
        canvas.place(x=0, y=0)

        # Buttons to switch between frames.
        nav_buttons=[
            ("Home", "HomePage"),
            ("About", "AboutPage"),
            ("Quiz", "QuizPage"),
            ("Test", "TestPage"),
            ("Help", "HelpPage"),
            ("Profile", "ProfilePage")
        ]

        # Create exit button and place it.
        exit_btn=tk.Button(master, text="Exit", width=11, height=2,
                             font=("Helvetica", 10, "bold"), command=self.checkexit)
        exit_btn.place(x=1080, y=15)

        # Iterate through the list to create and place buttons.
        for i, (label, frame_name) in enumerate(nav_buttons):
            btn=tk.Button(master, text=label, command=lambda f=frame_name: self.show_frame(f), width=11, height=2,
                            font=("Helvetica", 10, "bold"))
            btn.place(x=50+i*115, y=15)

        # Container to hold all content frames
        container=tk.Frame(master, width = 700, height = 800)
        container.place(x=0, y=70, width=1200, height=630)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.container=container

        self.frames={}

        for F in (HomePage, AboutPage, QuizPage, TestPage, ProfilePage, HelpPage):
            page_name=F.__name__
            # Pass user_info to profile page.
            if page_name == "ProfilePage" or page_name=="QuizPage" or page_name=="TestPage":
                frame = F(master=container, controller=self, user_info=self.user_info, new_window=self.master)
            else:
                frame=F(master=container, controller=self)

            self.frames[page_name]=frame
            frame.configure(bg = "lemon chiffon")
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame=self.frames[page_name]
        frame.tkraise()

    def checkexit(self):
        """Function to confirm user wants to exit application."""
        response=mb.askquestion("Exit Programme?","Your "
                                              + "progress will NOT be saved."
                                              + "\nAre you sure you want to "
                                              + "exit the program?",
                                            icon='warning', master=self.master)
        if response == "yes":
            self.master.destroy()


class HomePage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        
        label=tk.Label(self, text="This is Home", font=("Arial", 16))
        label.pack(pady=20)

        # Display labels for title and substitle.
        program_title=tk.Label(self,
                                 text="KiwiDrive",
                                 font=("Helvetica", 100, "bold"),
                                 fg="gold",
                                 bg="lemon chiffon")
        program_title.place(x=100, y=200)

        sub_title=tk.Label(self, 
                             text="Learn. Quiz. Test.", 
                             font=("Helvetica", 20),
                             bg="lemon chiffon")
        sub_title.place(x=100, y=370)

        # Create image.
        image=Image.open("yellow_road_image.png")
        resize_image=image.resize((400, 400))
        img=ImageTk.PhotoImage(resize_image)
        road_image=tk.Label(image=img, bd=0, highlightthickness=0)
        road_image.image=img
        road_image.place(x=750, y=200)

        # Create dots for the letter I. To look like a traffic light.
        dots=[(193, 'red'), (335, 'goldenrod1'), (522, 'green')]
        for x, color in dots:
            canvas=tk.Canvas(self, width=50, height=50, bg="lemon chiffon", bd=0, highlightthickness=0)
            canvas.place(x=x, y=202)
            canvas.create_oval(15, 15, 35, 35, fill=color, outline='')


class AboutPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        
        about_title=tk.Label(self, text="About", font=("Helvetica", 42), bg="lemon chiffon")
        about_title.place(x=50, y=50)


class QuizPage(tk.Frame):
    def __init__(self, master, controller=None, user_info=None, new_window=None):
        super().__init__(master)
        quiz_title=tk.Label(self, text="Quiz", font=("Helvetica", 42), bg="lemon chiffon")
        quiz_title.place(x=50, y=50)

        self.new_window = new_window
        self.controller = controller
        self.user_info = user_info or {}
        
        intro_lbl=tk.Label(self, 
                           text="In quiz mode, there are a total of 3 "
                           "quizzes to choose from, as seen below. \nAll of "
                           "which consist of 10 - 15 questions with multiple "
                           "choice answers. \nA correct answer will be "
                           "indicated by a green tick. An incorrect answer "
                           "\nis indicated by a red dot. \n\nDURING: As the "
                           "questions are answered, you will be provided with "
                           "the correct \nanswer as a response. Please read "
                           "the response to improve your understanding. "
                           "\n\nAFTER: Once the quiz is completed, you will "
                           "be provided with insights of the number of "
                           "\nquestions answered correctly/incorrectly and a "
                           "percentage will be calculated.  \nFeel free to "
                           "try more quizzes or test how much you know!", 
                           bg="lemon chiffon", 
                           justify="left", 
                           font=("ariel", 11))
        intro_lbl.place(x=50, y=150)

        # Create buttons for different quiz options.
        theory_btn=tk.Button(self, text="Theory", command=self.choose_theory)
        behaviour_btn=tk.Button(self, text="Behaviour", command=self.choose_behaviour)
        emergency_btn=tk.Button(self, text="Emergency", command=self.choose_emergency)

        # Place buttons.
        theory_btn.place(x=700, y=200)
        behaviour_btn.place(x=700, y=400)
        emergency_btn.place(x=900, y=200)

        # # Create images for the button icons.
        # image=Image.open("theory_image_1.webp")
        # resize_image=image.resize((400, 400))
        # img=ImageTk.PhotoImage(resize_image)
        # road_image=tk.Label(image=img, bd=0, highlightthickness=0)
        # road_image.image=img
        # road_image.place(x=750, y=200)

    def choose_theory(self):
        self.chosen_quiz = 'theory_quiz.json'
        self.open_quiz(self.chosen_quiz, self.user_info)
    
    def choose_behaviour(self):
        self.chosen_quiz = 'behaviour_quiz.json'
        self.open_quiz(self.chosen_quiz, self.user_info)

    def choose_emergency(self):
        self.chosen_quiz = 'emergency_quiz.json'
        self.open_quiz(self.chosen_quiz, self.user_info)

    def get_chosen_quiz(self):
        return self.chosen_quiz
    
    def open_quiz(self, chosen_quiz, user_info):
        # Get the data from the json file.
        with open(chosen_quiz) as f:
            data = json.load(f)

        # Set the question, options, and answer.
        self.question = (data['question'])
        self.options = (data['options'])
        self.answer = (data[ 'answer'])
        self.feedback = (data[ 'feedback'])

        # Create the top level quiz window.
        Quiz(self.master, (self.question, self.options, self.answer, self.feedback), chosen_quiz, user_info)

    def get_quiz_data(self):
        """Function to get the quiz data for generation."""
        return self.question, self.options, self.answer, self.feedback
    
class Quiz(tk.Toplevel):
    """Class to define the components of the self."""
    def __init__(self, master, quiz_data, chosen_quiz, user_info):
        super().__init__(master)
        """Function called when new object of class is intitialised. Set 
        question count to 0 and initilise all other functions for content."""
        self.geometry("800x450")
        # Extract quiz name from file path of chosen quiz.
        quiz_name = chosen_quiz.split("_quiz.json")[0]
        self.title(f"{quiz_name} quiz")

        # Saving external variables to this class to use across functions.
        self.question, self.options, self.answer, self.feedback = quiz_data
        self.user_info = user_info
        self.quiz_name = quiz_name

        # set question number to 0
        self.q_no=0
        # Hold an integer value to select an option in a question.
        self.opt_selected = tk.IntVar(self, value=0)
        # Set options to zero.
        self.opt_selected.set(0)
        # Use radio button to display current question and display options.
        self.opts=self.radio_buttons()
        # display current question options, buttons, title, and display questions.
        title = Label(self, text=f"{quiz_name} quiz",
        width=50, bg="black", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)
        # Create a label for answer indication. Will be used in next_btn().
        self.answer_lbl=Label(self, text="", font=("ariel", 20, "bold"))
        self.answer_lbl.place(x=520,y=380)

        # Display buttons and labels.
        next_button = Button(self, text="Next",command=self.next_btn,
        width=10,bg="gold", font=("ariel", 16, "bold"))
        self.exit_button = Button(self, text="Exit", command=self.checkexit,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
        self.q_no_label = Label(self, text="", width=60,
                        font=('ariel', 16, 'bold'),
                        anchor='w', justify=LEFT)

        # Function.
        self.display_options(self.options)
        self.display_question(self.question)

        # Place buttons/labels.
        next_button.place(x=350,y=400)
        self.exit_button.place(x=700,y=50)
        self.q_no_label.place(x=70, y=80)

        # Ensure the button stays on top of the question label.
        self.exit_button.lift()
        
        # no of questions
        self.data_size=len(self.question)
        
        # keep a counter of correct answers
        self.correct=0

    def display_result(self, user_info):
        """Function to calculate, display, and save user results."""
        # Calculate how many questions user answered incorrectly.
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        
        # calcultaes the percentage of correct answers.
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        
        mb.showinfo("Quiz complete!\nResult", f"{result}\n{correct}\n{wrong}", parent=self)

        # Save users results to their file.
        today=datetime.today()
        formatted_date = today.strftime("%d/%m/%Y %H:%M")
        quiz_results=(
            f"\n{self.quiz_name} Quiz results ({formatted_date}):\n"
            f"Score: {score}\n"
            f"{correct}\n"
            f"{wrong}"
        )

        # Get username.
        username=user_info.get('Username', '')
        with open(f"{username}_info.txt", "a") as file:
                        file.write(f"\n{quiz_results}\n")

    def check_ans(self, q_no, answer):
        """Function to check the answer after user has clicked next."""
        # Check if selected option is correct.
        if self.opt_selected.get() == answer[q_no]:
            return self.opt_selected.get() == answer[q_no]
        
    def display_options(self, options):
        """Function to reset question options for next question."""
        val=0
        # Deselect options.
        self.opt_selected.set(0)
        # Ensure the question label doesn't cover the button.
        self.exit_button.lift()
        
        # Loop over options to display for radio button text.
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
        
    def display_question(self, question):
            """Function to update the question label."""
            self.q_no_label.config(text=question[self.q_no])

    def next_btn(self):
        """Function to check if the answer is correct, then increase question count by 1."""
        
        if self.opt_selected.get() >=1:
            # Check if the answer is correct, then increment correct by 1.
            if self.check_ans(self.q_no, self.answer):
                self.correct += 1
                self.answer_lbl.config(text="Correct!", fg="green")

            else:
                self.answer_lbl.config(text="Incorrect", fg="red")
                self.display_feedback(self.feedback)
            
            # Moves to next Question by incrementing the q_no counter
            self.q_no += 1
            
            # checks if the q_no size is equal to the data size
            if self.q_no==self.data_size:
                
                # if it is correct then it displays the score
                self.display_result(self.user_info)
                # destroys the self
                self.destroy()
            else:
                # shows the next question
                self.display_question(self.question)
                self.display_options(self.options)
                # Clear answer indication.
                self.after(700, lambda: self.answer_lbl.config(text=""))
        else:
            mb.showerror("Invalid input", "Please select an option.", parent=self)

    def display_feedback(self, feedback):
        """Function to display feedback when user answers incorrectly."""
        feedback_txt=feedback[self.q_no]
        mb.showinfo("Feedback", feedback_txt, parent=self)

    # This method shows the radio buttons to select the Question
    # on the screen at the specified position. It also returns a
    # list of radio button which are later used to add the options to
    # them.
    def radio_buttons(self):
        
        # initialize the list with an empty list of options and position first option.
        q_list = []
        y_pos = 160

        # adding the options to the list
        while len(q_list) < 4:
            
            # setting the radio button properties
            radio_btn = Radiobutton(self, text="", variable=self.opt_selected,
            value = len(q_list)+1, font = ("ariel",14), justify=LEFT)
            
            # Add button to the list then place it.
            q_list.append(radio_btn)
            radio_btn.place(x = 100, y = y_pos)
            
            # incrementing the y-axis position by 40
            y_pos += 52
        
        # return the radio buttons
        return q_list
    
    def checkexit(self):
        """Function to confirm user wants to exit quiz."""
        response=mb.askquestion("Exit Quiz?","Your "
                                              + "progress will NOT be saved."
                                              + "\nAre you sure you want to "
                                              + "exit the quiz?",
                                            icon='warning', parent=self)
        if response == "yes":
            self.destroy()


class TestPage(tk.Frame):
    def __init__(self, master, controller=None, user_info=None, new_window=None):
        super().__init__(master)
        test_title=tk.Label(self, text="Test", font=("Helvetica", 42), bg="lemon chiffon")
        test_title.place(x=50, y=50)
        
        self.new_window = new_window
        self.controller = controller
        self.user_info = user_info or {}

        intro_lbl=tk.Label(self, 
                           text="In test mode, there are a total of 25 "
                           "quizzes which you are tested on. \nThese cover "
                           "general road safety test questoins. Test "
                           "conditions apply. \nMeaning there is no "
                           "feedback provided and there is no indication "
                           "\nof correct/incorrect answers until completion. "
                           "\n\nBENEFITS:\n- Reinforce learning through "
                           "quizzes\n- Gain confidence in road safety "
                           "knowledge\n- Measure your progress"
                           "\n\nAFTER: Once the test is completed, you will "
                           "be provided with insights of the number of "
                           "\nquestions answered correctly/incorrectly and a "
                           "percentage will be calculated. \nFeel free to "
                           "try again and improve your score or "
                           "learn more through quizzes!",
                           bg="lemon chiffon", 
                           justify="left",
                           font=("ariel", 11))
        intro_lbl.place(x=50, y=150)

        # Create buttons for different quiz options.
        test_btn=tk.Button(self, text="Start now", command=self.choose_test)

        # Place buttons.
        test_btn.place(x=700, y=200)

    def choose_test(self):
        self.chosen_test = 'test.json'
        self.open_test(self.chosen_test, self.user_info)

    def open_test(self, chosen_test, user_info):
        # Get the data from the json file.
        with open(chosen_test) as f:
            data = json.load(f)

        # Set the question, options, and answer.
        self.question = (data['question'])
        self.options = (data['options'])
        self.answer = (data[ 'answer'])

        # Create the top level quiz window.
        Test(self.master, (self.question, self.options, self.answer), user_info)

    def get_test_data(self):
        """Function to get the quiz data for generation."""
        return self.question, self.options, self.answer


class Test(tk.Toplevel):
    """Class to define the components of the self."""
    def __init__(self, master, test_data, user_info):
        super().__init__(master)
        """Function called when new object of class is intitialised. Set 
        question count to 0 and initilise all other functions for content."""
        self.geometry("800x450")
        self.title("Test")

        # Saving external variables to this class to use across functions.
        self.question, self.options, self.answer = test_data
        self.user_info = user_info

        # set question number to 0.
        self.q_no=0
        # Hold an integer value to select an option in a question.
        self.opt_selected = tk.IntVar(self, value=0)
        # Set options to zero.
        self.opt_selected.set(0)
        # Use radio button to display current question and display options.
        self.opts=self.radio_buttons()
        # display current question options, buttons, title, and display questions.
        title = Label(self, text="Test", width=50, bg="black",fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

        # Display buttons.
        next_button = Button(self, text="Next",command=self.next_btn,
        width=10,bg="gold",font=("ariel",16,"bold"))
        self.exit_button = Button(self, text="Exit", command=self.checkexit,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
        self.q_no_label = Label(self, text="", width=60,
                        font=('ariel', 16, 'bold'),
                        anchor='w', justify=LEFT)

        # Function.
        self.display_options(self.options)
        self.display_question(self.question)

        # Place buttons/labels.
        next_button.place(x=350,y=400)
        self.exit_button.place(x=700,y=50)
        self.q_no_label.place(x=70, y=80)
        # Ensure the question label doesn't cover the button.
        self.exit_button.lift()
        
        # no of questions
        self.data_size=len(self.question)
        
        # keep a counter of correct answers
        self.correct=0

    def display_result(self, user_info):
        """Function to calculate, display, and save user results."""
        # Calculate how many questions user answered incorrectly.
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        
        # calcultaes the percentage of correct answers.
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        
        mb.showinfo("Test complete!\nResult", f"{result}\n{correct}\n{wrong}", parent=self)

        # Save users results to their file.
        today=datetime.today()
        formatted_date = today.strftime("%d/%m/%Y %H:%M")
        test_results=(
            f"\nTest results ({formatted_date}):\n"
            f"Score: {score}\n"
            f"{correct}\n"
            f"{wrong}"
        )

        # Get username.
        username=user_info.get('Username', '')
        with open(f"{username}_info.txt", "a") as file:
                        file.write(f"\n{test_results}\n")

    def check_ans(self, q_no, answer):
        """Function to check the answer after user has clicked next."""
        # Check if selected option is correct.
        if self.opt_selected.get() == answer[q_no]:
            return self.opt_selected.get() == answer[q_no]
        
    def display_options(self, options):
        """Function to reset question options for next question."""
        val=0
        # Deselect options.
        self.opt_selected.set(0)
        # Ensure the question label doesn't cover the button.
        self.exit_button.lift()
        
        # Loop over options to display for radio button text.
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
        
    def display_question(self, question):
            """Function to update the question label."""
            self.q_no_label.config(text=question[self.q_no])

    def next_btn(self):
        """Function to check if the answer is correct, then increase question count by 1."""
        
        if self.opt_selected.get() >=1:
            # Check if the answer is correct, then increment correct by 1.
            if self.check_ans(self.q_no, self.answer):
                self.correct += 1
            
            # Moves to next Question by incrementing the q_no counter
            self.q_no += 1
            
            # checks if the q_no size is equal to the data size
            if self.q_no==self.data_size:
                
                
                # if it is correct then it displays the score
                self.display_result(self.user_info)
                # destroys the self
                self.destroy()
            else:
                # shows the next question
                self.display_question(self.question)
                self.display_options(self.options)
        else:
            mb.showerror("Invalid input", "Please select an option.", parent=self)

    # This method shows the radio buttons to select the Question
    # on the screen at the specified position. It also returns a
    # list of radio button which are later used to add the options to
    # them.
    def radio_buttons(self):
        
        # initialize the list with an empty list of options and position first option.
        q_list = []
        y_pos = 160

        # adding the options to the list
        while len(q_list) < 4:
            
            # setting the radio button properties
            radio_btn = Radiobutton(self, text="", variable=self.opt_selected,
            value = len(q_list)+1, font = ("ariel",14), justify=LEFT)
            
            # Add button to the list then place it.
            q_list.append(radio_btn)
            radio_btn.place(x = 100, y = y_pos)
            
            # incrementing the y-axis position by 40
            y_pos += 52
        
        # return the radio buttons
        return q_list
    
    def checkexit(self):
        """Function to confirm user wants to exit quiz."""
        response=mb.askquestion("Exit Quiz?","Your "
                                              + "progress will NOT be saved."
                                              + "\nAre you sure you want to "
                                              + "exit the quiz?",
                                            icon='warning', parent=self)
        if response == "yes":
            self.destroy()


class ProfilePage(tk.Frame):
    def __init__(self, master, controller=None, user_info=None, new_window=None):
        """Function to initilaise class."""

        def signout():
            """Function to sign the user out and redirect them to the first 
            window.
            """
            response = mb.askquestion("Signout?","Your progress will "
                                                "NOT be saved.\nAre you sure you want "
                                                "to signout?",
            icon = 'warning', master=self.master)
            print(response)
            if response == "yes":
                self.new_window.destroy()
                
        super().__init__(master)
        self.new_window = new_window
        self.controller = controller
        self.user_info = user_info or {}

        profile_title=tk.Label(self, text="Profile", font=("Helvetica", 42), bg="lemon chiffon")
        profile_title.place(x=50, y=50)

        tk.Label(self, text=f"Username: {user_info.get('Username', '')}").pack()
        tk.Label(self, text=f"First name: {user_info.get('First name', '')}").pack()
        tk.Label(self, text=f"Last name: {user_info.get('Last name', '')}").pack()
        tk.Label(self, text=f"Birthdate: {user_info.get('Birthdate', '')}").pack()

        signout_btn = tk.Button(self,
                                text = "Signout",
                                width = 7,
                                height = 1,
                                fg = "black",
                                bg = "firebrick1",
                                command = signout)
        signout_btn.pack()


class HelpPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        
        help_title=tk.Label(self, text="Help", font=("Helvetica", 42), bg="lemon chiffon")
        help_title.place(x=50, y=50)


if __name__ == "__main__":
    root=tk.Tk()
    app=MainWindow(root)
    root.mainloop()