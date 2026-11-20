
import os
import shutil

# Folder to organize
source_folder = "sample_files"

# Create folders for different file types
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Python_Files": [".py"]
}

# Create the source folder if it doesn't exist
if not os.path.exists(source_folder):
    os.mkdir(source_folder)

# Organize files
for filename in os.listdir(source_folder):

    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):

        extension = os.path.splitext(filename)[1].lower()

        folder_name = "Others"

        for category, extensions in file_types.items():
            if extension in extensions:
                folder_name = category
                break

        destination_folder = os.path.join(source_folder, folder_name)

        os.makedirs(destination_folder, exist_ok=True)

        shutil.move(
            file_path,
            os.path.join(destination_folder, filename)
        )

        print(filename, "moved to", folder_name)

print("File organization completed!")
