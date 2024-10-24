# Audio Splitting Program

This tool splits an audio file into smaller chunks based on silence detection. It uses the `pydub` library to handle audio processing.

## Features

- Splits audio based on silence detection.
- Merges chunks to ensure they do not exceed a specified length.
- Saves the resulting chunks as `.wav` files in a specified output directory.

## Requirements

- Python 3.x
- `pydub` library
- `ffmpeg` or `libav` installed on your system

## Installation

1. Install the required Python packages:
    ```bash
    pip install pydub
    ```

2. Ensure `ffmpeg` or `libav` is installed on your system. You can download `ffmpeg` from [here](https://ffmpeg.org/download.html).
3. ffmpeg for mac
   ```bash
    brew install ffmpeg
    ```

## Usage

1. Place your audio file in the same directory as the script or update the `audio_file` variable with the correct path.

2. Run the script:
    ```bash
    python split_audio.py
    ```

3. The script will split the audio file into chunks and save them in the specified output directory (default is `/content/new_audio_chunks/`).

## Configuration

You can adjust the following parameters in the `split_audio` function:

- `silence_thresh`: Threshold for silence detection (default is -40 dBFS).
- `min_silence_len`: Minimum length of silence to consider for splitting (default is 500 ms).
- `chunk_length`: Maximum length of each chunk (default is 120000 ms or 2 minutes).
- `output_dir`: Directory to save the split audio chunks (default is `/content/new_audio_chunks/`).

## Example

``` python
audio_file = '<your_audio_file_path>'  # Update this path to your local audio file
split_audio(audio_file)
```


## Conclusion
> Batch processing video chunks for LLM testing significantly enhances the efficiency and scalability of the evaluation process. This method allows for the simultaneous analysis of multiple segments, leading to more accurate and detailed content capture, ultimately reducing the amount of omitted speech. While this approach optimizes resource utilization, careful attention must be paid to context preservation to prevent loss of continuity in the model's understanding, ensuring coherent and comprehensive outputs.
