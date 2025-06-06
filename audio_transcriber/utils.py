from pydub import AudioSegment

def convert_to_wav(input_path: str) -> str:
    audio = AudioSegment.from_file(input_path)
    output_path = input_path.rsplit(".", 1)[0] + ".wav"
    audio.export(output_path, format="wav")
    return output_path
