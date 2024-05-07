import tkinter as tk

from widgets.grid import Grid

def main():
    # Initialize Tk class
    root = tk.Tk()
    root.title("Scheduler")
    root.geometry("800x600") # window size

    # Add widgets
    grid = Grid(root)

    # Display program
    root.mainloop()

if __name__ == "__main__":
    main()
