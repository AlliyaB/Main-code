import tkinter as tk
from tkinter import *
from tkinter import messagebox 
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

    def open_login_window(self):
        self.login_window=tk.Toplevel(self.master)
        LoginWindow(self.login_window)

    def open_signup_window(self):
        self.open_signup_window=tk.Toplevel(self.master)
        SignupWindow(self.open_signup_window)

    def checkexit(self):
        """Function to confirm user wants to exit application."""
        response=messagebox.askquestion("Exit Programme?","Your "
                                              + "progress will NOT be saved."
                                              + "\nAre you sure you want to "
                                              + "exit the program?",
                                            icon='warning')
        if response == "yes":
            self.master.destroy()


class LoginWindow:
    def __init__(self, master):
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
                            
                            messagebox.showinfo("Successful", "Log in successful." +
                                        f"\nWelcome back {username}")
                            self.master.destroy()
                            NewWindow(tk.Tk(), user_info)
                        else: 
                            messagebox.showerror("Invalid input", "Incorrect password. Please enter a valid password or signup.")
                else:
                    messagebox.showerror("Invalid input", "Incorrect username. Please enter a valid username or signup.")
            else:
                messagebox.showerror("Invalid input", "There are missing " +
                                    "fields.\nPlease enter all fields.")

        self.master=master
        master.title("Login")
        master.geometry("350x450")
        master.resizable(False, False)
        master.configure(background="lemon chiffon")

        canvas=Canvas(master,
                        height=70,
                        width=350,
                        bg="black")

        # Create labels/buttons for title and user navigation.
        tk.Label(master, text="Log in:", font=("Helvetica", 15), fg="white", bg="black").place(x=10, y=24)
        tk.Label(master, text="Log into your account", font=("Helvetica", 10), fg="white", bg="black").place(x=82, y=30)
        tk.Button(master, text="Sign up", width=11, height=2, font=("Helvetica", 10, "bold"), command=self.open_signup_window).place(x=240, y=15)
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

    def open_signup_window(self):
        self.open_signup_window=tk.Toplevel(self.master)
        SignupWindow(self.open_signup_window)


class SignupWindow:
    def __init__(self, master):
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
                    messagebox.showerror("Invalid first name/last " +
                                        "name", "Please only enter letters " +
                                        "for first name and last name.")
                elif not username.isalnum():
                    messagebox.showerror("Invalid username", "Please only " +
                                        "enter numbers or letters for username.")
                elif os.path.exists(f"{username}_info.txt"):
                    messagebox.showerror("Invalid username", "This username " +
                                         "already exists.\nPlease enter a " +
                                         "different username.")
                elif password != confirm_password:
                    messagebox.showerror("Invalid password", "Please check " +
                                        "that your passwords match.")
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
                        if age <= 0 or age > 99:
                            messagebox.showerror("Invalid input", "Please enter a valid "
                                                "birthdate (dd/mm/yyyy)")
                            return
                        elif age < 15 or age > 24:
                            age_maybe = messagebox.askquestion("Note", "Please note that "
                                                            "this application is "
                                                            "primarily designed for "
                                                            "ages 15-24, and may not "
                                                            "meet your individual "
                                                            "needs.\n\nAre you sure "
                                                            "you want to continue?")
                            if age_maybe == "no":
                                return False
                        else:
                            messagebox.showinfo("Note", "Please enjoy this applications "
                                                "features and resources which are "
                                                "tailored specifically for ages 15-24 "
                                                "like yourself.")
                    except ValueError:
                        # Show an error if the date format is incorrect.
                        messagebox.showerror("Invalid input", "Please enter a valid "
                                            "birthdate (dd/mm/yyyy)")
                        return
                    
                    # Create an individual file for the user.
                    with open(f"{username}_info.txt", "a") as file:
                        file.write(f"\nUsername: {username}\n"
                                   f"First name: {first_name}\n"
                                   f"Last name: {last_name}\n"
                                   f"Password: {password}\n"
                                   f"Birthdate: {birthdate}")
                        
                    #Debugging statment
                    print(age)
                        
                    # Create a dictionary of user info.
                    user_info = {
                                 "Username": username,
                                 "First name": first_name,
                                 "Last name": last_name,
                                 "Birthdate": birthdate
                                 }

                    messagebox.showinfo("Successful", "Sign up successful." +
                                        f"\nWelcome {username}")
                    self.master.destroy()
                    print("DEBUG user_info:", user_info)

                    NewWindow(tk.Tk(), user_info)

            else:
                messagebox.showerror("Invalid input", "Please enter all fields")
                        
        self.master=master
        master.title("Signup")
        master.geometry("350x450")
        master.resizable(False, False)
        master.configure(background="lemon chiffon")

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
        tk.Button(master, text="Log in", width=11, height=2, font=("Helvetica", 10, "bold"), command=self.open_login_window).place(x=240, y=15)
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

    def open_login_window(self):
        self.login_window=tk.Toplevel(self.master)
        LoginWindow(self.login_window)


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
            if page_name == "ProfilePage":
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
        response=messagebox.askquestion("Exit Programme?","Your "
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
        label=tk.Label(self, text="This is About", font=("Helvetica", 16))
        label.pack(pady=20)


class QuizPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        quiz_title=tk.Label(self, text="Quiz", font=("Helvetica", 42), bg="lemon chiffon")
        quiz_title.place(x=50, y=50)
        
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
                           justify="left")
        intro_lbl.place(x=50, y=150)

        # Create buttons for different quiz options.
        theory_btn=tk.Button(self, text="Theory", command=self.open_quiz)
        behaviour_btn=tk.Button(self, text="Behaviour")
        emergency_btn=tk.Button(self, text="Emergency")

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
    
    def open_quiz(self):
            self.open_quiz=tk.Toplevel(self.master)
            Quiz(self.open_quiz)


