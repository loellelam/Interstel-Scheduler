import tkinter as tk
from datetime import datetime, timedelta

from read_json import ReadJson
ReadJson.read_json()

################################################################################
# HELPER FUNCTIONS

# Round down to the nearest 30 minutes
def nearest_30_min(dt):
    return dt - (dt - datetime.min) % timedelta(minutes=30)

# Returns x position given unix time
def unix_to_x_pos(unix):
    dt = datetime.fromtimestamp(unix) # convert unix to datetime
    time_diff = dt - start_time
    x_pos = header_width + (time_diff.total_seconds() / 60) * (cell_size / (time_increment // 5))
    return x_pos

################################################################################
# GLOBAL VARIABLES

# Custom row and column dimensions
cell_size = 20 # default
header_width = 110
map_height = 100
date_height = 90
time_height = 80

# Calculate starting y-coordinates
date_y = map_height
time_y = map_height + date_height
events_y = map_height + date_height + time_height

# save start and end time from json file
start_time = nearest_30_min(datetime.fromtimestamp(ReadJson.get_start_utc()))
end_time = datetime.fromtimestamp(ReadJson.get_end_utc())
time_increment = 30 # 30 minute increments

# Initial grid size
num_rows = 7
num_cols = (int((end_time - start_time).total_seconds() / 60) // 5) + 1 # the number of 5-min increments
max_x = header_width + num_cols * cell_size
max_y = events_y + num_rows * cell_size
################################################################################

class Grid:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, bg="black")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.scrollbar_x = tk.Scrollbar(master, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.canvas.configure(xscrollcommand=self.scrollbar_x.set)

        self.draw_grid()
        self.populate_data()

    def draw_grid(self):
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
        self.canvas.create_text(header_width/2, map_height/2, text="Map", fill="white")
        self.canvas.create_text(header_width/2, date_y + date_height/2, text="UTC Date", fill="white")
        self.canvas.create_text(header_width/2, time_y + time_height/2, text="UTC Time", fill="white")
        
        self.canvas.create_text(header_width/2, events_y + cell_size/2, text="Umbra", fill="white")
        self.canvas.create_text(header_width/2, events_y + cell_size*1.5, text="Orbital Events", fill="white")

        # create empty list for gs names
        name_list = []
        # fill in list with gs names
        gs_names = ReadJson.getEventName(name_list)

        gs_start = events_y + cell_size * 2.5 # .5 to vertically center text
        for i in range(len(gs_names)):
            self.canvas.create_text(header_width/2, gs_start + cell_size*i, text=gs_names[i], fill="white")

        # Fill in data
        # colors = ["gray", "white", "red", "orange", "yellow", "green", "blue", "purple", "red", "orange"]
        # for row in range(num_rows):  # iterate through rows
        #     cell_color = colors[row]
        #     for col in range(num_cols):  # iterate through columns
        #         #cell_color = "white"
        #         x0 = header_width + col * 20  # Starting x-coordinate for the cell
        #         y0 = events_y + row * 20  # Starting y-coordinate for the cell
        #         x1 = x0 + 20  # Ending x-coordinate for the cell
        #         y1 = y0 + 20  # Ending y-coordinate for the cell
        #         self.canvas.create_rectangle(x0, y0, x1, y1, fill=cell_color)
        
        # Adjust scroll region based on the actual size of the grid, remove for infinite scroll
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def populate_data(self):
        # Populate UTC Date and Time
        self.canvas.create_text(header_width, date_y + date_height/2, text=start_time.strftime('%Y-%m-%d'), fill="white", angle=90) # first date
        # Label every 30 minute increment
        time_counter = start_time
        for i in range(0, max_x//cell_size, time_increment//5):
            self.canvas.create_text(header_width + i*cell_size, time_y + time_height/2, text=time_counter.strftime('%H:%M:%S'), fill="white", angle=90) 
            # Label every new day
            if time_counter.time() == datetime.min.time():  # if time is 00:00
                self.canvas.create_text(header_width + i * cell_size, date_y + date_height / 2, text=time_counter.strftime('%Y-%m-%d'), fill="white", angle=90)
            time_counter = time_counter + timedelta(minutes=time_increment)
       
        # Populate umbra events
        umbra_times = ReadJson.get_umbra_utc()
        for i in range(0, len(umbra_times["in"])):
            start = unix_to_x_pos(umbra_times["in"][i])
            end = unix_to_x_pos(umbra_times["out"][i])
            self.canvas.create_rectangle(start + 1, events_y + 1, end - 1, events_y + cell_size - 1, fill="gray")