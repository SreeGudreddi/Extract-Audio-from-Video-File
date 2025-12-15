import requests
import subprocess
import os

def download_instagram_video(video_url, output_video_path="video.mp4"):
    """
    Downloads an Instagram video from a direct URL.
    """
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(video_url, headers=headers, stream=True)
    if response.status_code == 200:
        with open(output_video_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Video downloaded: {output_video_path}")
        return output_video_path
    else:
        raise Exception(f"Failed to download video. Status code: {response.status_code}")

def extract_audio_from_video(video_path, output_audio_path="audio.wav", sample_rate=16000):
    """
    Uses ffmpeg to extract audio from a video file.
    """
    command = [
        r"C:\Users\sgudr\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe",
        "-i", video_path,
        "-vn",  # ignore video
        "-acodec", "pcm_s16le",  # raw PCM
        "-ar", str(sample_rate),  # sample rate
        "-ac", "1",  # mono audio
        output_audio_path
    ]

    subprocess.run(command, check=True)
    print(f"Audio extracted: {output_audio_path}")
    return output_audio_path

if __name__ == "__main__":

    # Example usage
    instagram_video_url = r"C:\Users\sgudr\Downloads\frame_founder_video.mp4"  # replace with actual Instagram video URL
   # video_file = download_instagram_video(instagram_video_url)
    audio_file = extract_audio_from_video(instagram_video_url)
