import os
from audio_extract import extract_audio

def main():
    # Define the directory path where the .mp4 files are located
    directory = '/Users/felixtong/Desktop/usf_msds/ACLU/data/'

    # Use os.walk to traverse through all subdirectories of the specified directory
    for root, dirs, files in os.walk(directory):
        # For each file in the current directory
        for file in files:
            # Check if the file ends with '.mp4'
            if file.endswith('.mp4'):
                # Construct the full path of the .mp4 file
                input_file_path = os.path.join(root, file)
                # Replace the '.mp4' extension with '.mp3' to create the new file name
                new_file_path = file.replace('.mp4','.mp3')
                # Construct the full path of the .mp3 file
                output_file_path = os.path.join(root, new_file_path)
                # Check if the .mp3 file already exists
                if not os.path.isfile(output_file_path):
                    # If the .mp3 file does not exist, call the extract_audio function to convert the .mp4 file to .mp3
                    extract_audio(input_path=input_file_path, output_path=output_file_path)

if __name__ == "__main__":
    main()
