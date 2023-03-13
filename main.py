from PIL import Image, ImageDraw, ImageFont
import subprocess
import os 

def path_finder(folder_name, filename):
    file_location = os.path.join(os.path.dirname(__file__), folder_name,filename)
    return file_location
# Define the font file path
# font_file = "abc.ttf"

import datetime

output_file_name = "output.png"

def days_until_may_7():
    today = datetime.date.today()
    may_7 = datetime.date(today.year, 5, 7)
    if may_7 < today:
        may_7 = datetime.date(today.year + 1, 5, 7)
    days_left = (may_7 - today).days
    day_zero_correction = days_left - 1
    return day_zero_correction

def today_date():
    today = datetime.date.today()
    return today.strftime("%A, %d-%m-%Y")

# Define the text to be written
days_left = str(days_until_may_7())

# Define the font size and weight
font_size = 221
# font_weight = "bold"

# Open the existing image
template_path =  path_finder('.', 'template.png')
image = Image.open(template_path)

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

def draw_line(font_file_name, font_size, x_coordinate_from_centre, y_coordinate_from_centre, color, input_string):
    font = ImageFont.truetype(font_file_name, font_size)

    text_width, text_height = draw.textsize(input_string, font=font)
    x = (image.width - text_width) / 2 + y_coordinate_from_centre
    y = (image.height - text_height) / 2 + x_coordinate_from_centre
    
    draw.text((x, y), str(input_string), font=font, fill=color)
    
    
# DRAW
draw_line(path_finder('.', 'LED-Dot-Matrix.ttf'), 221, -50, 0, "#FFFFFF", days_left)
draw_line(path_finder('.', 'LED-Dot-Matrix.ttf'), 30, 200, 0, "#FFFFFF", f"Today is {today_date()}")

#OUTPUT
image.save(output_file_name)


file_path = f"{os.getcwd()}/{output_file_name}"
command = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", f"file://{file_path}"]
subprocess.run(command, check=True)


