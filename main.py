import tkinter as tk

from widgets.grid import Grid

def main():
    # Initialize Tk class
    root = tk.Tk()
    root.title("Scheduler")
    root.geometry("800x600") # window size

    # Add widgets
    grid = Grid(root)

    l1 = tk.Label(root, text = "Test: ")
    # l1.grid(row = 1, column = 0)

    # Display program
    root.mainloop()

if __name__ == "__main__":
    main()
