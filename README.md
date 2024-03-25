# Speech Detection in Video Files

This Python script processes video files to detect speech and visualize the results.

## Dependencies

- os
- time
- speech_recognition
- moviepy.editor
- matplotlib.pyplot
- numpy
- audio_extract (a custom module)

## How it Works

1. The script walks through a specified directory and its subdirectories to find all .mp4 files.
2. For each .mp4 file, it checks if a corresponding .mp3 file exists. If not, it extracts the audio from the .mp4 file using the `extract_audio` function from the `audio_extract` module.
3. The script then processes the audio file, segmenting it into one-second clips.
4. Each audio segment is transcribed using Google's Speech Recognition service.
5. If speech is detected in a segment, the corresponding index in a binary outcome array is set to 1.
6. Finally, the binary outcome array is plotted, providing a visual representation of when speech occurs in the video.

## Usage

Run the script with Python. If a `ConnectionResetError` occurs, the script will automatically retry after 5 seconds.

Please note that this script is designed to be run in an environment where the Google Speech Recognition service is accessible, and the necessary Python packages are installed.
