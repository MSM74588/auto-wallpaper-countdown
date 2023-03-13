# # from PIL import Image, ImageDraw, ImageFont
# # import os
# # from datetime import date

# # # Define the path to the template image file
# # template_image_path = f"{os.getcwd()}/template.png"
# # print(template_image_path)

# # # Define the font to use for the number
# # font = ImageFont.truetype("LED-Dot-Matrix.ttf", 40)

# # # Define the range of numbers to use
# # start_number = 1
# # end_number = 10

# # # Define the output image size
# # image_width = 1920
# # image_height = 1080

# # # Create a loop that iterates over the range of numbers
# # for i in range(start_number, end_number + 1):
# #     # Load the template image
# #     template_image = Image.open(template_image_path)

# #     # Draw the number on the image
# #     draw = ImageDraw.Draw(template_image)
# #     number_position = (100, 100)  # Change this to position the number on the image
# #     number_position2 = (764, 868)  # Change this to position the number on the image
# #     draw.text(number_position, str(i), font=font, fill=(255, 255, 255))
# #     draw.text(number_position2, str(f"Today is {date.today()}"), font=font, fill=(255, 255, 255), align="center")
    

# #     # Resize the image to the desired size
# #     template_image = template_image.resize((image_width, image_height))

# #     # Save the modified image with a unique filename
# #     output_image_folder = "output"
# #     output_image_filename = f"image{i}.png"
# #     output_image_path = f"{output_image_folder}/{output_image_filename}"
# #     template_image.save(output_image_path)


# # from PIL import Image, ImageDraw, ImageFont

# # # Define the font file path
# # font_file = "LED-Dot-Matrix.ttf"

# # # Define the text to be written
# # text = "30"

# # # Define the font size and weight
# # font_size = 221
# # font_weight = 400

# # # Define the image size
# # image_size = (1920, 1080)

# # # Create a new image with a white background
# # image = Image.new('RGB', image_size, color=(255, 255, 255))

# # # Load the font
# # font = ImageFont.truetype(font_file, font_size, weight=font_weight)

# # # Get the size of the text
# # text_width, text_height = font.getsize(text)

# # # Calculate the x and y coordinates for the center of the image
# # x = (image_size[0] - text_width) / 2
# # y = (image_size[1] - text_height) / 2

# # # Draw the text in the center of the image
# # draw = ImageDraw.Draw(image)
# # draw.text((x, y), text, font=font, fill=(255, 255, 255))

# # # Save the image as "xyz.png"
# # image.save("template.png")

# from PIL import Image, ImageDraw, ImageFont

# # Define the font file path
# # font_file = "abc.ttf"
# font_file = "LED-Dot-Matrix.ttf"


# # Define the text to be written
# text = "30"

# # Define the font size and weight
# font_size = 221
# font_weight = "bold"

# # Define the image size
# image_size = (1920, 1080)

# # Create a new image with a white background
# image = Image.new('RGB', image_size, color=(255, 255, 255))

# # Load the font
# font = ImageFont.truetype(font_file, font_size)

# # Create a new font with the desired weight
# # font = font.font_variant(weight=font_weight)

# # Get the size of the text
# text_width, text_height = font.getsize(text)

# # Calculate the x and y coordinates for the center of the image
# x = (image_size[0] - text_width) / 2
# y = (image_size[1] - text_height) / 2

# # Draw the text in the center of the image
# draw = ImageDraw.Draw(image)
# draw.text((x, y), text, font=font, fill=(255, 255, 255))

# # Save the image as "xyz.png"
# image.save("output.png")


from PIL import Image, ImageDraw, ImageFont

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
image = Image.open("template.png")

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

def draw_line(font_file_name, font_size, x_coordinate_from_centre, y_coordinate_from_centre, color, input_string):
    font = ImageFont.truetype(font_file_name, font_size)

    text_width, text_height = draw.textsize(input_string, font=font)
    x = (image.width - text_width) / 2 + y_coordinate_from_centre
    y = (image.height - text_height) / 2 + x_coordinate_from_centre
    
    draw.text((x, y), str(input_string), font=font, fill=color)
    
    
# DRAW
draw_line("LED-Dot-Matrix.ttf", 221, -50, 0, "#FFFFFF", days_left)
draw_line("LED-Dot-Matrix.ttf", 30, 200, 0, "#FFFFFF", f"Today is {today_date()}")

#OUTPUT
image.save(output_file_name)


# Load the font
# font = ImageFont.truetype(font_file, font_size)

# Create a new font with the desired weight
# font = font.font_variant(weight=font_weight)

# # Get the size of the text
# text_width, text_height = draw.textsize(text, font=font)

# # Calculate the x and y coordinates for the center of the image
# x = (image.width - text_width) / 2
# y = (image.height - text_height) / 2 - 50

# # Draw the text in the center of the image
# draw.text((x, y), text, font=font, fill=(255, 255, 255))



# draw.text((x, y), str(datetime.date.today()), font=font, fill=(255, 255, 255))


# text_2 = f"Today is {todays_date()}"

# Save the output image as "output.png"

import subprocess
import os 
# template_image_path = f"{os.getcwd()}/{output_file_name}"

file_path = f"{os.getcwd()}/{output_file_name}"
command = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", f"file://{file_path}"]
subprocess.run(command, check=True)


