import json
import sys
from audio_to_waveform import audio_to_waveform

def predict(input_data):
    file_path_or_url = input_data["file"]
    is_url = input_data.get("is_url", False)
    waveform = audio_to_waveform(file_path_or_url, is_url)
    return waveform.tolist()

if __name__ == "__main__":
    input_data = json.load(sys.stdin)
    waveform = predict(input_data)
    output = {"waveform": waveform}
    print(json.dumps(output))

