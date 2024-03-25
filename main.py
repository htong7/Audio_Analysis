import os
import time
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import matplotlib.pyplot as plt
import numpy as np
from audio_extract import extract_audio

def transcribe_audio(audio_segment):
    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio_segment)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return ""

def process_video(video_path):
    r = sr.Recognizer()
    audio = AudioFileClip(video_path)
    duration = int(audio.duration)
    binary_outcome = [0] * duration
    for i in range(duration):
        audio_segment = audio.subclip(i, i+1)
        audio_segment.write_audiofile("temp.wav", logger=None)
        with sr.AudioFile("temp.wav") as source:
            audio_data = r.record(source)
            transcript = transcribe_audio(audio_data)
            if transcript:
                binary_outcome[i] = 1
    return binary_outcome

def process_file(file_path):
    binary_outcome = process_video(file_path)
    return binary_outcome

def plot_binary_outcome(binary_outcome):
    plt.figure(figsize=(40, 6))
    x = np.arange(len(binary_outcome))
    plt.fill_between(x, binary_outcome, color='red', alpha=0.7, where=np.array(binary_outcome)==1)
    plt.xticks(np.arange(min(x), max(x)+1, 5))
    plt.xlabel('Time (seconds)')
    plt.ylabel('Speech Detected')
    plt.show()

def main():
    directory = '/Users/felixtong/Desktop/usf_msds/ACLU/data/'

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                input_file_path = os.path.join(root, file)
                new_file_path = file.replace('.mp4','.mp3')
                output_file_path = os.path.join(root, new_file_path)
                if not os.path.isfile(output_file_path):
                    extract_audio(input_path=input_file_path, output_path=output_file_path)

                binary_outcome = process_file(output_file_path)
                plot_binary_outcome(binary_outcome)

if __name__ == "__main__":
    max_retries = 5
    retries = 0
    while retries < max_retries:
        try:
            main("/path/to/your/directory")  # replace with your directory
            break
        except ConnectionResetError:
            print("Connection reset by peer. Retrying...")
            time.sleep(5)
            retries += 1
