# Intelligent Video Editor

An AI-powered video editing tool that automatically enhances raw footage by detecting scenes, removing silences, syncing with music, applying color grading, and exporting cinematic videos.

## Features

- 🎬 **Automatic Scene Detection** - Intelligently splits video into scenes
- 🔇 **Silence Removal** - Automatically cuts out silent segments
- 🎵 **Music Sync** - Syncs video cuts to musical beats
- 🎨 **Color Grading** - Applies cinematic color presets
- 📤 **Smart Export** - Exports optimized videos in multiple formats
- 🌐 **Web Interface** - Modern, intuitive UI built with Streamlit

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install FFmpeg (required for video processing):
   - **Windows**: Download from https://ffmpeg.org/download.html
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg`

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser to `http://localhost:8501`

3. Upload your video and music files

4. Configure your editing preferences

5. Click "Process Video" and wait for the magic to happen!

## Project Structure

```
videoeditor/
├── app.py                 # Main Streamlit application
├── core/
│   ├── __init__.py
│   ├── scene_detector.py  # Scene detection logic
│   ├── audio_processor.py # Audio analysis and silence removal
│   ├── music_sync.py      # Music beat detection and sync
│   ├── color_grading.py   # Color grading and LUTs
│   └── video_exporter.py  # Video export functionality
├── utils/
│   ├── __init__.py
│   ├── file_utils.py      # File handling utilities
│   └── video_utils.py     # Video processing utilities
├── assets/
│   ├── luts/             # Color grading LUTs
│   └── presets/          # Editing presets
└── requirements.txt
```

## Supported Formats

- **Video**: MP4, MOV, AVI, MKV, WMV
- **Audio**: MP3, WAV, M4A, FLAC
- **Output**: MP4 (H.264), MOV (ProRes)

## License

MIT License - feel free to use and modify! 