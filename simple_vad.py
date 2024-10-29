import webrtcvad
import sounddevice as sd
import numpy as np
import time

# Parameters
sampling_rate = 16000  # Hertz
block_size = 320  # samples per block (320 samples / 16000 Hz = 20 ms)
vad_aggressiveness = 3  # 0-3, higher is more aggressive

# Initialize VAD
vad = webrtcvad.Vad(vad_aggressiveness)


def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(f"Error:   {status}")

    # Convert audio to the format expected by webrtcvad
    indata = indata.squeeze()  # remove extra dimension
    indata = indata.astype(np.int16)  # convert to int16

    # Process in 10 ms frames (adjust as needed)
    frame_duration_ms = 10
    frame_bytes = int(sampling_rate * frame_duration_ms / 1000) * 2
    for i in range(0, len(indata) - frame_bytes + 1, frame_bytes):
        frame = indata[i:i + frame_bytes]
        is_speech = vad.is_speech(frame.tobytes(), sampling_rate)
        print(f"Voice detected: {is_speech}")


with sd.InputStream(samplerate=sampling_rate,
                     blocksize=block_size,
                     channels=1,
                     dtype=np.int16,
                     callback=audio_callback):
    print("Listening... Press Ctrl+C to stop")
    try:
        while True:
            time.sleep(0.1)  # Sleep for a short duration
    except KeyboardInterrupt:
        print("Stopped")
