import os
import subprocess
import re
from urllib.parse import urlparse, parse_qs
from pytubefix import YouTube, Playlist
from tqdm import tqdm
from alive_progress import alive_bar
from termcolor import colored

CONFIG_FILE = "config.txt"  # File where the download path will be stored

def clean_youtube_url(url):
    """Clean YouTube URL and ensure it contains a valid video ID"""
    parsed = urlparse(url)
    video_id = parse_qs(parsed.query).get("v")
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id[0]}"
    raise ValueError("Invalid YouTube URL (no video ID found)")

def clean_filename(title):
    """Sanitize the title to make it safe for filenames"""
    return re.sub(r'[\\/*?:"<>|]', '_', title)

def download_youtube_as_mp3(url, save_path):
    try:
        clean_url = clean_youtube_url(url)
        yt = YouTube(clean_url)
        video_title = clean_filename(yt.title)  
        print(f"\n{colored('Downloading:', 'cyan')} {colored(video_title, 'yellow')}...")

        # Progress bar for download
        audio_stream = yt.streams.filter(only_audio=True).first()

        with alive_bar(total=100, title=f"Downloading {video_title}", spinner='dots') as bar:
            temp_file = audio_stream.download(filename="temp_audio")
            bar()

        mp3_filename = f"{video_title}.mp3"
        mp3_path = os.path.join(save_path, mp3_filename)

        # Convert to MP3 using ffmpeg with progress animation
        print(f"{colored('Converting to MP3...', 'blue')}")
        with alive_bar(total=100, title=f"Converting {video_title}", spinner='pulse') as bar:
            subprocess.run([
                'ffmpeg', '-i', temp_file,
                '-vn', '-ab', '192k', '-ar', '44100', '-y', mp3_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            bar()

        os.remove(temp_file)
        print(f"{colored('✅ MP3 saved to:', 'green')} {mp3_path}\n")
    except Exception as e:
        print(f"{colored('❌ Error:', 'red')} {e}")

def download_playlist_as_mp3(playlist_url, save_path):
    try:
        playlist = Playlist(playlist_url)
        print(f"\n{colored('Downloading Playlist:', 'cyan')} {colored(playlist.title, 'yellow')}")
        
        with alive_bar(len(playlist.videos), title="Downloading Playlist", spinner='dots') as bar:
            for video in playlist.videos:
                video_url = video.watch_url
                print(f"\n{colored('Downloading:', 'cyan')} {colored(video.title, 'yellow')}...")

                audio_stream = video.streams.filter(only_audio=True).first()
                temp_file = audio_stream.download(filename="temp_audio")
                bar()

                mp3_filename = f"{clean_filename(video.title)}.mp3"
                mp3_path = os.path.join(save_path, mp3_filename)

                # Convert to MP3
                subprocess.run([
                    'ffmpeg', '-i', temp_file,
                    '-vn', '-ab', '192k', '-ar', '44100', '-y', mp3_path
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

                os.remove(temp_file)
                print(f"{colored('✅ MP3 saved to:', 'green')} {mp3_path}\n")

    except Exception as e:
        print(f"{colored('❌ Error while downloading playlist:', 'red')} {e}")

def get_save_path():
    """Get the save path from the config file or ask the user for it."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            save_path = file.read().strip()
            if os.path.exists(save_path):  # Check if the saved path exists
                return save_path
            else:
                print(f"{colored('❌ The saved path does not exist. Please provide a new path.', 'red')}")
    
    # If path is not saved or invalid, ask the user
    save_path = input(f"{colored('Enter the path where you want to save MP3 files:', 'cyan')} ").strip()
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Save the path for future runs
    with open(CONFIG_FILE, 'w') as file:
        file.write(save_path)

    return save_path

def main():
    # Get the save path, either from the config or user input
    save_path = get_save_path()

    while True:
        url = input(f"{colored('Enter YouTube video or playlist URL:', 'cyan')} ").strip()
        
        if "playlist" in url:  # If it's a playlist URL
            download_playlist_as_mp3(url, save_path)
        elif url:  # If it's a single video URL
            download_youtube_as_mp3(url, save_path)
        else:
            print(f"{colored('❌ Invalid URL', 'red')}")

        again = input(f"{colored('Do you want to convert another video/playlist? (y/n):', 'cyan')} ").strip().lower()
        if again != 'y':
            print(f"{colored('👋 Goodbye!', 'green')}")
            break

if __name__ == "__main__":
    main()
