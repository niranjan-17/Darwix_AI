from pyannote.audio import Pipeline
from whisperx.diarize import assign_word_speakers
import os

def diarize_audio(audio_path: str, segments):
    print("Performing speaker diarization...")

    # 1. Get token from environment (safer than hardcoding)
    hf_token = os.getenv("HF_TOKEN", "_")  # USE_HUGGING_FACE_TOKEN_HERE

    try:
        # 2. Load diarization pipeline with auth token
        pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization@2.1",
            use_auth_token=hf_token
        )
    except Exception as e:
        print("Failed to load diarization pipeline:", e)
        return None

    # 3. Run diarization
    try:
        diarization = pipeline(audio_path)
    except Exception as e:
        print("Failed during diarization:", e)
        return None

    # 4. Extract speaker segments
    speaker_segments = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        speaker_segments.append({
            "speaker": speaker,
            "start": turn.start,
            "end": turn.end
        })

    # 5. Assign speakers to Whisper words
    result = assign_word_speakers(diarized_segments=speaker_segments, whisper_segments=segments)
    return result
