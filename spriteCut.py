import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os
def submit():
    try:
        row_val = int(row_entry.get())
        col_val = int(col_entry.get())
        tot_row_val = int(tot_row_entry.get())
        tot_col_val = int(tot_col_entry.get())
        print("Row:", row_val)
        print("Column:", col_val)
        print("Selected File:", selected_file)

        im = Image.open(selected_file, 'r')

        # Size of the image in pixels (size of original image)
        width, height = im.size
        print("width:", width)
        print("height:", height)

        # Setting the points for cropped image
        sprite_width = width / tot_col_val
        sprite_height = height / tot_row_val 
        left = sprite_width * (col_val - 1)
        top = sprite_height * (row_val - 1)
        right = width  # Right coordinate is the width of the image
        bottom = top + sprite_height
        print(sprite_height,sprite_width,left,right,bottom, top)
        # Cropped image of above dimension
        im1 = im.crop((left, top, right, bottom))

        # Shows the image in image viewer
        im1.show()
        output_file = "cropped_sprite.png"  # You can change the filename as needed
        output_path = os.path.join(os.getcwd(), output_file)
        im1.save(output_path)
    except ValueError:
       
        print("Please enter valid integer values for row and column.")
        # assuming file is submited 
        

def browse_file():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=(("jpgs","jpg"),("pngs","png")))
    print("Selected File:", selected_file)

    
window = tk.Tk()
window.title("Sprite Sheet Splitter")

# Row entry
row_label = tk.Label(window, text="Row:")
row_label.grid(row=0, column=0, padx=5, pady=5)
row_entry = tk.Entry(window)
row_entry.grid(row=0, column=1, padx=5, pady=5)

# Column entry
col_label = tk.Label(window, text="Column:")
col_label.grid(row=1, column=0, padx=5, pady=5)
col_entry = tk.Entry(window)
col_entry.grid(row=1, column=1, padx=5, pady=5)

# Row entry
tot_row_label = tk.Label(window, text="Total Rows:")
tot_row_label.grid(row=2, column=0, padx=5, pady=5)
tot_row_entry = tk.Entry(window)
tot_row_entry.grid(row=2, column=1, padx=5, pady=5)

# Column entry
tot_col_label = tk.Label(window, text="Total Columns:")
tot_col_label.grid(row=3, column=0, padx=5, pady=5)
tot_col_entry = tk.Entry(window)
tot_col_entry.grid(row=3, column=1, padx=5, pady=5)

# File selection button
file_button = tk.Button(window, text="Select File", command=browse_file)
file_button.grid(row=4, column=0, columnspan=4, padx=20, pady=5)

# Submit button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=4, column=2, columnspan=4, padx=20, pady=5)

window.mainloop()