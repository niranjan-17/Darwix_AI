# Audio Transcription with Diarization

This project offers a robust solution for transcribing audio files and automatically identifying different speakers within the transcription. It uses powerful open-source tools like **WhisperX** for transcription and **pyannote.audio** for speaker diarization, providing accurate and structured JSON output.

---

## Features

* **Accurate Audio Transcription:** Leverages WhisperX for high-quality speech-to-text conversion.
* **Speaker Diarization:** Differentiates between speakers in the audio, assigning speaker labels to transcribed segments.
* **Structured JSON Output:** Presents transcription and diarization results in a clean, easy-to-parse JSON format.
* **Multilingual Support (WhisperX):** Inherits multilingual capabilities from WhisperX, allowing for transcription of various languages.
* **Automatic WAV Conversion:** Handles common audio formats (`.mp3`, `.m4a`, `.mpeg`) by converting them to `.wav` for processing.

---

## Installation

Before you begin, make sure you have **Python 3.8+** installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your_username/your_repo_name.git](https://github.com/your_username/your_repo_name.git)
    cd your_repo_name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install torch torchaudio transformers pyannote.audio whisperx faster-whisper numpy scipy pydub
    ```

4.  **Hugging Face Authentication Token:**
    `pyannote.audio` requires an authentication token from Hugging Face.
    * Go to [Hugging Face Settings](https://huggingface.co/settings/tokens) and create a **new access token** with "read" role.
    * Set this token as an environment variable named `HF_TOKEN`. You can do this in your terminal:
        ```bash
        export HF_TOKEN="YOUR_HUGGING_FACE_TOKEN"
        ```
        **Important:** Replace `"YOUR_HUGGING_FACE_TOKEN"` with the actual token you generated. For persistent setup, consider adding this line to your `.bashrc`, `.zshrc`, or system environment variables.

---

## Usage

1.  **Place your audio files** in the `audio/` directory. Supported formats include `.mp3`, `.wav`, `.mpeg`, and `.m4a`.

2.  **Run the main script:**
    ```bash
    python main.py
    ```

    The script will process each audio file in the `audio/` directory, transcribe it, perform speaker diarization, and save the results as a JSON file in the `output/` directory.

---

## Output Format

The output for each audio file will be a JSON file containing an array of segments, each with the following structure:

```json
[
    {
        "text": "Hello, this is speaker one.",
        "start": 0.5,
        "end": 3.2,
        "speaker": "SPEAKER_00"
    },
    {
        "text": "And I am speaker two, responding.",
        "start": 4.1,
        "end": 7.8,
        "speaker": "SPEAKER_01"
    }
    // ... more segments
]
text: The transcribed text for the segment.
start: The start time of the segment in seconds.
end: The end time of the segment in seconds.
speaker: The identified speaker for that segment (e.g., SPEAKER_00, SPEAKER_01).
Project Structure
.
├── audio/                 # Directory to place your input audio files
├── output/                # Directory where JSON output files will be saved
├── diarizer.py            # Contains the speaker diarization logic
├── transcriber.py         # Handles the audio transcription
├── utils.py               # Utility functions, e.g., audio conversion
└── main.py                # The main script to run the process
Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements!

License
This project is open-sourced under the MIT License. See the LICENSE file for more details.