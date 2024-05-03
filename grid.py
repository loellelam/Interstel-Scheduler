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
        with open('data.json', 'r') as file:
            data = json.load(file)
        
        # Custom row and column dimensions
        map_height = 100
        date_colheight = map_height + 80
        time_colheight = date_colheight + 80
        label_rowwidth = 80

        self.canvas.create_line(0, 0, 1000, 0, fill="gray", tags="gridline") # top row
        self.canvas.create_line(0, map_height, 1000, map_height, fill="gray", tags="map") # map
        self.canvas.create_line(0, date_colheight, 1000, date_colheight, fill="gray", tags="utc") # date
        self.canvas.create_line(0, time_colheight, 1000, time_colheight, fill="gray", tags="utc") # time
        self.canvas.create_line(label_rowwidth, 0, label_rowwidth, time_colheight+200, fill="gray", tags="label") # label column

        # Create rows
        for i in range(time_colheight, time_colheight+220, 20):
            self.canvas.create_line(0, i, 1000, i, fill="gray", tags="gridline")
        
        # Create columns
        for i in range(label_rowwidth, 1000, 20): 
            self.canvas.create_line(i, time_colheight, i, time_colheight+200, fill="gray", tags="gridline")
            
        # Adjust scroll region based on the actual size of the grid
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

       