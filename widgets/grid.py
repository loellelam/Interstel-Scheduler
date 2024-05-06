import tkinter as tk

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
        # Custom row and column dimensions
        map_height = 100
        date_colheight = map_height + 80
        time_colheight = date_colheight + 80
        label_rowwidth = 80

        self.canvas.create_line(0, 0, 1000, 0, fill="gray", tags="gridline") # top row
        self.canvas.create_line(0, map_height, 1000, map_height, fill="gray", tags="map") # map
        self.canvas.create_line(0, date_colheight, 1000, date_colheight, fill="gray", tags="utc") # date
        self.canvas.create_line(0, time_colheight, 1000, time_colheight, fill="gray", tags="utc") # time
        self.canvas.create_line(label_rowwidth, 0, label_rowwidth, time_colheight+200, fill="gray", tags="label") # header column

        # Create rows
        for i in range(time_colheight, time_colheight+220, 20):
            self.canvas.create_line(0, i, 1000, i, fill="gray", tags="gridline")
        
        # Create columns
        for i in range(label_rowwidth, 1000, 20): 
            self.canvas.create_line(i, time_colheight, i, time_colheight+200, fill="gray", tags="gridline")

        cell_data = f"Map"
        self.canvas.create_text(40, map_height/2, text=cell_data, fill="white")
        self.canvas.create_text(40, (date_colheight/2) + (map_height/2), text="UTC Date", fill="white")
        self.canvas.create_text(40, (time_colheight/2) +(date_colheight/2), text="UTC Time", fill="white")

        # Fill in data
        for row in range(5):  # Example: 5 rows
            for col in range(5):  # Example: 5 columns
                cell_color = "white"
                x0 = label_rowwidth + col * 20  # Starting x-coordinate for the cell
                y0 = time_colheight + row * 20  # Starting y-coordinate for the cell
                x1 = x0 + 20  # Ending x-coordinate for the cell
                y1 = y0 + 20  # Ending y-coordinate for the cell
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=cell_color)
                
        # Adjust scroll region based on the actual size of the grid
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
