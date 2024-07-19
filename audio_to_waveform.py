import numpy as np
import wave
import struct
import requests
from io import BytesIO

def download_audio(url):
    response = requests.get(url)
    response.raise_for_status()
    return BytesIO(response.content)

def audio_to_waveform(file_path_or_url, is_url=False):
    if is_url:
        file = download_audio(file_path_or_url)
    else:
        file = file_path_or_url
    
    with wave.open(file, 'r') as wav_file:
        # Extract raw audio frames
        frames = wav_file.readframes(wav_file.getnframes())
        # Convert frames to integer values
        frame_count = wav_file.getnframes()
        frame_width = wav_file.getsampwidth()
        fmt = f"{frame_count * frame_width // 2}h"
        waveform_data = struct.unpack(fmt, frames)
        return np.array(waveform_data)

# Example usage
waveform = audio_to_waveform("https://example.com/audio.wav", is_url=True)
print(waveform)

