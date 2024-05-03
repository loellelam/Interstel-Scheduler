import tkinter as tk
import json

class Grid:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, bg="black")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.scrollbar_x = tk.Scrollbar(master, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.canvas.configure(xscrollcommand=self.scrollbar_x.set)

        self.draw_grid()

    def draw_grid(self):
        # Read data from JSON file
        with open('data.json', 'r') as file:
            data = json.load(file)
        
        # Create rows
        for i in range(0, 220, 20):
            self.canvas.create_line(0, i, 1000, i, fill="gray", tags="gridline")

        
        # Draw grid on the canvas based on the data
        # Example code to draw a grid columns
        header_width = 80
        for i in range(header_width, 1000, 20): 
            self.canvas.create_line(i, 0, i, 200, fill="gray", tags="gridline")
            
        # Adjust scroll region based on the actual size of the grid
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

       