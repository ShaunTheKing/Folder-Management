import os
import time

# Define your source directory
source_dir = "path/to/source/directory"

# Define your destination directories
dest_dir_pdf = "path/to/pdf/destination/directory"
dest_dir_video = "path/to/video/destination/directory"
dest_dir_audio = "path/to/audio/destination/directory"
# Add more destination directories as needed
dest_dir_images = "path/to/image/destination/directory"

# Polling interval in seconds
polling_interval = 5

# Create dictionaries to store the file modification times
file_modification_times_pdf = {}
file_modification_times_video = {}
file_modification_times_audio = {}
# Add more dictionaries for other file types as needed
file_modification_times_images = {}

def monitor_directory():
    while True:
        # Get the list of files in the source directory
        files = os.listdir(source_dir)
        
        for file in files:
            file_path = os.path.join(source_dir, file)
            # Check if the file has a .pdf extension
            if file.lower().endswith(".pdf"):
                move_file(file, file_path, dest_dir_pdf, file_modification_times_pdf)
            # Check if the file has a video extension
            elif file.lower().endswith((".mp4", ".avi", ".mov")):
                move_file(file, file_path, dest_dir_video, file_modification_times_video)
            # Check if the file has an audio extension
            elif file.lower().endswith((".mp3", ".wav", ".flac")):
                move_file(file, file_path, dest_dir_audio, file_modification_times_audio)
            # Add more conditions for other file types
            elif file.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                move_file(file, file_path, dest_dir_images, file_modification_times_images)
        
        # Sleep for the polling interval
        time.sleep(polling_interval)

def move_file(file, file_path, dest_dir, file_modification_times):
    # Check if the file has been modified since the last check
    if os.path.isfile(file_path):
        modification_time = os.path.getmtime(file_path)
        if file not in file_modification_times or modification_time > file_modification_times[file]:
            # Move the file to the destination directory
            destination_path = os.path.join(dest_dir, file)
            os.rename(file_path, destination_path)
            print(f"Moved {os.path.splitext(file)[1][1:].upper()} file: {file}")
            # Update the modification time in the dictionary
            file_modification_times[file] = modification_time

if __name__ == "__main__":
    monitor_directory()
