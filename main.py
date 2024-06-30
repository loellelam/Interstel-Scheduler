import tkinter as tk

from widgets.grid import Grid

from read_json import ReadJson

def main():
    # Initialize Tk class
    root = tk.Tk()
    root.title("Scheduler")
    root.geometry("800x600") # window size

    # Add widgets
    grid = Grid(root)

    # Display program
    root.mainloop()

    ##############################TESTING METHOD################################
    # ReadJson.findPairs()

if __name__ == "__main__":
    main()
