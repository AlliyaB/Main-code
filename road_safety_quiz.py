import tkinter as tk
from tkinter import *
from tkinter import messagebox 

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Main Window")
        master.geometry("1200x700")
        master.resizable(False, False)

        self.button = tk.Button(master, text="Open New Window", command=self.open_new_window)
        self.button.place(x=700, y=300)
        
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

        # Create Sign up, log in, and exit buttons.
        login_btn = tk.Button(master, text = "Log in", width=11, height=2,
                             font=("Helvetica", 10, "bold"))
        signup_btn = tk.Button(master, text = "Sign up", width=11, height=2,
                             font=("Helvetica", 10, "bold"))
        exit_btn = tk.Button(master, text = "Exit", width=11, height=2,
                             font=("Helvetica", 10, "bold"), command = self.checkexit)
        
        # Place signup, login, and exit buttons.
        login_btn.place(x = 830, y = 15)
        signup_btn.place(x = 940, y = 15)
        exit_btn.place(x = 1080, y = 15)

    def open_new_window(self):
        self.new_window = tk.Toplevel(self.master)
        NewWindow(self.new_window)

    def checkexit(self):
        """Function to confirm user wants to exit application."""
        response = messagebox.askquestion("Exit Programme?","Your "
                                              + "progress will NOT be saved."
                                              + "\nAre you sure you want to "
                                              + "exit the program?",
                                            icon = 'warning')
        if response == "yes":
            self.master.destroy()


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