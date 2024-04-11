import os
from PIL import Image

#folder_path = './1a0bc9ab92c915167ae33d942430658c/'  # Replace with the actual folder path
#folder_path = './1a1dcd236a1e6133860800e6696b8284/'  # Replace with the actual folder path
folder_path = './Datasets/cars/1a0bc9ab92c915167ae33d942430658c/input_png'  # Replace with the actual folder path

# Create a new folder for the output images
#output_folder_path = os.path.join(folder_path, 'output')
#os.makedirs(output_folder_path, exist_ok=True)
output_folder_path = './Datasets/cars/1a0bc9ab92c915167ae33d942430658c/images/'

# Get a list of all .png files in the folder
png_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]
#sort the files
png_files.sort()

# Iterate over each .png file
for i, png_file in enumerate(png_files):
    # Open the image
    image_path = os.path.join(folder_path, png_file)

    print ("-------------------") 
    print (image_path)
    image = Image.open(image_path)
    # sprit the image path by _ and then by . and have the first element
    # as the new name for the image


    #new_name = image_path.split('_')[2].split('.')[0] + '.jpg'
    #print ("new_name: ")
    #new_name = "0" + new_name
    #print ("0" + new_name)

    # new_name  is i from 4 digits + .jpg
    new_name = f'{i:04d}.jpg'

    # Convert black pixels to white
    image = image.convert('RGB')
    pixels = image.load()
    width, height = image.size
    # resize the image 
    # image = image.resize((1024, 1024))

    for x in range(width):
        for y in range(height):
            if pixels[x, y] == (0, 0, 0):
                pixels[x, y] = (255, 255, 255)
            #else:
            #    pixels[x, y] = (0, 0, 0)
            #if pixels[x, y] != (255, 255, 255):
            #    pixels[x, y] = (0, 0, 0)

    # Save the image with new name in the output folder
    #new_name = f'{i:04d}.jpg'
    new_path = os.path.join(output_folder_path, new_name)
    print ("new_path: ")
    print (new_path)
    image.save(new_path)

    # Close the image
    image.close()
