# 🎬 Intelligent Video Editor - Setup Guide

## Quick Start

1. **Install Python 3.8+** (if not already installed)
2. **Install FFmpeg** (required for video processing)
3. **Install dependencies**: `pip install -r requirements.txt`
4. **Run the application**: `python run.py` or `streamlit run app.py`

## Detailed Installation

### 1. Python Requirements
- Python 3.8 or higher
- pip package manager

### 2. FFmpeg Installation

#### Windows
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract to a folder (e.g., `C:\ffmpeg`)
3. Add to PATH environment variable
4. Verify: `ffmpeg -version`

#### macOS
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

### 3. Python Dependencies

Install all required packages:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install opencv-python moviepy librosa pydub scenedetect streamlit
pip install numpy scikit-learn pillow matplotlib seaborn tqdm
```

### 4. Verify Installation

Run the test script:
```bash
python test_installation.py
```

## Usage

### Starting the Application

**Option 1: Quick Start**
```bash
python run.py
```

**Option 2: Direct Streamlit**
```bash
streamlit run app.py
```

### Using the Application

1. **Upload Video**: Select your raw video file (MP4, MOV, AVI, etc.)
2. **Upload Music** (optional): Add background music for sync
3. **Adjust Settings**: Configure detection sensitivity and preferences
4. **Process**: Click "Process Video" and wait
5. **Download**: Get your edited video

### Features

- **🎬 Scene Detection**: Automatically splits video into scenes
- **🔇 Silence Removal**: Cuts out silent segments
- **🎵 Music Sync**: Syncs cuts to musical beats
- **🎨 Color Grading**: Applies cinematic color presets
- **📤 Export**: High-quality video output

## Troubleshooting

### Common Issues

**1. Import Errors**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**2. FFmpeg Not Found**
- Ensure FFmpeg is installed and in PATH
- Restart terminal/command prompt after installation

**3. Memory Issues**
- Close other applications
- Use smaller video files for testing
- Reduce resolution in export settings

**4. Processing Errors**
- Check video file format (MP4, MOV, AVI supported)
- Ensure video file is not corrupted
- Try with a shorter video first

### Performance Tips

- **Smaller files**: Process shorter videos for faster results
- **Lower resolution**: Use 720p for testing, 1080p for final
- **Close applications**: Free up RAM before processing
- **SSD storage**: Use SSD for faster file I/O

## File Structure

```
videoeditor/
├── app.py                 # Main Streamlit application
├── run.py                 # Quick start script
├── test_installation.py   # Installation test
├── requirements.txt       # Python dependencies
├── README.md             # Project overview
├── SETUP.md              # This setup guide
├── core/                 # Core processing modules
│   ├── scene_detector.py
│   ├── audio_processor.py
│   ├── music_sync.py
│   ├── color_grading.py
│   └── video_exporter.py
├── utils/                # Utility functions
│   ├── file_utils.py
│   └── video_utils.py
└── assets/               # Resources
    ├── luts/            # Color grading LUTs
    └── presets/         # Editing presets
```

## Advanced Configuration

### Custom Color Presets

Edit `core/color_grading.py` to add custom presets:
```python
'my_preset': {
    'contrast': 1.2,
    'brightness': 0.1,
    'saturation': 0.9,
    'temperature': 6500,
    'tint': 0.0,
    'shadows': 0.8,
    'highlights': 1.1,
    'gamma': 1.1
}
```

### Custom LUTs

Add `.cube` files to `assets/luts/` directory for custom color grading.

### Environment Variables

Set these for advanced configuration:
```bash
export VIDEO_EDITOR_TEMP_DIR="/path/to/temp"
export VIDEO_EDITOR_OUTPUT_DIR="/path/to/output"
export VIDEO_EDITOR_LOG_LEVEL="DEBUG"
```

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Run `python test_installation.py` to verify setup
3. Check the logs in the application for error details

## System Requirements

- **OS**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **RAM**: 8GB minimum, 16GB recommended
- **Storage**: 10GB free space
- **CPU**: Multi-core processor recommended
- **GPU**: Optional, CPU processing supported

## License

MIT License - feel free to use and modify! 