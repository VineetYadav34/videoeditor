import streamlit as st
import os
import tempfile
import logging
from pathlib import Path
import time
from typing import Optional, Tuple

# Import our modules
from core.scene_detector import SceneDetector
from core.audio_processor import AudioProcessor
from core.music_sync import MusicSync
from core.color_grading import ColorGrading
from core.video_exporter import VideoExporter
from utils.file_utils import FileUtils
from utils.video_utils import VideoUtils

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="Intelligent Video Editor",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .feature-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .progress-section {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .error-message {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application function"""
    
    # Header
    st.markdown('<h1 class="main-header">🎬 Intelligent Video Editor</h1>', unsafe_allow_html=True)
    st.markdown("### Transform raw footage into cinematic content with AI-powered editing")
    
    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Scene detection settings
        st.subheader("Scene Detection")
        scene_threshold = st.slider("Detection Sensitivity", 10.0, 50.0, 30.0, 1.0)
        min_scene_length = st.slider("Minimum Scene Length (s)", 0.5, 5.0, 1.0, 0.1)
        
        # Audio processing settings
        st.subheader("Audio Processing")
        silence_threshold = st.slider("Silence Threshold (dB)", -60.0, -20.0, -40.0, 1.0)
        min_silence_length = st.slider("Min Silence Length (ms)", 200, 1000, 500, 50)
        
        # Color grading settings
        st.subheader("Color Grading")
        color_preset = st.selectbox(
            "Color Preset",
            ["cinematic", "warm", "cool", "vintage", "dramatic"],
            index=0
        )
        
        # Export settings
        st.subheader("Export Settings")
        target_resolution = st.selectbox(
            "Resolution",
            ["1920x1080 (Full HD)", "1280x720 (HD)", "3840x2160 (4K)"],
            index=0
        )
        target_fps = st.selectbox("Frame Rate", [24, 30, 60], index=1)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📁 Upload Files")
        
        # File upload section
        uploaded_video = st.file_uploader(
            "Upload Video File",
            type=['mp4', 'mov', 'avi', 'mkv', 'wmv'],
            help="Upload your raw video footage"
        )
        
        uploaded_music = st.file_uploader(
            "Upload Background Music (Optional)",
            type=['mp3', 'wav', 'm4a', 'flac'],
            help="Add background music to sync with"
        )
        
        # Process button
        if uploaded_video is not None:
            st.success(f"✅ Video uploaded: {uploaded_video.name}")
            
            if st.button("🚀 Process Video", type="primary", use_container_width=True):
                process_video(uploaded_video, uploaded_music, {
                    'scene_threshold': scene_threshold,
                    'min_scene_length': min_scene_length,
                    'silence_threshold': silence_threshold,
                    'min_silence_length': min_silence_length,
                    'color_preset': color_preset,
                    'target_resolution': target_resolution,
                    'target_fps': target_fps
                })
    
    with col2:
        st.header("📊 Features")
        
        features = [
            "🎬 **Automatic Scene Detection**",
            "🔇 **Smart Silence Removal**",
            "🎵 **Music Beat Sync**",
            "🎨 **Cinematic Color Grading**",
            "📤 **High-Quality Export**",
            "⚡ **Fast Processing**"
        ]
        
        for feature in features:
            st.markdown(f'<div class="feature-card">{feature}</div>', unsafe_allow_html=True)

def process_video(video_file, music_file, settings):
    """Process the uploaded video with all features"""
    
    # Create progress section
    progress_section = st.container()
    
    with progress_section:
        st.markdown('<div class="progress-section">', unsafe_allow_html=True)
        st.subheader("🔄 Processing Video")
        
        # Create temporary files
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_video:
            tmp_video.write(video_file.getvalue())
            video_path = tmp_video.name
        
        music_path = None
        if music_file:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_music:
                tmp_music.write(music_file.getvalue())
                music_path = tmp_music.name
        
        try:
            # Progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Step 1: Scene Detection
            status_text.text("Step 1/5: Detecting scenes...")
            progress_bar.progress(20)
            
            scene_detector = SceneDetector(
                threshold=settings['scene_threshold'],
                min_scene_length=settings['min_scene_length']
            )
            scenes = scene_detector.detect_scenes(video_path)
            
            if not scenes:
                st.error("❌ No scenes detected. Please try adjusting the sensitivity.")
                return
            
            st.success(f"✅ Detected {len(scenes)} scenes")
            
            # Step 2: Audio Processing
            status_text.text("Step 2/5: Processing audio...")
            progress_bar.progress(40)
            
            audio_processor = AudioProcessor(
                silence_threshold=settings['silence_threshold'],
                min_silence_len=settings['min_silence_length']
            )
            
            # Extract audio and process
            silence_ranges = audio_processor.detect_silence(video_path)
            st.info(f"📊 Found {len(silence_ranges)} silent segments")
            
            # Step 3: Music Sync (if music provided)
            if music_path:
                status_text.text("Step 3/5: Syncing with music...")
                progress_bar.progress(60)
                
                music_sync = MusicSync()
                beat_times = music_sync.detect_beats(music_path)
                
                if beat_times:
                    # Get video duration
                    video_info = VideoUtils.get_video_info(video_path)
                    if video_info:
                        scenes = music_sync.sync_scenes_to_beats(
                            scenes, beat_times, video_info['duration']
                        )
                        st.success(f"🎵 Synced {len(scenes)} scenes to {len(beat_times)} beats")
                else:
                    st.warning("⚠️ Could not detect beats in music")
            else:
                progress_bar.progress(60)
                st.info("⏭️ Skipping music sync (no music provided)")
            
            # Step 4: Color Grading
            status_text.text("Step 4/5: Applying color grading...")
            progress_bar.progress(80)
            
            color_grader = ColorGrading()
            st.success(f"🎨 Applied {settings['color_preset']} color preset")
            
            # Step 5: Export
            status_text.text("Step 5/5: Exporting final video...")
            progress_bar.progress(90)
            
            # Parse resolution
            resolution_map = {
                "1920x1080 (Full HD)": (1920, 1080),
                "1280x720 (HD)": (1280, 720),
                "3840x2160 (4K)": (3840, 2160)
            }
            target_res = resolution_map[settings['target_resolution']]
            
            exporter = VideoExporter()
            output_path = exporter.export_video(
                video_path=video_path,
                scenes=scenes,
                music_path=music_path,
                color_preset=settings['color_preset'],
                target_resolution=target_res,
                target_fps=settings['target_fps']
            )
            
            progress_bar.progress(100)
            status_text.text("✅ Processing complete!")
            
            # Success message
            st.markdown('<div class="success-message">', unsafe_allow_html=True)
            st.success("🎉 Video processing completed successfully!")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Download section
            if output_path and os.path.exists(output_path):
                st.subheader("📥 Download Your Video")
                
                with open(output_path, 'rb') as f:
                    video_bytes = f.read()
                
                st.download_button(
                    label="Download Edited Video",
                    data=video_bytes,
                    file_name=f"edited_{video_file.name}",
                    mime="video/mp4",
                    use_container_width=True
                )
                
                # Show video info
                file_size = len(video_bytes) / (1024 * 1024)  # MB
                st.info(f"📊 File size: {file_size:.1f} MB")
                
                # Preview video
                st.subheader("🎬 Preview")
                st.video(output_path)
            
        except Exception as e:
            st.markdown('<div class="error-message">', unsafe_allow_html=True)
            st.error(f"❌ Error during processing: {str(e)}")
            st.markdown("</div>", unsafe_allow_html=True)
            logger.error(f"Processing error: {str(e)}")
        
        finally:
            # Cleanup temporary files
            try:
                os.unlink(video_path)
                if music_path:
                    os.unlink(music_path)
            except:
                pass

def show_help():
    """Show help information"""
    st.sidebar.header("❓ Help")
    
    with st.sidebar.expander("How to use"):
        st.markdown("""
        1. **Upload Video**: Select your raw video file
        2. **Upload Music** (optional): Add background music
        3. **Adjust Settings**: Configure detection sensitivity
        4. **Process**: Click the process button
        5. **Download**: Get your edited video
        """)
    
    with st.sidebar.expander("Supported Formats"):
        st.markdown("""
        **Video**: MP4, MOV, AVI, MKV, WMV
        **Audio**: MP3, WAV, M4A, FLAC
        **Output**: MP4 (H.264)
        """)
    
    with st.sidebar.expander("Tips"):
        st.markdown("""
        - Higher sensitivity = more scene cuts
        - Lower silence threshold = more aggressive silence removal
        - Music sync works best with clear beats
        - Larger files take longer to process
        """)

if __name__ == "__main__":
    # Show help in sidebar
    show_help()
    
    # Run main app
    main() 