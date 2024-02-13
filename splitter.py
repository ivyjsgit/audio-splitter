import subprocess
import re

def timestamp_to_seconds(timestamp):
    parts = timestamp.split('-')
    start_time = sum(int(x) * 60**i for i, x in enumerate(reversed(parts[0].split(':'))))
    end_time = sum(int(x) * 60**i for i, x in enumerate(reversed(parts[1].split(':'))))
    return start_time, end_time

def split_audio(input_file, output_prefix, timestamps_file):
    with open(timestamps_file, 'r') as file:
        for i, line in enumerate(file, start=1):
            start_time, end_time = timestamp_to_seconds(line.strip())
            duration = end_time - start_time
            output_file = f"{output_prefix}_{i}.mp3"
            subprocess.run(['ffmpeg', '-i', input_file, '-ss', str(start_time), '-t', str(duration), '-c', 'copy', output_file], capture_output=True)
            print(f"Segment {i} extracted: {output_file}")

def main():
    input_file = input("Enter the input audio file path: ")
    output_prefix = input("Enter the prefix for output files: ")
    timestamps_file = input("Enter the file path containing timestamps: ")

    split_audio(input_file, output_prefix, timestamps_file)

if __name__ == "__main__":
    main()