class Quiz:
    # This is the first method which is called when a
    # new object of the class is initialized. This method
    # sets the question count to 0. and initialize all the
    # other methoods to display the content and make all the
    # functionalities available
    def __init__(self, master):
        super().__init__(master)
        # set question number to 0
        self.q_no=0
        
        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_question()
        
        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected=IntVar()
        
        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts=self.radio_buttons()
        
        # display options for the current question
        self.display_options()
        
        # displays the button for next and exit.
        self.buttons()
        
        # no of questions
        self.data_size=len(question)
        
        # keep a counter of correct answers
        self.correct=0


    # This method is used to display the result
    # It counts the number of correct and wrong answers
    # and then display them at the end as a message Box
    def display_result(self):
        
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        
        # Shows a message box to display the result
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):
        
        # checks for if the selected option is correct
        if self.opt_selected.get() == answer[q_no]:
            # if the option is correct it return true
            return True

    # This method is used to check the answer of the
    # current question by calling the check_ans and question no.
    # if the question is correct it increases the count by 1
    # and then increase the question number by 1. If it is last
    # question then it calls display result to show the message box.
    # otherwise shows next question.
    def next_btn(self):
        
        # Check if the answer is correct
        if self.check_ans(self.q_no):
            
            # if the answer is correct it increments the correct by 1
            self.correct += 1
        
        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1
        
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
            
            # if it is correct then it displays the score
            self.display_result()
            
            # destroys the self
            self.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()


    # This method shows the two buttons on the screen.
    # The first one is the next_button which moves to next question
    # It has properties like what text it shows the functionality,
    # size, color, and property of text displayed on button. Then it
    # mentions where to place the button on the screen. The second
    # button is the exit button which is used to close the self without
    # completing the quiz.
    def buttons(self):
        
        # The first button is the Next button to move to the
        # next Question
        next_button = Button(self, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        
        # placing the button  on the screen
        next_button.place(x=350,y=380)
        
        # This is the second button which is used to Quit the self
        quit_button = Button(self, text="Quit", command=self.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
        
        # placing the Quit button on the screen
        quit_button.place(x=700,y=50)


    # This method deselect the radio button on the screen
    # Then it is used to display the options available for the current
    # question which we obtain through the question number and Updates
    # each of the options for the current question of the radio button.
    def display_options(self):
        val=0
        
        # deselecting the options
        self.opt_selected.set(0)
        
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1


    # This method shows the current Question on the screen
    def display_question(self):
        
        # setting the Question properties
        q_no = Label(self, text=question[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        
        #placing the option on the screen
        q_no.place(x=70, y=100)


    # This method is used to Display Title
    def display_title(self):
        
        # The title to be shown
        title = Label(self, text="GeeksforGeeks QUIZ",
        width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
        
        # place of the title
        title.place(x=0, y=2)


    # This method shows the radio buttons to select the Question
    # on the screen at the specified position. It also returns a
    # list of radio button which are later used to add the options to
    # them.
    def radio_buttons(self):
        
        # initialize the list with an empty list of options
        q_list = []
        
        # position of the first option
        y_pos = 150
        
        # adding the options to the list
        while len(q_list) < 4:
            
            # setting the radio button properties
            radio_btn = Radiobutton(self,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14))
            
            # adding the button to the list
            q_list.append(radio_btn)
            
            # placing the button
            radio_btn.place(x = 100, y = y_pos)
            
            # incrementing the y-axis position by 40
            y_pos += 40
        
        # return the radio buttons
        return q_list


class TestPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        label=tk.Label(self, text="This is Test", font=("Arial", 16))
        label.pack(pady=20)


class ProfilePage(tk.Frame):
    def __init__(self, master, controller=None, user_info=None, new_window=None):
        """Function to initilaise class."""

        def signout():
            """Function to sign the user out and redirect them to the first 
            window.
            """
            response = messagebox.askquestion("Signout?","Your progress will "
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

        label=tk.Label(self, text="This is Profile", font=("Arial", 16))
        label.pack(pady=20)

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
        label=tk.Label(self, text="This is Help", font=("Arial", 16))
        label.pack(pady=20)


if __name__ == "__main__":
    root=tk.Tk()
    app=MainWindow(root)
    root.mainloop()