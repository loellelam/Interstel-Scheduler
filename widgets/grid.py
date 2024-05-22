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
        header_rowwidth = 100

        self.canvas.create_line(0, 0, 1000, 0, fill="gray", tags="gridline") # top row
        self.canvas.create_line(0, map_height, 1000, map_height, fill="gray", tags="map") # map
        self.canvas.create_line(0, date_colheight, 1000, date_colheight, fill="gray", tags="utc") # date
        self.canvas.create_line(0, time_colheight, 1000, time_colheight, fill="gray", tags="utc") # time
        self.canvas.create_line(header_rowwidth, 0, header_rowwidth, time_colheight+200, fill="gray", tags="header") # header column

        # Create rows
        num_rows = -1
        for i in range(time_colheight, time_colheight+220, 20):
            self.canvas.create_line(0, i, 1000, i, fill="gray", tags="gridline")
            num_rows += 1
        
        # Create columns
        num_cols = 0
        for i in range(header_rowwidth, 1000, 20): 
            self.canvas.create_line(i, time_colheight, i, time_colheight+200, fill="gray", tags="gridline")
            num_cols += 1

        # fill in headers
        left_padding = 50
        self.canvas.create_text(left_padding, map_height/2, text="Map", fill="white")
        self.canvas.create_text(left_padding, (date_colheight/2) + (map_height/2), text="UTC Date", fill="white")
        self.canvas.create_text(left_padding, (time_colheight/2) +(date_colheight/2), text="UTC Time", fill="white")
        
        self.canvas.create_text(left_padding, 10 + time_colheight, text="Umbra", fill="white")
        self.canvas.create_text(left_padding, 30 + time_colheight, text="Orbital Events", fill="white")

        # fill in the ground station headers
        gs_names = ["MC3-NPS", "MC3-PCH", "KSAT-PA", "KSAT-PL", "KSAT-NZ"]
        gs_start = 50 + time_colheight
        gs_rowheight = 20
        for row in range(len(gs_names)):
            self.canvas.create_text(left_padding, gs_start + gs_rowheight*row, text=gs_names[row], fill="white")

        # Fill in data
        colors = ["gray", "white", "red", "orange", "yellow", "green", "blue", "purple", "red", "orange"]
        for row in range(num_rows):  # iterate through rows
            cell_color = colors[row]
            for col in range(num_cols):  # iterate through columns
                #cell_color = "white"
                x0 = header_rowwidth + col * 20  # Starting x-coordinate for the cell
                y0 = time_colheight + row * 20  # Starting y-coordinate for the cell
                x1 = x0 + 20  # Ending x-coordinate for the cell
                y1 = y0 + 20  # Ending y-coordinate for the cell
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=cell_color)
                
        # Adjust scroll region based on the actual size of the grid
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
