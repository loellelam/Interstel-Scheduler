import tkinter as tk

from grid import Grid

def main():
    # Initialize Tk class
    root = tk.Tk()
    root.title("Scheduler")
    root.geometry("800x300")

    # Add grid widget
    app = Grid(root)

    # Display program
    root.mainloop()

if __name__ == "__main__":
    main()
