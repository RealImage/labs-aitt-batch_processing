from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

def split_audio(audio_path, silence_thresh=-40, min_silence_len=500, chunk_length=120000, output_dir="/content/new_audio_chunks/"):
    # Load audio file
    audio = AudioSegment.from_file(audio_path)
    print(f"Total audio length: {len(audio)} ms")
    
    # Split audio on silence
    chunks = split_on_silence(audio,
                              min_silence_len=min_silence_len,
                              silence_thresh=silence_thresh, keep_silence=True)
    print(f"Initial number of chunks: {len(chunks)}")
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    merged_chunks = []
    current_chunk = AudioSegment.empty()
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i} length: {len(chunk)} ms")
        
        if len(current_chunk) + len(chunk) <= chunk_length:
            current_chunk += chunk
        else:
            if len(current_chunk) > 0:
                merged_chunks.append(current_chunk)
            current_chunk = chunk
        
        # Handle the last chunk
        if i == len(chunks) - 1 and len(current_chunk) > 0:
            merged_chunks.append(current_chunk)
    
    split_chunks = merged_chunks
    
    
    # Save chunks to files
    for i, chunk in enumerate(split_chunks):
        chunk_path = os.path.join(output_dir, f"chunk_{i}.wav")
        chunk.export(chunk_path, format="wav")
        print(f"Saved chunk {i} length: {len(chunk)} ms to {chunk_path}")
    
    # return split_chunks




audio_file = 'Code-Nayantara.wav'  # Update this path to your local audio file
output_srt = "output_subtitles.srt"


split_chunks = split_audio(audio_file)
