import os

folder_path = "camers_settings/cam_RT"  # Replace with the actual path to your cam_RT folder
new_folder_path = "camers_settings/cam_RT_new"  # Replace with the actual path to your cam_RT folder

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.startswith("cam_RT_") and filename.endswith(".txt"):
            # Extract the index from the filename
            index_str = filename.split("_")[2].split(".")[0]
            index = int(index_str)

            # Reduce the index by 1
            new_index = index - 1

            # Create the new filename
            new_filename = "cam_RT_{:03d}.txt".format(new_index)

            # Construct the full paths for old and new filenames
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(new_folder_path, new_filename)

            # Rename the file
            os.rename(old_path, new_path)

            print(f"Renamed: {filename} to {new_filename}")

# Call the function to rename files in the specified folder
rename_files(folder_path)
