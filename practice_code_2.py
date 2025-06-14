import tkinter as tk
from tkinter import *
from tkinter import messagebox 
"""Creates and modifies images."""
from PIL import ImageTk

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Main Window")
        master.geometry("1200x700")
        master.resizable(False, False)
        master.configure(background="lemon chiffon")

        self.button = tk.Button(master, text="Open New Window", command=self.open_new_window)
        self.button.place(x=700, y=300)
        
         # Display labels for title and substitle.
        program_title = tk.Label(master,
                                 text="KiwiDrive",
                                 font=("Helvetica", 100, "bold"),
                                 fg="gold",
                                 bg="lemon chiffon")
        program_title.place(x=100, y=200)

        sub_title = tk.Label(master, 
                             text="Learn. Quiz. Test.", 
                             font=("Helvetica", 20),
                             bg="lemon chiffon")
        sub_title.place(x=100, y=370)

        # Create canvas to design dots for aesthetics.
        red_canvas = tk.Canvas(master, width=50, height=50, bg="lemon chiffon")
        red_canvas.place(x = 193, y=202)

        gold_canvas = tk.Canvas(master, width=50, height=50, bg="lemon chiffon")
        gold_canvas.place(x = 335, y=202)

        green_canvas = tk.Canvas(master, width=50, height=50, bg="lemon chiffon")
        green_canvas.place(x = 522, y=202)

        # Draw coloured dots that is a filled circle.
        red_canvas.create_oval(15, 15, 35, 35, fill='red', outline='')
        gold_canvas.create_oval(15, 15, 35, 35, fill='goldenrod1', outline='')
        green_canvas.create_oval(15, 15, 35, 35, fill='green', outline='')

        # Create a coloured box for the top where navigation bar will be.
        canvas = Canvas(master,
                        height = 70,
                        width = 1210,
                        bg = "black")
        canvas.place(x = 0, y = 0)

        # Create Sign up, log in, and exit buttons.
        login_btn = tk.Button(master, text = "Log in", width=11, height=2,
                             font=("Helvetica", 10, "bold"), command = self.open_login_window)
        signup_btn = tk.Button(master, text = "Sign up", width=11, height=2,
                             font=("Helvetica", 10, "bold"), command = self.open_master)
        exit_btn = tk.Button(master, text = "Exit", width=11, height=2,
                             font=("Helvetica", 10, "bold"), command = self.checkexit)
        
        # Place signup, login, and exit buttons.
        login_btn.place(x = 830, y = 15)
        signup_btn.place(x = 940, y = 15)
        exit_btn.place(x = 1080, y = 15)

    def open_new_window(self):
        self.new_window = tk.Toplevel(self.master)
        NewWindow(self.new_window)

    def open_login_window(self):
        self.login_window = tk.Toplevel(self.master)
        LoginWindow(self.login_window)

    def open_master(self):
        self.master = tk.Toplevel(self.master)
        SignupWindow(self.master)

    def checkexit(self):
        """Function to confirm user wants to exit application."""
        response = messagebox.askquestion("Exit Programme?","Your "
                                              + "progress will NOT be saved."
                                              + "\nAre you sure you want to "
                                              + "exit the program?",
                                            icon = 'warning')
        if response == "yes":
            self.master.destroy()


class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Login Window")
        master.geometry("300x350")
        master.resizable(False, False)


