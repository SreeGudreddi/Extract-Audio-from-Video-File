

# Extract Audio from Video

A simple and efficient utility for **extracting audio tracks from video files** using FFmpeg.
This project supports common video formats and outputs high-quality audio suitable for transcription, analysis, or downstream audio processing pipelines.

---

## Features

* Extracts audio from video files
* Supports common formats (MP4, MKV, AVI, MOV, etc.)
* Outputs WAV or MP3 audio
* Preserves audio quality and sampling rate
* Lightweight and easy to integrate into pipelines

---

## Project Structure

```
extract-audio-from-video/
├── extract_audio.py     # Audio extraction script
├── requirements.txt
├── README.md
└── assets/
    └── sample_video.mp4 # Example input video
```

---

## How It Works

The script uses **FFmpeg** to:

1. Read the input video file
2. Isolate the audio stream
3. Convert and save the audio in the desired format

---

## Prerequisites

* Python 3.8+
* FFmpeg installed and available in PATH

### Install FFmpeg

**macOS**

```bash
brew install ffmpeg
```

**Ubuntu / Debian**

```bash
sudo apt install ffmpeg
```

**Windows**

* Download from [https://ffmpeg.org](https://ffmpeg.org)
* Add FFmpeg to system PATH

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python extract_audio.py --input sample_video.mp4 --output audio.wav
```

### Optional Arguments

* `--format` : Output format (`wav`, `mp3`)
* `--sample_rate` : Target sample rate (e.g., 16000)

---

## Example

```bash
python extract_audio.py --input interview.mp4 --output interview.wav --sample_rate 16000
```

---

## Use Cases

* Speech-to-text pipelines
* Meeting and call transcription
* Podcast and interview processing
* Audio analytics and NLP workflows
* Preprocessing for LLM-based insights

---

## Design Principles

* Simple CLI interface
* Minimal dependencies
* Pipeline-friendly output
* Easy integration with ASR and NLP systems

---

## Future Enhancements

* Batch processing support
* GUI interface
* Automatic format detection
* Metadata extraction

---

## License

This project is intended for research and educational purposes.
Add a license file as appropriate.

---



Just tell me 👍
