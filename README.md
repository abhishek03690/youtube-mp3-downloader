
# YouTube MP3 Downloader

A simple Python script to download YouTube videos and playlists as MP3 files. This script leverages the `pytubefix` library to download videos and `ffmpeg` to convert them to MP3 format. It provides a seamless way to download audio from YouTube and save it in MP3 format for offline use.

## Features

* **Download single YouTube videos** as MP3 files.
* **Download entire YouTube playlists** and convert them to MP3.
* **Custom save path**: Choose where to save the MP3 files, and the script will remember this location for future use.
* **Progress indicators**: Real-time download and conversion progress with visual feedback.

## Requirements
Before running the script, you need to have the following installed:

* **Python 3.x**
* **`pytubefix`**: For downloading YouTube videos.
* **`ffmpeg`**: To convert videos into MP3 format.
* **`tqdm`, `alive-progress`, `termcolor`**: For showing progress bars and colorized terminal output.

### Installation

1. **Clone the repository** or download the script:

   bash
   git clone https://github.com/abhishek03690/youtube-mp3-downloader.git
   
2. **Navigate to the project folder**:

   bash
   cd youtube-mp3-downloader
   
3. **Install the required Python libraries**:

   bash
   pip install pytubefix ffmpeg-python alive-progress termcolor
   
   bash
   pip install -r requirements.txt
   
5. **Install FFmpeg**:

   * On **Linux (Ubuntu/Debian)**:

     bash
     sudo apt install ffmpeg

   * On **macOS** (using Homebrew):

     bash
     brew install ffmpeg
     
   * On **Windows**, download FFmpeg from the [official website](https://ffmpeg.org/download.html), and add it to your system’s `PATH`.
   

## Usage

### 1. **First Run - Choose Save Path**

When you run the script for the first time, it will ask you to specify the directory where the MP3 files will be saved. This directory will be saved for future use.

bash
python ytmp3.py


Example prompt:

Enter the path where you want to save MP3 files: /path/to/your/directory

After the first run, the script will remember this path and automatically save all MP3 files to that location in future runs.

### 2. **Download a Single YouTube Video as MP3**

To download an individual video, simply enter the YouTube video URL when prompted. The script will download the audio and convert it to MP3 format.

Example prompt:

Enter YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ


The script will save the MP3 file in the chosen save directory.

### 3. **Download a YouTube Playlist as MP3**

To download an entire playlist, enter the YouTube playlist URL when prompted. The script will download and convert each video in the playlist to MP3 format.

Example prompt:

Enter YouTube playlist URL: https://www.youtube.com/playlist?list=PLxTgWxF-jxzsmkcTtXZtE0gzIyaElNwmd

Each video in the playlist will be processed individually.

## Script Details

### Functions

#### `download_youtube_as_mp3(url, save_path)`

* **Description**: Downloads a single YouTube video and converts it to MP3.
* **Parameters**:

  * `url` (str): The YouTube video URL.
  * `save_path` (str): The directory where the MP3 file will be saved.

#### `download_playlist_as_mp3(playlist_url, save_path)`

* **Description**: Downloads and converts all videos in a YouTube playlist to MP3.
* **Parameters**:

  * `playlist_url` (str): The URL of the YouTube playlist.
  * `save_path` (str): The directory where MP3 files will be saved.

#### `get_save_path()`

* **Description**: Retrieves the save path from the `config.txt` file (if it exists), or prompts the user to input the path if it's the first run.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

* **FFmpeg not found**: If FFmpeg is not detected by the script, ensure that FFmpeg is correctly installed and added to your system’s `PATH`.
* **Invalid video URL**: If the video is unavailable or deleted, the script will show an error. Try using a different video URL.
* **Path errors**: If the save path provided in `config.txt` does not exist, the script will prompt you for a new path.

## Contributing

Feel free to contribute by opening an issue or creating a pull request! Here are some ideas for improvements:

* Add support for batch downloads from text files.
* Allow the user to select MP3 quality (e.g., 128kbps, 192kbps).
* Add more error handling and logging.

## Contact

For any questions or suggestions, feel free to open an issue on GitHub or contact me at:
**Email**: [technologyhacker02@gmail.com](mailto:technologyhacker02@gmail.com)
**GitHub**: [https://github.com/abhishek03690](https://github.com/abhishek03690)

