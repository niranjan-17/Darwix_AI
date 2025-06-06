import whisperx

def transcribe_audio(audio_path: str):
    # model = whisperx.load_model(
    #     "base",  # or "medium", "large-v3", etc.
    #     device="cuda" if torch.cuda.is_available() else "cpu",
    #     compute_type="float16" if torch.cuda.is_available() else "int8"
    # )
    model = whisperx.load_model("medium", device="cpu", compute_type="int8")

    audio = whisperx.load_audio(audio_path)
    result = model.transcribe(audio, batch_size=16, language=None)
    return result["segments"]
