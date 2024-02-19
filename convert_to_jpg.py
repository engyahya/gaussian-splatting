import os
from PIL import Image

#folder_path = './1a0bc9ab92c915167ae33d942430658c/'  # Replace with the actual folder path
#folder_path = './1a1dcd236a1e6133860800e6696b8284/'  # Replace with the actual folder path
folder_path = './Datasets/car9/input_png/'  # Replace with the actual folder path

# Create a new folder for the output images
#output_folder_path = os.path.join(folder_path, 'output')
#os.makedirs(output_folder_path, exist_ok=True)
output_folder_path = './Datasets/car9/input/'

# Get a list of all .png files in the folder
png_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]

# Iterate over each .png file
for i, png_file in enumerate(png_files):
    # Open the image
    image_path = os.path.join(folder_path, png_file)
    image = Image.open(image_path)

    # Convert black pixels to white
    image = image.convert('RGB')
    pixels = image.load()
    width, height = image.size
    # resize the image 
    image = image.resize((1024, 1024))

    #for x in range(width):
    #    for y in range(height):
    #        if pixels[x, y] == (0, 0, 0):
    #            pixels[x, y] = (255, 255, 255)

    # Save the image with new name in the output folder
    new_name = f'{i:04d}.jpg'
    new_path = os.path.join(output_folder_path, new_name)
    image.save(new_path)

    # Close the image
    image.close()
