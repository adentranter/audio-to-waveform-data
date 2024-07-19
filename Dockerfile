FROM python:3.9-slim

# Install dependencies
RUN pip install numpy requests

# Copy the library and the predict script
COPY audio_to_waveform.py /app/audio_to_waveform.py
COPY predict.py /app/predict.py

WORKDIR /app

ENTRYPOINT ["python", "predict.py"]

