import tkinter as tk

from read_data import read_data

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
        cell_size = 20 # default
        header_width = 100
        map_height = 100
        date_height = 80
        time_height = 80

        # Calculate starting y-coordinates
        date_y = map_height
        time_y = map_height + date_height
        events_y = map_height + date_height + time_height

        # Initial grid size
        num_rows = 7
        num_cols = 40
        max_x = header_width + num_cols * cell_size
        max_y = events_y + num_rows * cell_size

        # Main gridlines
        self.canvas.create_line(0, date_y, max_x, date_y, fill="gray") # date
        self.canvas.create_line(0, time_y, max_x, time_y, fill="gray") # time
        self.canvas.create_line(0, events_y, max_x, events_y, fill="gray") # events
        self.canvas.create_line(header_width, 0, header_width, max_y, fill="gray") # header column

        # Create rows
        for i in range(0, num_rows + 1): # +1 to draw the last line
            y = events_y + i * cell_size
            self.canvas.create_line(0, y, max_x, y, fill="gray")
   
        # Create columns
        for i in range(0, num_cols + 1): # +1 to draw the last line
            x = header_width + i * cell_size
            self.canvas.create_line(x, events_y, x, max_y, fill="gray")

        # Fill in headers
        left_padding = 50
        self.canvas.create_text(left_padding, map_height/2, text="Map", fill="white")
        self.canvas.create_text(left_padding, date_y + date_height/2, text="UTC Date", fill="white")
        self.canvas.create_text(left_padding, time_y + time_height/2, text="UTC Time", fill="white")
        
        self.canvas.create_text(left_padding, events_y + cell_size/2, text="Umbra", fill="white")
        self.canvas.create_text(left_padding, events_y + cell_size*1.5, text="Orbital Events", fill="white")

        # Fill in the ground station headers
        gs_names = ["MC3-NPS", "MC3-PCH", "KSAT-PA", "KSAT-PL", "KSAT-NZ"]
        gs_start = events_y + cell_size * 2.5 # .5 to vertically center text
        for i in range(len(gs_names)):
            self.canvas.create_text(left_padding, gs_start + cell_size*i, text=gs_names[i], fill="white")

        # Fill in data
        colors = ["gray", "white", "red", "orange", "yellow", "green", "blue", "purple", "red", "orange"]
        for row in range(num_rows):  # iterate through rows
            cell_color = colors[row]
            for col in range(num_cols):  # iterate through columns
                #cell_color = "white"
                x0 = header_width + col * 20  # Starting x-coordinate for the cell
                y0 = events_y + row * 20  # Starting y-coordinate for the cell
                x1 = x0 + 20  # Ending x-coordinate for the cell
                y1 = y0 + 20  # Ending y-coordinate for the cell
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=cell_color)
        
        # data = read_data('ground_contacts.csv')
        # # for contact in data:
        # #     utc = contact['utc']
        # #     hst = contact['hst']
        # #     gs_id = contact['GS id']
        # #     orbital_events = contact['orbital events']
        # #     self.canvas.create_text(100, 100, text=f"{utc}, {hst}, {gs_id}, {orbital_events}", fill="white")

        # Adjust scroll region based on the actual size of the grid, remove for infinite scroll
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
