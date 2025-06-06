from transcriber import transcribe_audio
from diarizer import diarize_audio
from utils import convert_to_wav
import os
import json

AUDIO_DIR = "audio"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(AUDIO_DIR):
    if not filename.lower().endswith((".mp3", ".wav", ".mpeg", ".m4a")):
        continue

    filepath = os.path.join(AUDIO_DIR, filename)
    print(f"\n🔁 Processing: {filename}")

    # Convert to WAV if needed
    if not filename.endswith(".wav"):
        print("🔄 Converting to WAV...")
        filepath = convert_to_wav(filepath)

    transcription = transcribe_audio(filepath)
    diarized = diarize_audio(filepath, transcription)

    out_filename = os.path.basename(filepath).replace(".wav", ".json")
    out_file = os.path.join(OUTPUT_DIR, out_filename)

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(diarized, f, ensure_ascii=False, indent=4)

    print(f"✅ Done: {out_file}")
