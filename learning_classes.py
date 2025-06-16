import tkinter as tk

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Main Window")

        self.button = tk.Button(master, text="Open New Window", command=self.open_new_window)
        self.button.pack()

    def open_new_window(self):
        self.new_window = tk.Toplevel(self.master)
        NewWindow(self.new_window)

class NewWindow:
    def __init__(self, master):
        self.master = master
        master.title("New Window")

        self.label = tk.Label(master, text="This is a new window")
        self.label.pack()

# root = tk.Tk()
# main_window = MainWindow(root)
# root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()