class SignupWindow:
    def __init__(self, master):
        self.master = master
        master.title("Signup Window")
        master.geometry("300x350")
        master.resizable(False, False)

        # Declaring name and password as string variables.
        fields = ["First name", "Last name", "Username", "Password", "Confirm\nPassword", "Birthdate"]
        vars = {field: tk.StringVar() for field in fields}

        # Declaring name and password as string variables.
        first_name_var = tk.StringVar()
        last_name_var = tk.StringVar()
        username_var = tk.StringVar()
        password_var = tk.StringVar()
        confirm_password_var = tk.StringVar()

        # Entrys.
        first_name_entry = tk.Entry(master,
                                    textvariable = first_name_var)
        last_name_entry = tk.Entry(master,
                                textvariable = last_name_var)
        username_entry = tk.Entry(master,
                                textvariable = username_var)
        password_entry=tk.Entry(master,
                                textvariable = password_var,
                                show = "*")
        confirm_password_entry=tk.Entry(master,
                                        textvariable = confirm_password_var,
                                        show = "*")
        
        first_name_entry.place(x = 100, y = 120)
        last_name_entry.place(x = 100, y = 160)
        username_entry.place(x = 100, y = 200)
        password_entry.place(x = 100, y = 240)
        confirm_password_entry.place(x = 100, y = 280)

        # Create labels/buttons for title and user navigation.
        tk.Label(master, text="Sign up:", font=("Helvetica", 15)).place(x=10, y=25)
        tk.Label(master, text="Create an account", font=("Helvetica", 10)).place(x=82, y=30)
        tk.Button(master, text = "Log in", width=11, height=2, font=("Helvetica", 10, "bold"), command = self.open_login_window).place(x=200, y=15)

        # Loop for labels and entries
        for i, field in enumerate(fields):
            y = 80 + i * 40
            tk.Label(master, text=field + ":", font=("Helvetica", 10, "bold")).place(x=20, y=y)
            # tk.Entry(master, textvariable=vars[field], show="*" if "Password" in field else "").place(x=100, y=y)

        # Signup button
        tk.Button(master, text="Sign up", width=7, height=1, fg="black", bg="gold", command = self.signup).place(x=120, y=315)

    def signup(self):
        first_name = first_name_var.get()
        last_name = last_name_var.get()
        username = username_var.get()
        password = password_var.get()
        confirm_password = confirm_password_var.get()

        print("First name: " + first_name)
        print("Last name: " + last_name)
        print("Username: " + username)
        print("Password: " + password)
        print("Confirm password: " + confirm_password)
        

    def open_login_window(self):
        self.login_window = tk.Toplevel(self.master)
        LoginWindow(self.login_window)

        # Declaring username and password as string variables.
        username_var = tk.StringVar()
        password_var = tk.StringVar()


class NewWindow:
    def __init__(self, master):
        self.master = master
        master.title("New Window")
        master.geometry("1200x700")

        self.label = tk.Label(master, text="This is a new window")
        self.label.pack()

        # Display label.
        program_title = tk.Label(master,
            text = "NZ Road safety Education",
            font = ("Helvetica", 18))
        program_title.place(x = 200, y = 250)

        # Create a coloured box for the top where navigation bar will be.
        canvas = Canvas(master,
                        height = 70,
                        width = 1210,
                        bg = "black")
        canvas.place(x = 0, y = 0)

        # Buttons to switch between frames.
        nav_buttons = [
            ("Home", "HomePage"),
            ("About", "AboutPage"),
            ("Quiz", "QuizPage"),
            ("Test", "TestPage"),
            ("Help", "HelpPage"),
            ("Profile", "ProfilePage")
        ]

        # Create exit button and place it.
        exit_btn = tk.Button(master, text = "Exit", width=11, height=2,
                             font=("Helvetica", 10, "bold"), command = self.checkexit)
        exit_btn.place(x = 1080, y = 15)

        # Iterate through the list to create and place buttons.
        for i, (label, frame_name) in enumerate(nav_buttons):
            btn = tk.Button(master, text=label, command=lambda f=frame_name: self.show_frame(f), width=11, height=2,
                            font=("Helvetica", 10, "bold"))
            btn.place(x=50+i*115, y=15)

        # Container to hold all content frames
        container = tk.Frame(master)
        container.place(x=0, y=70, width=1200, height=630)
        self.container = container

        self.frames = {}

        for F in (HomePage, AboutPage, QuizPage, TestPage, ProfilePage, HelpPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def checkexit(self):
        """Function to confirm user wants to exit application."""
        response = messagebox.askquestion("Exit Programme?","Your "
                                              + "progress will NOT be saved."
                                              + "\nAre you sure you want to "
                                              + "exit the program?",
                                            icon = 'warning', parent = self.master)
        if response == "yes":
            self.master.destroy()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is Home", font=("Arial", 16))
        label.pack(pady=20)


class AboutPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is About", font=("Arial", 16))
        label.pack(pady=20)

class QuizPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is Quiz", font=("Arial", 16))
        label.pack(pady=20)

class TestPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is Test", font=("Arial", 16))
        label.pack(pady=20)

class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is Profile", font=("Arial", 16))
        label.pack(pady=20)

class HelpPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is Help", font=("Arial", 16))
        label.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()